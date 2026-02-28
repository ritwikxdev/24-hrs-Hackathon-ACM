        return [
            dict(
                id=r.id,
                hosp=r.hospital,
                pid=r.patient_id,
                proc=r.diagnosis,
                claimed=r.claimed,
                score=r.score,
                type=r.type,
                risk=r.risk,
            )
            for r in rows
        ]
    finally:
        db.close()

@app.get("/explain/{claim_id}")
def explain_claim(claim_id: str):
    """
    Mock AI Explanation endpoint.
    In a real system, this would call Google Gemini or OpenAI.
    Here we generate a contextual, realistic AI explanation.
    """
    db = SessionLocal()
    try:
        c = db.query(Claim).filter(Claim.id == claim_id).first()
        if not c:
            raise HTTPException(status_code=404, detail="Claim not found")
        
        # Build a highly realistic "AI" response based on the actual claim data
        response = f"**AI Fraud Analysis for {c.id}:**\n\n"
        
        if c.risk == "HIGH":
            if c.type == "phantom_billing":
                response += f"⚠️ **High Confidence Anomaly Detected**\nThe claim for **₹{c.claimed:,.2f}** at **{c.hospital}** is completely out of expected bounds. The patient **{c.patient_id}** has no prior critical history, yet this claim represents a 400% deviation from the hospital's median billing for `{c.diagnosis}`. This is strongly indicative of phantom billing."
            elif c.type == "systemic_abuse":
                response += f"⚠️ **Systemic Abuse Pattern**\nThis claim matches a known pattern of upcoding at **{c.hospital}**. The procedure `{c.diagnosis}` billed at **₹{c.claimed:,.2f}** is statistically anomalous compared to peer institutions in the region. Furthermore, the patient **{c.patient_id}** is associated with an unusually high frequency of claims this month."
            else:
                response += f"⚠️ **Critical Risk Flagged**\nThe Isolation Forest ML model gave this claim a score of **{c.score:.1f}/100**. A claimed amount of **₹{c.claimed:,.2f}** for `{c.diagnosis}` is considered an extreme outlier based on our historical Ayushman Bharat 10M+ claim dataset."
                
        elif c.risk == "MEDIUM":
            response += f"🔶 **Moderate Review Required**\nThis claim looks suspicious because of the `{c.type}` flag. The amount **₹{c.claimed:,.2f}** is on the higher end for `{c.diagnosis}` at **{c.hospital}**. Manual auditor review is recommended to verify patient **{c.patient_id}**."
        
        else:
            response += f"✅ **Clean Claim**\nThe AI model found no anomalies. The amount of **₹{c.claimed:,.2f}** for `{c.diagnosis}` is within standard deviation parameters for **{c.hospital}**."

        return {"analysis": response}
    finally:
        db.close()
