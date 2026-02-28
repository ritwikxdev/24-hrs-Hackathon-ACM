import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import hashlib

def compute_scores(raw_claims):
    """
    Enhanced AI Fraud Detection Pipeline.
    Uses multidimensional Isolation Forest to score claims based on:
    - Claim Amount
    - Hospital frequency encoding 
    - Diagnosis/Procedure frequency encoding
    - Patient claim velocity (claims per patient)
    """
    if not raw_claims:
        return pd.DataFrame(columns=["id", "claimed", "score", "type", "risk"])

    df = pd.DataFrame(raw_claims)
    
    # 1. Clean numerical amount
    df["claimed"] = pd.to_numeric(df.get("billedAmount", 0), errors="coerce").fillna(0)
    
    # If hardly any data, fallback to safe defaults
    if len(df) < 5:
        df["score"] = 0.0
        df["type"] = "clean"
        df["risk"] = "LOW"
        return df

    # 2. Extract and encode categorical features
    # Hospital Frequency Encoding
    hosp_col = df.get("hospitalName", df.get("hosp", "Unknown")).fillna("Unknown")
    df["hosp_freq"] = hosp_col.map(hosp_col.value_counts(normalize=True))
    
    # Diagnosis/Procedure Frequency
    diag_col = df.get("diagnosis", df.get("proc", "Unknown")).fillna("Unknown")
    df["diag_freq"] = diag_col.map(diag_col.value_counts(normalize=True))
    
    # Patient Claim Velocity (How many claims has this patient made?)
    pid_col = df.get("patientId", df.get("pid", "Unknown")).fillna("Unknown")
    patient_counts = pid_col.value_counts()
    df["patient_velocity"] = pid_col.map(patient_counts)

    # 3. Build Feature Matrix (X)
    # We log-transform claimed amount because medical billing is highly right-skewed
    X = pd.DataFrame({
        "log_amount": np.log1p(df["claimed"]),
        "hosp_freq": df["hosp_freq"],
        "diag_freq": df["diag_freq"],
        "patient_velocity": df["patient_velocity"]
    })

    # Fill any remaining NaNs
    X = X.fillna(0)

    # 4. Train AI Model (Isolation Forest)
    # We use a 10% expected fraud rate (contamination)
    iso = IsolationForest(
        n_estimators=150,     # More trees = more stable scoring
        contamination=0.10,   # Expected anomaly rate
        max_features=1.0, 
        bootstrap=True,
        random_state=42
    )
    
    iso.fit(X.values)
    
    # decision_function gives negative scores to anomalies. 
    # We negate so higher score = higher anomaly.
    raw_scores = -iso.decision_function(X.values)
    
    # 5. Normalize Scores to 0-100 range for the UI
    s_min, s_max = raw_scores.min(), raw_scores.max()
    if s_max == s_min:
        df["score"] = 0.0
    else:
        # Scale and tightly bound to 0-100
        normalized = (raw_scores - s_min) / (s_max - s_min) * 100
        df["score"] = np.clip(normalized, 0, 100)

    # 6. AI Categorization Rules
    df["type"] = "clean"
    df["risk"] = "LOW"
    
    for idx, row in df.iterrows():
        score = row["score"]
        amt = row["claimed"]
        vel = row["patient_velocity"]
        
        # Risk thresholds
        if score >= 85:
            df.at[idx, "risk"] = "HIGH"
        elif score >= 55:
            df.at[idx, "risk"] = "MEDIUM"
            
        # Determine specific AI Fraud Type based on which features drove the anomaly
        if score >= 55:
            if vel > 3:  # Patient has many claims
                df.at[idx, "type"] = "identity_theft"
            elif row["hosp_freq"] < 0.05 and amt > df["claimed"].median() * 3:
                # Rare hospital billing unusually high amounts
                df.at[idx, "type"] = "phantom_billing"
            elif amt > df["claimed"].median() * 5:
                # Massively expensive procedure
                df.at[idx, "type"] = "upcode"
            else:
                df.at[idx, "type"] = "systemic_abuse"
                
    return df
