"""
CarDekho — Design System
Playfair Display (titres) + DM Sans (corps) + DM Mono (labels/code)
"""

ENHANCED_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

/* ── TOKENS ─────────────────────────────────────────────────── */
:root {
    --ink:        #1C1917;
    --ink2:       #44403C;
    --ink3:       #78716C;
    --cream:      #FAFAF8;
    --cream2:     #F5F3EF;
    --cream3:     #EDE9E3;
    --teal:       #0D6E68;
    --teal2:      #0A5652;
    --teal-light: #E8F4F3;
    --teal-glow:  #5DCAA5;
    --amber:      #C2710C;
    --red:        #B91C1C;
    --border:     rgba(28,25,23,0.12);
    --border2:    rgba(28,25,23,0.22);
}

/* ── HIDE STREAMLIT CHROME ───────────────────────────────────── */
[data-testid="collapsedControl"],
section[data-testid="stSidebar"],
header[data-testid="stHeader"],
#MainMenu, footer,
[data-testid="stToolbar"],
[data-testid="stDecoration"] { display: none !important; }

/* ── GLOBAL ──────────────────────────────────────────────────── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
    color: var(--ink);
    background-color: var(--cream) !important;
}
section[data-testid="stMain"] > div:first-child { padding-top: 68px !important; }
section[data-testid="stMain"] > div { padding-bottom: 56px; }

/* ── NAVBAR ──────────────────────────────────────────────────── */
.app-navbar {
    position: fixed; top: 0; left: 0; right: 0;
    display: flex; align-items: center; gap: 14px;
    background: var(--ink);
    padding: 0 32px; height: 60px;
    border-bottom: 3px solid var(--teal);
    z-index: 9998; box-sizing: border-box;
}
.nav-logo {
    width: 36px; height: 36px; background: var(--teal);
    border-radius: 6px; display: flex;
    align-items: center; justify-content: center; flex-shrink: 0;
}
.nav-logo svg { width: 20px; height: 20px; fill: white; }
.nav-title {
    font-family: 'Playfair Display', serif;
    font-size: 17px; font-weight: 700;
    color: white; margin: 0; letter-spacing: 0.01em;
}
.nav-sub {
    font-family: 'DM Mono', monospace;
    font-size: 10px; color: var(--ink3);
    text-transform: uppercase; letter-spacing: 0.15em; margin: 1px 0 0;
}
.nav-badge {
    margin-left: auto; background: var(--teal); color: white;
    font-size: 10px; font-weight: 600; padding: 4px 12px;
    border-radius: 3px; text-transform: uppercase; letter-spacing: 0.12em;
}

/* ── FOOTER ──────────────────────────────────────────────────── */
.app-footer {
    position: fixed; bottom: 0; left: 0; right: 0;
    background: var(--cream2); border-top: 1px solid var(--border);
    padding: 10px 32px; display: flex;
    justify-content: space-between; align-items: center;
    font-size: 12px; color: var(--ink3); z-index: 9999;
}
.footer-id {
    font-family: 'DM Mono', monospace;
    font-size: 10px; letter-spacing: 0.1em;
}

/* ── HERO ────────────────────────────────────────────────────── */
.hero-banner {
    background: var(--ink); color: white;
    padding: 72px 48px 64px;
    margin-top: -68px;
    margin-left: calc(-50vw + 50%);
    margin-right: calc(-50vw + 50%);
    margin-bottom: 0;
    width: 100vw;
    position: relative; overflow: hidden;
}
.hero-banner::before {
    content: ''; position: absolute; inset: 0;
    background:
        repeating-linear-gradient(90deg,rgba(255,255,255,.015) 0,rgba(255,255,255,.015) 1px,transparent 1px,transparent 80px),
        repeating-linear-gradient(0deg, rgba(255,255,255,.015) 0,rgba(255,255,255,.015) 1px,transparent 1px,transparent 80px);
    pointer-events: none;
}
.hero-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px; text-transform: uppercase; letter-spacing: 0.2em;
    color: var(--teal-glow); margin-bottom: 20px;
    display: flex; align-items: center; gap: 10px;
}
.hero-label::before {
    content: ''; display: inline-block;
    width: 28px; height: 1px; background: var(--teal-glow);
}
.hero-h1 {
    font-family: 'Playfair Display', serif !important;
    font-size: 3rem !important; line-height: 1.12 !important;
    color: white !important; font-weight: 700 !important;
    max-width: 600px; margin-bottom: 20px !important;
}
.hero-h1 em { color: var(--teal-glow); font-style: italic; }
.hero-sub {
    font-size: 15px; color: rgba(255,255,255,.55);
    max-width: 500px; line-height: 1.7; margin-bottom: 36px;
}

/* ── HERO BUTTON ─────────────────────────────────────────────── */
.hero-cta-btn {
    display: inline-flex; align-items: center; gap: 10px;
    background: var(--teal); color: white;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px; font-weight: 600; letter-spacing: 0.03em;
    padding: 14px 28px; border-radius: 4px;
    border: none; cursor: pointer;
    transition: background 0.15s, transform 0.1s;
    text-decoration: none;
}
.hero-cta-btn:hover {
    background: var(--teal2); transform: translateY(-1px);
}
.hero-cta-btn svg {
    width: 16px; height: 16px;
    stroke: white; stroke-width: 2.5; fill: none;
}

/* ── HERO STATS ──────────────────────────────────────────────── */
.hero-stats {
    display: flex; gap: 0;
    border-top: 1px solid rgba(255,255,255,.1);
    padding-top: 36px; margin-top: 48px;
}
.hero-stat {
    padding: 0 40px 0 0;
    border-right: 1px solid rgba(255,255,255,.1);
    margin-right: 40px;
}
.hero-stat:last-child { border: none; margin: 0; padding: 0; }
.hero-stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 34px; font-weight: 700;
    color: white; line-height: 1;
}
.hero-stat-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px; color: rgba(255,255,255,.4);
    text-transform: uppercase; letter-spacing: 0.12em; margin-top: 5px;
}

/* ── FEATURES STRIP ──────────────────────────────────────────── */
.features-strip {
    background: var(--teal); padding: 18px 48px;
    display: flex; justify-content: space-between; align-items: center;
    margin-left: calc(-50vw + 50%);
    margin-right: calc(-50vw + 50%);
    width: 100vw; margin-bottom: 40px;
}
.feature-item {
    display: flex; align-items: center; gap: 10px; color: white;
}
.feature-dot {
    width: 6px; height: 6px; border-radius: 50%;
    background: rgba(255,255,255,.5); flex-shrink: 0;
}
.feature-text {
    font-family: 'DM Mono', monospace;
    font-size: 11px; letter-spacing: 0.04em;
}

/* ── SECTION LABEL ───────────────────────────────────────────── */
.section-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px; text-transform: uppercase;
    letter-spacing: 0.2em; color: var(--ink3); margin-bottom: 6px;
}

/* ── STEP CARDS ──────────────────────────────────────────────── */
.step-card {
    background: white; border: 1px solid var(--border);
    border-radius: 8px; padding: 28px 24px; height: 100%;
}
.step-num {
    font-family: 'DM Mono', monospace; font-size: 11px;
    font-weight: 600; color: var(--teal); letter-spacing: 0.1em;
    text-transform: uppercase; margin-bottom: 14px;
}
.step-card h4 {
    font-family: 'Playfair Display', serif !important;
    font-size: 16px !important; font-weight: 600 !important;
    margin-bottom: 10px !important; color: var(--ink) !important;
}
.step-card p { font-size: 13px; color: var(--ink3); line-height: 1.65; margin: 0; }

/* ── DATASET TABLE ───────────────────────────────────────────── */
.dataset-table {
    width: 100%; border-collapse: collapse; font-size: 13px;
    border: 1px solid var(--border); border-radius: 8px; overflow: hidden;
}
.dataset-table th {
    text-align: left; font-family: 'DM Mono', monospace;
    font-size: 10px; text-transform: uppercase; letter-spacing: 0.12em;
    color: var(--ink3); padding: 10px 16px;
    background: var(--cream2); border-bottom: 1px solid var(--border);
}
.dataset-table td { padding: 11px 16px; border-bottom: 1px solid var(--border); color: var(--ink2); }
.dataset-table tr:last-child td { border: none; }
.dataset-table td:first-child {
    font-family: 'DM Mono', monospace; font-size: 11px; color: var(--teal);
}

/* ── METRICS ─────────────────────────────────────────────────── */
[data-testid="stMetric"] {
    background: var(--cream2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important; padding: 16px 18px !important;
}
[data-testid="stMetric"] label {
    font-family: 'DM Mono', monospace !important;
    font-size: 10px !important; text-transform: uppercase !important;
    letter-spacing: 0.12em !important; color: var(--ink3) !important;
}
[data-testid="stMetricValue"] {
    font-family: 'DM Mono', monospace !important;
    font-size: 22px !important; font-weight: 400 !important; color: var(--ink) !important;
}
[data-testid="stMetricDelta"] { display: none; }

/* ── BUTTONS ─────────────────────────────────────────────────── */
[data-testid="stButton"] > button, .stButton > button {
    background: var(--teal) !important; color: white !important;
    border: none !important; border-radius: 4px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 14px !important; font-weight: 600 !important;
    letter-spacing: 0.02em !important; padding: 12px 24px !important;
    transition: background 0.15s !important;
}
[data-testid="stButton"] > button:hover { background: var(--teal2) !important; border: none !important; }
[data-testid="stButton"]:first-of-type > button {
    background: transparent !important; color: var(--ink3) !important;
    border: 1px solid var(--border2) !important;
    font-size: 12px !important; letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
}
[data-testid="stButton"]:first-of-type > button:hover {
    background: var(--cream2) !important; color: var(--ink) !important;
}
[data-testid="stButton"]:first-of-type > button[kind="primary"] {
    background: var(--teal) !important; color: white !important;
    border: none !important; font-size: 14px !important;
    text-transform: none !important; letter-spacing: 0.02em !important;
}
[data-testid="stButton"]:first-of-type > button[kind="primary"]:hover {
    background: var(--teal2) !important;
}

/* ── SELECTBOX & INPUTS ──────────────────────────────────────── */
[data-testid="stSelectbox"] label,
[data-testid="stNumberInput"] label,
[data-testid="stTextInput"] label {
    font-family: 'DM Mono', monospace !important;
    font-size: 10px !important; text-transform: uppercase !important;
    letter-spacing: 0.12em !important; color: var(--ink3) !important; font-weight: 600 !important;
}
[data-baseweb="select"] > div,
[data-testid="stNumberInput"] input {
    border: 1px solid var(--border2) !important; border-radius: 6px !important;
    font-family: 'DM Sans', sans-serif !important;
    background: white !important; color: var(--ink) !important;
}
[data-baseweb="select"] > div:focus-within,
[data-testid="stNumberInput"] input:focus {
    border-color: var(--teal) !important;
    box-shadow: 0 0 0 2px rgba(13,110,104,0.12) !important;
}

/* ── TABS ────────────────────────────────────────────────────── */
[data-testid="stTabs"] [role="tablist"] {
    background: white !important; border-bottom: 1px solid var(--border) !important; gap: 0 !important;
}
[data-testid="stTabs"] [role="tab"] {
    font-family: 'DM Sans', sans-serif !important; font-size: 13px !important;
    font-weight: 500 !important; color: var(--ink3) !important;
    padding: 14px 20px !important; border-radius: 0 !important;
    border: none !important; border-bottom: 2px solid transparent !important; margin-bottom: -1px !important;
}
[data-testid="stTabs"] [role="tab"][aria-selected="true"] {
    color: var(--teal) !important; border-bottom-color: var(--teal) !important; background: transparent !important;
}
[data-testid="stTabs"] [role="tab"]:hover { color: var(--ink) !important; background: var(--cream2) !important; }

/* ── DATAFRAMES ──────────────────────────────────────────────── */
[data-testid="stDataFrame"] {
    border: 1px solid var(--border) !important; border-radius: 8px !important; overflow: hidden !important;
}
[data-testid="stDataFrame"] th {
    font-family: 'DM Mono', monospace !important; font-size: 10px !important;
    text-transform: uppercase !important; letter-spacing: 0.12em !important;
    background: var(--cream2) !important; color: var(--ink3) !important;
    border-bottom: 1px solid var(--border) !important;
}
[data-testid="stDataFrame"] td { font-size: 13px !important; color: var(--ink2) !important; }

/* ── ALERTS ──────────────────────────────────────────────────── */
[data-testid="stSuccess"] {
    background: var(--teal-light) !important; border-left: 3px solid var(--teal) !important;
    border-radius: 6px !important; font-size: 14px !important; color: var(--teal2) !important;
}
[data-testid="stInfo"] {
    background: #FEF9EC !important; border-left: 3px solid var(--amber) !important;
    border-radius: 6px !important; font-size: 13px !important; color: var(--ink2) !important;
}
[data-testid="stError"] {
    background: #FFF0EF !important; border-left: 3px solid var(--red) !important; border-radius: 6px !important;
}

/* ── EXPANDER ────────────────────────────────────────────────── */
[data-testid="stExpander"] {
    border: 1px solid var(--border) !important; border-radius: 8px !important; background: white !important;
}
[data-testid="stExpander"] summary {
    font-family: 'DM Mono', monospace !important; font-size: 11px !important;
    text-transform: uppercase !important; letter-spacing: 0.1em !important;
    color: var(--ink3) !important; font-weight: 600 !important;
}

hr { border: none !important; border-top: 1px solid var(--border) !important; margin: 28px 0 !important; }

/* ── FILE UPLOADER ───────────────────────────────────────────── */
[data-testid="stFileUploader"] {
    border: 1px dashed var(--border2) !important; border-radius: 8px !important; background: var(--cream2) !important;
}

/* ── DOWNLOAD BUTTON ─────────────────────────────────────────── */
[data-testid="stDownloadButton"] > button {
    background: transparent !important; color: var(--teal) !important;
    border: 1px solid var(--teal) !important; font-weight: 600 !important;
}
[data-testid="stDownloadButton"] > button:hover { background: var(--teal-light) !important; }

/* ── RADIO ALGO CARDS ────────────────────────────────────────── */
div[data-testid="stRadio"] > div[role="radiogroup"],
div[data-testid="stRadio"] > div > div[role="radiogroup"] {
    gap: 8px !important; flex-direction: column !important;
}
div[data-testid="stRadio"] [data-baseweb="radio"] {
    background: white !important; border: 1px solid var(--border) !important;
    border-radius: 8px !important; padding: 14px 16px !important;
    cursor: pointer !important; transition: background 0.15s, border-color 0.15s !important;
    width: 100% !important; box-sizing: border-box !important; align-items: center !important;
}
div[data-testid="stRadio"] [data-baseweb="radio"]:hover { border-color: var(--teal) !important; }
div[data-testid="stRadio"] [data-baseweb="radio"]:has(input:checked) {
    background: var(--teal) !important; border-color: var(--teal) !important;
}
div[data-testid="stRadio"] [data-baseweb="radio"] > div:first-child { display: none !important; }
div[data-testid="stRadio"] [data-baseweb="radio"] > div:last-child {
    margin-left: 0 !important; font-size: 14px !important;
    font-weight: 500 !important; line-height: 1.4 !important; color: var(--ink) !important;
}
div[data-testid="stRadio"] [data-baseweb="radio"]:has(input:checked) [data-testid="stMarkdownContainer"] * {
    color: white !important;
}

/* ── ALGO METRICS GRID ───────────────────────────────────────── */
.algo-metrics-grid {
    display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 16px;
}
.algo-metric {
    background: var(--cream2); border: 1px solid var(--border);
    border-radius: 8px; padding: 14px 16px;
}
.algo-metric-label {
    font-family: 'DM Mono', monospace; font-size: 9px;
    text-transform: uppercase; letter-spacing: 0.12em; color: var(--ink3); margin-bottom: 6px;
}
.algo-metric-value {
    font-family: 'DM Mono', monospace; font-size: 20px; font-weight: 500; color: var(--ink);
}

/* ── FORMAT CARD ─────────────────────────────────────────────── */
.format-card {
    background: #FEF9EC; border: 1px solid rgba(194,113,12,0.25);
    border-left: 3px solid var(--amber); border-radius: 8px; padding: 16px 20px; margin-bottom: 16px;
}
.format-card-title {
    font-family: 'DM Mono', monospace; font-size: 10px;
    text-transform: uppercase; letter-spacing: 0.15em;
    color: var(--amber); margin-bottom: 12px; font-weight: 600;
}
.format-row { font-size: 13px; color: var(--ink2); margin-bottom: 8px; line-height: 1.6; }
.format-tag {
    font-family: 'DM Mono', monospace; font-size: 10px; font-weight: 600;
    background: var(--amber); color: white; padding: 2px 8px; border-radius: 3px;
    margin-right: 8px; text-transform: uppercase; letter-spacing: 0.08em;
}
.format-note { font-size: 12px; color: var(--ink3); margin-top: 10px; font-style: italic; }
.format-card code {
    font-family: 'DM Mono', monospace; font-size: 11px;
    background: rgba(0,0,0,0.06); padding: 1px 5px; border-radius: 3px; color: var(--ink2);
}

/* ── SUMMARY CARDS ───────────────────────────────────────────── */
.summary-card {
    background: white; border: 1px solid var(--border); border-radius: 8px;
    padding: 14px 16px; margin-bottom: 8px; display: flex; flex-direction: column; gap: 4px;
}
.summary-card--best { background: var(--teal); border-color: var(--teal); }
.summary-card-header { display: flex; align-items: center; gap: 8px; }
.summary-card-name { font-size: 14px; font-weight: 500; color: var(--ink); }
.summary-card--best .summary-card-name { color: white; }
.summary-badge {
    font-family: 'DM Mono', monospace; font-size: 9px; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.12em;
    background: rgba(255,255,255,0.2); color: white; padding: 2px 8px; border-radius: 3px;
}
.summary-card-r2 { font-family: 'DM Mono', monospace; font-size: 12px; color: var(--ink3); }
.summary-card--best .summary-card-r2 { color: rgba(255,255,255,0.7); }

/* ── CONCLUSION CARD ─────────────────────────────────────────── */
.conclusion-card {
    background: var(--teal-light); border: 1px solid rgba(13,110,104,0.2);
    border-left: 3px solid var(--teal); border-radius: 8px; padding: 16px; margin-top: 8px;
}
.conclusion-label {
    font-family: 'DM Mono', monospace; font-size: 9px; text-transform: uppercase;
    letter-spacing: 0.15em; color: var(--teal); font-weight: 600; margin-bottom: 8px;
}
.conclusion-card p { font-size: 13px; color: var(--ink2); line-height: 1.6; margin: 0; }

/* ── ANALYSIS CARDS ──────────────────────────────────────────── */
.analysis-card {
    background: white; border: 1px solid var(--border); border-radius: 8px;
    padding: 16px 18px; margin-bottom: 10px;
}
.analysis-card--best { border-color: var(--teal); border-left: 3px solid var(--teal); }
.analysis-card-title { font-size: 13px; font-weight: 600; color: var(--ink); margin-bottom: 8px; }
.analysis-card--best .analysis-card-title { color: var(--teal); }
.analysis-card ul { margin: 0; padding-left: 16px; }
.analysis-card li { font-size: 12px; color: var(--ink2); line-height: 1.7; }

/* ── FEATURE IMPORTANCE ──────────────────────────────────────── */
.fi-row {
    display: flex; align-items: center; gap: 12px;
    padding: 9px 0; border-bottom: 1px solid var(--border);
}
.fi-row:last-child { border: none; }
.fi-name { font-family: 'DM Mono', monospace; font-size: 11px; color: var(--ink2); width: 230px; flex-shrink: 0; }
.fi-bar-wrap { flex: 1; background: var(--cream3); border-radius: 2px; height: 7px; overflow: hidden; }
.fi-bar { height: 100%; background: var(--teal); border-radius: 2px; }
.fi-pct { font-family: 'DM Mono', monospace; font-size: 12px; font-weight: 600; color: var(--ink2); min-width: 42px; text-align: right; }

/* ── RESULT CARD ─────────────────────────────────────────────── */
.result-display {
    background: var(--ink); color: white; border-radius: 8px;
    padding: 28px 32px; display: flex; align-items: center; gap: 32px; margin-top: 8px;
}
.price-label {
    font-family: 'DM Mono', monospace; font-size: 10px;
    text-transform: uppercase; letter-spacing: 0.15em; color: rgba(255,255,255,.4); margin-bottom: 6px;
}
.price-inr { font-family: 'Playfair Display', serif; font-size: 44px; font-weight: 700; line-height: 1; }
.price-eur { font-family: 'Playfair Display', serif; font-size: 26px; font-weight: 600; color: var(--teal-glow); }
.result-divider { width: 1px; height: 60px; background: rgba(255,255,255,.12); }
.model-badge {
    margin-left: auto; background: var(--teal); color: white;
    font-size: 10px; font-weight: 700; text-transform: uppercase;
    letter-spacing: 0.12em; padding: 6px 16px; border-radius: 3px;
}
</style>
"""

NAVBAR_HTML = """
<div class="app-navbar">
    <div class="nav-logo">
        <svg viewBox="0 0 24 24"><path d="M18.92 6.01C18.72 5.42 18.16 5 17.5 5h-11c-.66 0-1.21.42-1.42 1.01L3 12v8c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-1h12v1c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-8l-2.08-5.99zM6.5 16c-.83 0-1.5-.67-1.5-1.5S5.67 13 6.5 13s1.5.67 1.5 1.5S7.33 16 6.5 16zm11 0c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zM5 11l1.5-4.5h11L19 11H5z"/></svg>
    </div>
    <div>
        <p class="nav-title">Prédiction du Prix des Voitures d'Occasion</p>
        <p class="nav-sub">Car Dekho &nbsp;·&nbsp; Projet Python</p>
    </div>
    <span class="nav-badge">ML · 4 Modèles</span>
</div>
"""

FOOTER_HTML = """
<div class="app-footer">
    <div><strong>Étudiant :</strong> Meimoune Baba Cheikh Sidiya &nbsp;·&nbsp; <strong>Matricule :</strong> C34620</div>
    <div class="footer-id">CarDekho &nbsp;·&nbsp; Projet Python &nbsp;·&nbsp; 2024</div>
</div>
"""

# Hero avec bouton CTA intégré qui déclenche la navigation via JS
HERO_HTML = """
<div class="hero-banner">
    <div class="hero-label">Analyse par Machine Learning</div>
    <h1 class="hero-h1">Estimez le prix d'une voiture<br><em>d'occasion</em> en quelques secondes</h1>
    <p class="hero-sub">
        Entraîné sur <strong style="color:rgba(255,255,255,.85)">8 128 annonces réelles</strong>
        de la plateforme CarDekho &mdash; quatre algorithmes comparés pour une estimation fiable.
    </p>
    <button class="hero-cta-btn" onclick="
        const url = new URL(window.location.href);
        url.searchParams.set('go', 'app');
        window.location.href = url.toString();
    ">
        Commencer la prédiction
        <svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg>
    </button>
    <div class="hero-stats">
        <div class="hero-stat">
            <div class="hero-stat-num">8 128</div>
            <div class="hero-stat-label">Véhicules</div>
        </div>
        <div class="hero-stat">
            <div class="hero-stat-num">4</div>
            <div class="hero-stat-label">Algorithmes</div>
        </div>
        <div class="hero-stat">
            <div class="hero-stat-num">0,75</div>
            <div class="hero-stat-label">R² XGBoost</div>
        </div>
        <div class="hero-stat">
            <div class="hero-stat-num">~12</div>
            <div class="hero-stat-label">Variables</div>
        </div>
    </div>
</div>
<div class="features-strip">
    <div class="feature-item">
        <div class="feature-dot"></div>
        <span class="feature-text">XGBoost &nbsp;·&nbsp; Random Forest &nbsp;·&nbsp; SVR &nbsp;·&nbsp; Régression Linéaire</span>
    </div>
    <div class="feature-item">
        <div class="feature-dot"></div>
        <span class="feature-text">Prédiction individuelle &amp; en masse (CSV)</span>
    </div>
</div>
"""

DATASET_TABLE_HTML = """
<table class="dataset-table">
    <thead><tr><th>Variable</th><th>Description</th></tr></thead>
    <tbody>
        <tr><td>car_age</td><td>Ancienneté du véhicule</td></tr>
        <tr><td>km_driven</td><td>Kilométrage total</td></tr>
        <tr><td>fuel</td><td>Type de carburant</td></tr>
        <tr><td>transmission</td><td>Manuelle / Automatique</td></tr>
        <tr><td>seller_type</td><td>Particulier / Concessionnaire</td></tr>
        <tr><td>owner</td><td>Nombre de propriétaires</td></tr>
        <tr><td>brand</td><td>Marque du véhicule</td></tr>
    </tbody>
</table>
"""


def _fmt_indian(n: int) -> str:
    s = str(abs(int(n)))
    if len(s) <= 3:
        return s
    result = s[-3:]
    s = s[:-3]
    while s:
        chunk = s[-2:] if len(s) > 2 else s
        result = chunk + ',' + result
        s = s[:-2] if len(s) > 2 else ''
    return result


def result_card_html(price_inr: float, model_name: str, car_label: str = "") -> str:
    price_eur = price_inr / 90
    inr_str = _fmt_indian(int(price_inr))
    eur_str = f"{price_eur:,.0f}".replace(",", "\u202f")
    return f"""
<div class="result-display">
    <div>
        <div class="price-label">Prix estimé</div>
        <div class="price-inr">&#8377; {inr_str}</div>
        <div style="font-size:12px;color:rgba(255,255,255,.35);margin-top:5px">{car_label}</div>
    </div>
    <div class="result-divider"></div>
    <div>
        <div class="price-label">Équivalent</div>
        <div class="price-eur">&#8776; {eur_str} &euro;</div>
    </div>
    <div class="model-badge">{model_name}</div>
</div>
"""
