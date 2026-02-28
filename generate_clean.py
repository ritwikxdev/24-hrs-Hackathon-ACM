import sys, re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Fix meta description
text = re.sub(r'<meta name="description" content="AB-FDA[^"]+" />', '<meta name="description" content="AB-FDA &mdash; AI-powered Ayushman Bharat Fraud Detection &amp; Analytics Platform" />', text)

# Fix checkmark in CSS (.tab-feature-list li::before)
# The CSS checkmark was garbled. Replace whatever is inside content: '...' for that block
import re
text = re.sub(r"\.tab-feature-list li::before\s*\{\s*content:\s*'[^']+';", ".tab-feature-list li::before {\\n      content: '\\\\2713';", text)

# Find <body> tag to replace everything from there to the end
idx = text.find("<body>")
if idx == -1:
    print("Could not find <body> tag!")
    sys.exit(1)

clean_css_head = text[:idx]

clean_body = """<body>
  <!-- NAVBAR -->
  <nav class="navbar">
    <div class="navbar-inner">
      <a class="navbar-brand" href="#">
        <div class="brand-logo">AB</div>
        <span class="brand-text">AB<span>-FDA</span></span>
      </a>
      <ul class="navbar-nav">
        <li><a href="#" class="active">Dashboard</a></li>
        <li><a href="#analytics">Analytics</a></li>
        <li><a href="#platform">Platform</a></li>
        <li><a href="#claims-section">Claims</a></li>
      </ul>
      <div class="navbar-actions">
        <button id="syncBtn" class="btn btn-primary btn-sync" title="Sync claims from Firebase">
          <span class="spinner"></span>
          <span class="btn-label">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-2px">
              <path d="M21 2v6h-6"/><path d="M3 12a9 9 0 0 1 15-6.7L21 8"/><path d="M3 22v-6h6"/><path d="M21 12a9 9 0 0 1-15 6.7L3 16"/>
            </svg>
            Sync Firebase
          </span>
        </button>
      </div>
    </div>
  </nav>

  <!-- TICKER BAR -->
  <div class="ticker-bar">
    <div class="ticker-label">&#x1f7e2; Live</div>
    <div class="ticker-track" id="tickerTrack">
      <span class="ticker-item"><span class="dot"></span>Isolation Forest ML Active</span>
      <span class="ticker-item"><span class="dot"></span>Real-time Anomaly Scoring</span>
      <span class="ticker-item"><span class="dot"></span>Firebase Sync Enabled</span>
      <span class="ticker-item"><span class="dot"></span>Billing Fraud Detection</span>
      <span class="ticker-item"><span class="dot"></span>Upcoding Analysis</span>
      <span class="ticker-item"><span class="dot"></span>Government Healthcare Claims Protection</span>
      <span class="ticker-item"><span class="dot"></span>Isolation Forest ML Active</span>
      <span class="ticker-item"><span class="dot"></span>Real-time Anomaly Scoring</span>
      <span class="ticker-item"><span class="dot"></span>Firebase Sync Enabled</span>
      <span class="ticker-item"><span class="dot"></span>Billing Fraud Detection</span>
      <span class="ticker-item"><span class="dot"></span>Upcoding Analysis</span>
      <span class="ticker-item"><span class="dot"></span>Government Healthcare Claims Protection</span>
    </div>
  </div>

  <!-- HERO -->
  <section class="hero">
    <canvas id="hero-canvas"></canvas>
    <div class="hero-grid-overlay"></div>
    <div class="hero-inner">
      <div class="hero-content">
        <div class="hero-tag fade-up da1"><span class="ping-dot"></span>AI Fraud Detection &mdash; Active</div>
        <h1 class="fade-up da2">
          The AI Fraud Detection Platform for <span class="gradient-text">Ayushman Bharat</span>
        </h1>
        <p class="hero-desc fade-up da3">
          Real-time anomaly scoring powered by Isolation Forest ML &mdash; shielding government healthcare claims from billing fraud, upcoding, and systemic abuse without friction.
        </p>
        <div class="hero-actions fade-up da4">
          <a href="#claims-section" class="btn btn-green">View Claims &#x2193;</a>
          <a href="#analytics" class="btn btn-ghost">Analytics</a>
        </div>
        <div class="hero-meta fade-up da5">
          <span class="live-dot"></span>
          <span id="lastSync">Connecting to backend&#x2026;</span>
        </div>
      </div>
      <div class="hero-diagram fade-up da3">
        <div class="diagram-center"><span>&#x1f6e1;&#xfe0f;</span>AB-FDA</div>
        <div class="orbit-icon">&#x1f3e5;</div>
        <div class="orbit-icon">&#x1f510;</div>
        <div class="orbit-icon">&#x1f4f1;</div>
        <div class="orbit-icon">&#x1f4ca;</div>
        <div class="orbit-icon">&#x1f916;</div>
        <div class="orbit-icon">&#x2705;</div>
        <svg class="orbit-line" viewBox="0 0 400 360" fill="none" xmlns="http://www.w3.org/2000/svg">
          <line x1="200" y1="180" x2="320" y2="46" stroke="#2563eb" stroke-width="1" stroke-dasharray="4 4" opacity="0.3"/>
          <line x1="200" y1="180" x2="380" y2="180" stroke="#2563eb" stroke-width="1" stroke-dasharray="4 4" opacity="0.3"/>
          <line x1="200" y1="180" x2="320" y2="314" stroke="#2563eb" stroke-width="1" stroke-dasharray="4 4" opacity="0.3"/>
          <line x1="200" y1="180" x2="80" y2="46" stroke="#2563eb" stroke-width="1" stroke-dasharray="4 4" opacity="0.3"/>
          <line x1="200" y1="180" x2="80" y2="314" stroke="#2563eb" stroke-width="1" stroke-dasharray="4 4" opacity="0.3"/>
        </svg>
      </div>
    </div>
  </section>

  <!-- STAT CARDS -->
  <div class="stats-row">
    <div class="stats-grid">
      <div class="stat-card total reveal d1"><span class="stat-icon">&#x1f4ca;</span><div class="stat-value" id="kpiTotal">&mdash;</div><div class="stat-label">Total Claims</div></div>
      <div class="stat-card high reveal d2"><span class="stat-icon">&#x1f6a8;</span><div class="stat-value" id="kpiHigh">&mdash;</div><div class="stat-label">High Risk</div></div>
      <div class="stat-card medium reveal d3"><span class="stat-icon">&#x26a0;&#xfe0f;</span><div class="stat-value" id="kpiMedium">&mdash;</div><div class="stat-label">Medium Risk</div></div>
      <div class="stat-card low reveal d4"><span class="stat-icon">&#x2705;</span><div class="stat-value" id="kpiLow">&mdash;</div><div class="stat-label">Low Risk</div></div>
      <div class="stat-card amount reveal d5"><span class="stat-icon">&#x1f4b0;</span><div class="stat-value" id="kpiAmount">&mdash;</div><div class="stat-label">Total &#x20b9; Claimed</div></div>
    </div>
  </div>

  <!-- FEATURE TABS -->
  <section id="platform" class="tabs-section">
    <div class="tabs-section-inner">
      <h2 class="tabs-section-title reveal d1">Our end-to-end platform covers the entire healthcare fraud lifecycle &mdash; from claim submission to risk assessment.</h2>
      <div class="tabs-nav reveal d2">
        <button class="tab-btn active" onclick="switchTab(this,'tab-claims')">Claims Intelligence</button>
        <button class="tab-btn" onclick="switchTab(this,'tab-risk')">Risk Scoring</button>
        <button class="tab-btn" onclick="switchTab(this,'tab-ai')">AI Fraud Detection</button>
      </div>
      <div id="tab-claims" class="tab-content active">
        <div class="tab-text">
          <h3>Intelligent Claims Processing</h3>
          <p>Our platform ingests Ayushman Bharat claims data from Firebase in real time, normalises hospital and patient records, and prepares them for ML scoring.</p>
          <ul class="tab-feature-list">
            <li>Real-time Firebase data ingestion</li>
            <li>Automated hospital record normalisation</li>
            <li>Duplicate claim detection</li>
            <li>Multi-hospital claim aggregation</li>
          </ul>
        </div>
        <div class="tab-visual"><div class="tab-visual-inner"><div class="tab-visual-icon">&#x1f4cb;</div><div class="tab-visual-label">Claims synced from Firebase Firestore instantly</div></div></div>
      </div>
      <div id="tab-risk" class="tab-content">
        <div class="tab-text">
          <h3>Real-Time Risk Scoring</h3>
          <p>Each claim receives an anomaly score from our Isolation Forest model. Claims are classified as High, Medium, or Low risk based on billing patterns and procedure codes.</p>
          <ul class="tab-feature-list">
            <li>Isolation Forest ML anomaly detection</li>
            <li>Per-claim fraud score (0&ndash;100)</li>
            <li>HIGH / MEDIUM / LOW risk classification</li>
            <li>Visual score bars for quick review</li>
          </ul>
        </div>
        <div class="tab-visual"><div class="tab-visual-inner"><div class="tab-visual-icon">&#x1f3af;</div><div class="tab-visual-label">ML model scores every claim in milliseconds</div></div></div>
      </div>
      <div id="tab-ai" class="tab-content">
        <div class="tab-text">
          <h3>AI-Powered Fraud Detection</h3>
          <p>Our AI identifies billing fraud, upcoding, ghost patients, and systemic abuse by analysing patterns across thousands of claims simultaneously.</p>
          <ul class="tab-feature-list">
            <li>Billing fraud pattern recognition</li>
            <li>Upcoding and unbundling detection</li>
            <li>Ghost patient &amp; phantom claim flags</li>
            <li>Cross-hospital comparison analytics</li>
          </ul>
        </div>
        <div class="tab-visual"><div class="tab-visual-inner"><div class="tab-visual-icon">&#x1f916;</div><div class="tab-visual-label">Powered by scikit-learn Isolation Forest</div></div></div>
      </div>
    </div>
  </section>

  <!-- MAIN CONTENT -->
  <main class="content">
    <section id="analytics">
      <div class="section-header reveal d2">
        <div><h2>Analytics Overview</h2><p>Claimed amounts breakdown &amp; risk distribution</p></div>
      </div>
      <div class="charts-grid">
        <div class="chart-card reveal d3">
          <h3>Claimed Amount by Hospital <span style="font-weight:500;color:var(--muted);font-size:.65rem;text-transform:none;letter-spacing:0;margin-left:4px">&middot; color = risk level</span></h3>
          <div class="chart-container"><canvas id="barChart"></canvas></div>
        </div>
        <div class="chart-card reveal d4">
          <h3>Risk Distribution</h3>
          <div class="chart-container"><canvas id="doughnutChart"></canvas></div>
        </div>
      </div>
    </section>

    <section id="claims-section">
      <div class="section-header reveal d2">
        <div><h2>All Claims</h2><p>Search, filter and review individual claim records</p></div>
      </div>
      <div class="toolbar reveal d3">
        <div class="search-wrap">
          <span class="search-icon"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg></span>
          <input type="text" id="searchInput" placeholder="Search by hospital, patient ID, diagnosis&#x2026;"/>
        </div>
        <select class="filter-select" id="riskFilter">
          <option value="">All Risk Levels</option>
          <option value="HIGH">&#x1f534; High Risk</option>
          <option value="MEDIUM">&#x1f7e1; Medium Risk</option>
          <option value="LOW">&#x1f7e2; Low Risk</option>
        </select>
        <select class="filter-select" id="hospitalFilter"><option value="">All Hospitals</option></select>
      </div>
      <div class="table-card reveal d4">
        <div class="table-wrapper">
          <table>
            <thead><tr><th>Claim ID</th><th>Hospital</th><th>Patient ID</th><th>Diagnosis / Procedure</th><th>Claimed (&#x20b9;)</th><th>Fraud Score</th><th>Type</th><th>Risk</th></tr></thead>
            <tbody id="claimsBody">
              <tr><td colspan="8"><div class="skeleton" style="height:16px;width:100%;margin:10px 0"></div></td></tr>
              <tr><td colspan="8"><div class="skeleton" style="height:16px;width:93%;margin:10px 0"></div></td></tr>
              <tr><td colspan="8"><div class="skeleton" style="height:16px;width:87%;margin:10px 0"></div></td></tr>
              <tr><td colspan="8"><div class="skeleton" style="height:16px;width:80%;margin:10px 0"></div></td></tr>
            </tbody>
          </table>
        </div>
        <div class="empty-state" id="emptyState" style="display:none">
          <div class="empty-icon">&#x1f4ed;</div>
          <h3>No claims found</h3>
          <p>Click <strong>Sync Firebase</strong> to pull latest claim data, or adjust your filters.</p>
        </div>
      </div>
    </section>
  </main>

  <!-- CTA -->
  <section class="cta-section">
    <h2>Protect Healthcare. Protect Public Funds.</h2>
    <p>Experience how AB-FDA uses AI to detect scams, reduce false positives, and build accountability in government healthcare schemes.</p>
    <a href="#claims-section" class="btn btn-green">View Live Claims</a>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="footer-inner">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="footer-logo"><div class="logo">AB</div>AB-FDA</div>
          <p>AI-powered fraud detection &amp; analytics platform protecting Ayushman Bharat healthcare claims in real time.</p>
        </div>
        <div class="footer-col"><h4>Platform</h4><ul><li><a href="#">Dashboard</a></li><li><a href="#">Claims Analysis</a></li><li><a href="#">ML Pipeline</a></li><li><a href="#">Risk Scoring</a></li></ul></div>
        <div class="footer-col"><h4>Resources</h4><ul><li><a href="#">Documentation</a></li><li><a href="#">API Reference</a></li><li><a href="#">Research</a></li></ul></div>
        <div class="footer-col"><h4>Company</h4><ul><li><a href="#">About Us</a></li><li><a href="#">Contact</a></li><li><a href="#">Privacy Policy</a></li></ul></div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 AB-FDA. Built for ACM Hackathon.</p>
        <div class="footer-links"><a href="#">Privacy</a><a href="#">Terms</a><a href="#">Support</a></div>
      </div>
    </div>
  </footer>

  <div class="toast-container" id="toastContainer"></div>

  <script>
    const API = 'http://127.0.0.1:8000';
    let allClaims = [];
    const $ = s => document.querySelector(s);

    // ── TAB SWITCHER ───────────────────────────────────
    function switchTab(btn, tabId) {
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
      btn.classList.add('active');
      document.getElementById(tabId).classList.add('active');
    }

    // ── HERO CANVAS PARTICLES ──────────────────────────
    (function () {
      const canvas = document.getElementById('hero-canvas');
      const ctx = canvas.getContext('2d');
      let W, H, particles = [];
      function resize() { W = canvas.width = canvas.offsetWidth; H = canvas.height = canvas.offsetHeight; }
      resize();
      window.addEventListener('resize', () => { resize(); init(); });
      function rand(a, b) { return a + Math.random() * (b - a); }
      function init() {
        const count = Math.floor(W / 18);
        particles = Array.from({ length: count }, () => ({
          x: rand(0, W), y: rand(0, H),
          vx: rand(-0.3, 0.3), vy: rand(-0.3, 0.3),
          r: rand(1, 2.2), a: rand(0.1, 0.4)
        }));
      }
      init();
      function draw() {
        ctx.clearRect(0, 0, W, H);
        particles.forEach(p => {
          p.x += p.vx; p.y += p.vy;
          if (p.x < 0) p.x = W; if (p.x > W) p.x = 0;
          if (p.y < 0) p.y = H; if (p.y > H) p.y = 0;
          ctx.beginPath();
          ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
          ctx.fillStyle = `rgba(37,99,235,${p.a})`;
          ctx.fill();
        });
        for (let i = 0; i < particles.length; i++) {
          for (let j = i + 1; j < particles.length; j++) {
            const dx = particles[i].x - particles[j].x;
            const dy = particles[i].y - particles[j].y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < 100) {
              ctx.beginPath();
              ctx.moveTo(particles[i].x, particles[i].y);
              ctx.lineTo(particles[j].x, particles[j].y);
              ctx.strokeStyle = `rgba(37,99,235,${0.12 * (1 - dist / 100)})`;
              ctx.lineWidth = 0.7;
              ctx.stroke();
            }
          }
        }
        requestAnimationFrame(draw);
      }
      draw();
    })();

    // ── SCROLL REVEAL ──────────────────────────────────
    const revealObserver = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); revealObserver.unobserve(e.target); } });
    }, { threshold: 0.12 });
    document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

    // ── TOAST ──────────────────────────────────────────
    function toast(msg, type = 'success') {
      const el = document.createElement('div');
      el.className = `toast ${type}`;
      el.textContent = msg;
      $('#toastContainer').appendChild(el);
      setTimeout(() => { el.style.animation = 'toastOut .3s ease forwards'; setTimeout(() => el.remove(), 300); }, 3800);
    }

    // ── FORMAT ─────────────────────────────────────────
    const fmt = n => new Intl.NumberFormat('en-IN').format(n);
    const fmtCr = n => {
      if (n >= 1e7) return '&#x20b9;' + (n / 1e7).toFixed(2) + ' Cr';
      if (n >= 1e5) return '&#x20b9;' + (n / 1e5).toFixed(2) + ' L';
      return '&#x20b9;' + fmt(Math.round(n));
    };
    function esc(s) { if (!s) return ''; const d = document.createElement('div'); d.textContent = s; return d.innerHTML; }

    // ── FETCH ──────────────────────────────────────────
    async function fetchClaims() {
      try {
        const res = await fetch(`${API}/claims`);
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        allClaims = await res.json();
        $('#lastSync').textContent = `Last loaded ${new Date().toLocaleTimeString()} &middot; ${allClaims.length} records`;
        updateDashboard();
      } catch (err) {
        console.error(err);
        toast('Failed to load claims &mdash; is the backend running on port 8000?', 'error');
        showEmpty();
      }
    }

    // ── SYNC ───────────────────────────────────────────
    const syncBtn = $('#syncBtn');
    syncBtn.addEventListener('click', async () => {
      syncBtn.classList.add('loading');
      try {
        const res = await fetch(`${API}/sync`, { method: 'POST' });
        if (!res.ok) { const e = await res.json().catch(() => ({})); throw new Error(e.detail || `HTTP ${res.status}`); }
        const data = await res.json();
        toast(`&#x2713; Synced ${data.count} claims from Firebase`);
        await fetchClaims();
      } catch (err) {
        console.error(err);
        toast(`Sync failed: ${err.message}`, 'error');
      } finally {
        syncBtn.classList.remove('loading');
      }
    });

    // ── FILTERS ────────────────────────────────────────
    const searchInput = $('#searchInput'), riskFilter = $('#riskFilter'), hospitalFilter = $('#hospitalFilter');
    searchInput.addEventListener('input', renderFiltered);
    riskFilter.addEventListener('change', renderFiltered);
    hospitalFilter.addEventListener('change', renderFiltered);

    function getFiltered() {
      const q = searchInput.value.toLowerCase().trim();
      const risk = riskFilter.value, hosp = hospitalFilter.value;
      return allClaims.filter(c => {
        if (risk && c.risk !== risk) return false;
        if (hosp && (c.hosp || '') !== hosp) return false;
        if (q) { const hay = `${c.id} ${c.hosp} ${c.pid} ${c.proc}`.toLowerCase(); if (!hay.includes(q)) return false; }
        return true;
      });
    }
    function renderFiltered() { renderTable(getFiltered()); }

    // ── DASHBOARD UPDATE ───────────────────────────────
    function updateDashboard() {
      const high = allClaims.filter(c => c.risk === 'HIGH').length;
      const medium = allClaims.filter(c => c.risk === 'MEDIUM').length;
      const low = allClaims.filter(c => c.risk === 'LOW').length;
      const total = allClaims.length;
      const totalAmt = allClaims.reduce((s, c) => s + (c.claimed || 0), 0);
      animateVal('kpiTotal', total); animateVal('kpiHigh', high);
      animateVal('kpiMedium', medium); animateVal('kpiLow', low);
      $('#kpiAmount').innerHTML = fmtCr(totalAmt);
      const hospitals = [...new Set(allClaims.map(c => c.hosp || 'Unregistered Hospital'))].sort();
      hospitalFilter.innerHTML = '<option value="">All Hospitals</option>' + hospitals.map(h => `<option value="${esc(h)}">${esc(h)}</option>`).join('');
      renderTable(allClaims);
      renderBarChart();
      renderDoughnut(high, medium, low);
    }

    // ── ANIMATE NUMBER ─────────────────────────────────
    function animateVal(id, target) {
      const el = document.getElementById(id);
      const start = parseInt(el.textContent) || 0;
      const dur = 750, t0 = performance.now();
      (function step(now) {
        const p = Math.min((now - t0) / dur, 1);
        const ease = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(start + (target - start) * ease);
        if (p < 1) requestAnimationFrame(step);
      })(t0);
    }

    // ── RENDER TABLE ───────────────────────────────────
    function renderTable(data) {
      const body = $('#claimsBody'), empty = $('#emptyState');
      if (!data.length) { body.innerHTML = ''; empty.style.display = ''; return; }
      empty.style.display = 'none';
      body.innerHTML = data.map(c => {
        const s = Math.round(c.score);
        const sc = s >= 80 ? 'var(--red)' : s >= 50 ? 'var(--amber)' : 'var(--green)';
        const rk = c.risk.toLowerCase();
        const isUnreg = !c.hosp;
        const hospDisplay = c.hosp || 'Unregistered Hospital';
        return `<tr${isUnreg ? ' style="opacity:.55"' : ''}>
          <td class="id-cell" title="${c.id}">${c.id}</td>
          <td class="hosp-cell"${isUnreg ? ' style="font-style:italic;color:var(--muted)"' : ''}>${esc(hospDisplay)}</td>
          <td>${esc(c.pid)}</td><td class="proc-cell">${esc(c.proc || '—')}</td>
          <td class="amount">&#x20b9;${fmt(Math.round(c.claimed))}</td>
          <td><div class="score-bar-wrap"><span class="score-num" style="color:${sc}">${s}</span><div class="score-track"><div class="score-fill" style="width:${c.score}%;background:${sc}"></div></div></div></td>
          <td style="text-transform:capitalize;color:var(--muted)">${esc(c.type)}</td>
          <td><span class="badge ${rk}">${c.risk}</span></td>
        </tr>`;
      }).join('');
    }
    function showEmpty() { $('#claimsBody').innerHTML = ''; $('#emptyState').style.display = ''; }

    // ── BAR CHART ──────────────────────────────────────
    let barInstance = null;
    function renderBarChart() {
      const hospMap = {};
      allClaims.forEach(c => {
        const h = c.hosp; if (!h || h === 'Unregistered Hospital') return;
        if (!hospMap[h]) hospMap[h] = { total: 0, maxRisk: 'LOW' };
        hospMap[h].total += c.claimed || 0;
        if (c.risk === 'HIGH') hospMap[h].maxRisk = 'HIGH';
        else if (c.risk === 'MEDIUM' && hospMap[h].maxRisk !== 'HIGH') hospMap[h].maxRisk = 'MEDIUM';
      });
      const labels = Object.keys(hospMap).sort((a, b) => hospMap[b].total - hospMap[a].total);
      const totals = labels.map(h => Math.round(hospMap[h].total));
      const rp = {
        HIGH: { bg: 'rgba(239,68,68,0.75)', border: '#ef4444' },
        MEDIUM: { bg: 'rgba(245,158,11,0.75)', border: '#f59e0b' },
        LOW: { bg: 'rgba(16,185,129,0.7)', border: '#10b981' },
      };
      const bgColors = labels.map(h => rp[hospMap[h].maxRisk].bg);
      const borderColors = labels.map(h => rp[hospMap[h].maxRisk].border);
      if (barInstance) barInstance.destroy();
      barInstance = new Chart($('#barChart'), {
        type: 'bar',
        data: { labels, datasets: [{ label: 'Total Claimed', data: totals, backgroundColor: bgColors, borderColor: borderColors, borderWidth: 2, borderRadius: 10, borderSkipped: false, barPercentage: 0.6, categoryPercentage: 0.75 }] },
        options: {
          responsive: true, maintainAspectRatio: false,
          animation: { duration: 900, easing: 'easeOutQuart' },
          plugins: {
            legend: { display: false },
            tooltip: {
              backgroundColor: '#fff', titleColor: '#1a2540', bodyColor: '#64748b',
              borderColor: 'rgba(37,99,235,0.15)', borderWidth: 1,
              cornerRadius: 10, padding: 14,
              titleFont: { family: 'Inter', weight: '700', size: 12 },
              bodyFont: { family: 'Inter', size: 12 },
              callbacks: {
                title: ctx => ctx[0].label,
                label: ctx => ` ₹${fmt(ctx.parsed.y)} · ${hospMap[ctx.label]?.maxRisk || ''} risk`
              }
            }
          },
          scales: {
            x: {
              ticks: { color: '#64748b', font: { size: 11, family: 'Inter', weight: '600' }, maxRotation: 35,
                callback: function (v) { const l = this.getLabelForValue(v); return l.length > 14 ? l.slice(0, 14) + '…' : l; }
              },
              grid: { display: false }, border: { display: false }
            },
            y: {
              ticks: { color: '#94a3b8', font: { size: 11, family: 'Inter' }, callback: v => fmtCr(v) },
              grid: { color: 'rgba(37,99,235,0.06)' }, border: { display: false }
            }
          }
        }
      });
    }

    // ── DOUGHNUT CHART ─────────────────────────────────
    let doughnutInst = null;
    const centerTextPlugin = {
      id: 'centerText',
      beforeDraw(chart) {
        if (chart.config.type !== 'doughnut') return;
        const { width, height, ctx } = chart;
        const total = chart.data.datasets[0].data.reduce((a, b) => a + b, 0);
        ctx.save();
        const cx = width / 2, cy = height / 2 - 14;
        ctx.font = '700 1.8rem Inter, sans-serif';
        ctx.fillStyle = '#1a2540';
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText(total, cx, cy);
        ctx.font = '600 .65rem Inter, sans-serif';
        ctx.fillStyle = '#64748b';
        ctx.fillText('TOTAL CLAIMS', cx, cy + 24);
        ctx.restore();
      }
    };
    function renderDoughnut(high, medium, low) {
      if (doughnutInst) doughnutInst.destroy();
      doughnutInst = new Chart($('#doughnutChart'), {
        type: 'doughnut', plugins: [centerTextPlugin],
        data: {
          labels: ['High Risk', 'Medium Risk', 'Low Risk'],
          datasets: [{ data: [high, medium, low],
            backgroundColor: ['#ef4444', '#f59e0b', '#10b981'],
            hoverBackgroundColor: ['#dc2626', '#d97706', '#059669'],
            borderColor: '#ffffff', borderWidth: 3, hoverOffset: 14, borderRadius: 6
          }]
        },
        options: {
          responsive: true, maintainAspectRatio: false, cutout: '70%',
          animation: { duration: 900, easing: 'easeOutQuart' },
          plugins: {
            legend: { position: 'bottom', labels: { color: '#334155', font: { family: 'Inter', size: 12, weight: '600' }, padding: 22, usePointStyle: true, pointStyleWidth: 12 } },
            tooltip: {
              backgroundColor: '#fff', titleColor: '#1a2540', bodyColor: '#64748b',
              borderColor: 'rgba(37,99,235,0.15)', borderWidth: 1,
              cornerRadius: 10, padding: 14,
              titleFont: { family: 'Inter', weight: '700', size: 13 },
              bodyFont: { family: 'Inter', size: 12 },
              callbacks: {
                label: ctx => {
                  const total = ctx.dataset.data.reduce((a, b) => a + b, 0);
                  const pct = ((ctx.parsed / total) * 100).toFixed(1);
                  return ` ${ctx.label}: ${ctx.parsed} claims (${pct}%)`;
                }
              }
            }
          }
        }
      });
    }

    // ── BOOT ───────────────────────────────────────────
    fetchClaims();
  </script>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(clean_css_head + clean_body)

print("Rewrote index.html cleanly using pure HTML entities.")
