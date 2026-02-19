import streamlit as st

# ── CSS STYLING ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Jost:wght@300;400;500;600&display=swap');

/* ── RESET & BASE ── */
section[data-testid="stMain"] { background: #FBF2DC; }
.block-container { padding: 2rem 3rem 4rem 3rem !important; max-width: 900px !important; margin: 0 auto; }

/* ── HERO HEADER ── */
.calc-hero {
    text-align: center;
    padding: 3rem 2rem 2rem 2rem;
    margin-bottom: 2.5rem;
    position: relative;
}
.calc-hero::before {
    content: '◆';
    display: block;
    color: #C8A96E;
    font-size: 14px;
    letter-spacing: 8px;
    margin-bottom: 1rem;
}
.calc-hero h1 {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 3.2rem !important;
    font-weight: 300 !important;
    color: #3D2008 !important;
    letter-spacing: 0.05em;
    margin: 0 0 0.5rem 0 !important;
    line-height: 1.1;
}
.calc-hero h1 em {
    font-style: italic;
    color: #6C4118;
}
.calc-hero p {
    font-family: 'Jost', sans-serif;
    font-size: 0.85rem;
    font-weight: 300;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #9E7A52;
    margin: 0.5rem 0 0 0;
}
.divider-ornament {
    text-align: center;
    margin: 0.5rem 0 2rem 0;
    color: #C8A96E;
    font-size: 11px;
    letter-spacing: 12px;
}

/* ── SECTION CARD ── */
.section-card {
    background: #FFFDF5;
    border: 1px solid #E8D9C0;
    border-radius: 4px;
    padding: 1.8rem 2rem;
    margin-bottom: 1.2rem;
    position: relative;
    transition: box-shadow 0.3s ease;
}
.section-card:hover { box-shadow: 0 4px 24px rgba(108,65,24,0.08); }
.section-label {
    font-family: 'Jost', sans-serif;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #9E7A52;
    margin-bottom: 0.4rem;
}
.section-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.5rem;
    font-weight: 400;
    color: #3D2008;
    margin-bottom: 0.2rem;
}
.section-icon {
    position: absolute;
    top: 1.8rem;
    right: 2rem;
    font-size: 1.4rem;
    opacity: 0.35;
}

/* ── STREAMLIT WIDGET OVERRIDES ── */
div[data-testid="stSelectbox"] label,
div[data-testid="stNumberInput"] label {
    font-family: 'Jost', sans-serif !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    color: #9E7A52 !important;
}
div[data-testid="stSelectbox"] > div > div,
div[data-testid="stNumberInput"] input {
    background: #FBF2DC !important;
    border: 1px solid #D4B896 !important;
    border-radius: 3px !important;
    color: #3D2008 !important;
    font-family: 'Jost', sans-serif !important;
    font-size: 0.9rem !important;
}
div[data-testid="stSelectbox"] > div > div:focus-within,
div[data-testid="stNumberInput"] input:focus {
    border-color: #6C4118 !important;
    box-shadow: 0 0 0 2px rgba(108,65,24,0.12) !important;
}

/* ── CATERING SPLIT ── */
.catering-split {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-top: 1rem;
}
.catering-side {
    background: #F5ECD8;
    border-radius: 4px;
    padding: 1.2rem 1.4rem;
    border: 1px solid #E0CCA8;
}
.catering-side-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.1rem;
    color: #6C4118;
    margin-bottom: 0.2rem;
}
.catering-side-sub {
    font-family: 'Jost', sans-serif;
    font-size: 0.72rem;
    color: #9E7A52;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 0.8rem;
}
.catering-calc-row {
    font-family: 'Jost', sans-serif;
    font-size: 0.82rem;
    color: #6C4118;
    padding: 0.25rem 0;
    border-bottom: 1px dashed #D4B896;
    margin-bottom: 0.25rem;
}
.catering-calc-row span {
    float: right;
    font-weight: 500;
}
.catering-subtotal {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.15rem;
    color: #3D2008;
    margin-top: 0.6rem;
    font-weight: 600;
}
.catering-subtotal span { float: right; }

/* ── BREAKDOWN TABLE ── */
.breakdown-wrapper {
    background: #FFFDF5;
    border: 1px solid #E8D9C0;
    border-radius: 4px;
    padding: 1.8rem 2rem;
    margin: 1.5rem 0;
}
.breakdown-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.3rem;
    color: #3D2008;
    margin-bottom: 1.2rem;
    padding-bottom: 0.8rem;
    border-bottom: 1px solid #E8D9C0;
}
.breakdown-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.55rem 0;
    border-bottom: 1px dashed #E8D9C0;
    font-family: 'Jost', sans-serif;
    font-size: 0.88rem;
}
.breakdown-row:last-child { border-bottom: none; }
.breakdown-label { color: #6C4118; font-weight: 400; }
.breakdown-value { color: #3D2008; font-weight: 500; }

/* ── TOTAL BOX ── */
.total-box {
    background: linear-gradient(135deg, #6C4118 0%, #3D2008 100%);
    border-radius: 6px;
    padding: 3rem 2.5rem;
    text-align: center;
    margin: 1rem 0 2rem 0;
    position: relative;
    overflow: hidden;
}
.total-box::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23C8A96E' fill-opacity='0.06'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}
.total-ornament {
    color: #C8A96E;
    font-size: 11px;
    letter-spacing: 10px;
    margin-bottom: 1rem;
    position: relative;
}
.total-label {
    font-family: 'Jost', sans-serif;
    font-size: 0.75rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: #C8A96E;
    margin-bottom: 1rem;
    position: relative;
}
.total-amount {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3.8rem;
    font-weight: 300;
    color: #FBF2DC;
    letter-spacing: -0.01em;
    line-height: 1;
    position: relative;
    margin-bottom: 0.5rem;
}
.total-note {
    font-family: 'Jost', sans-serif;
    font-size: 0.72rem;
    color: #C8A96E;
    letter-spacing: 0.15em;
    margin-top: 1.2rem;
    position: relative;
    opacity: 0.8;
}

/* ── PAX INFO CHIP ── */
.pax-chip {
    display: inline-block;
    background: #F0E4CC;
    border: 1px solid #D4B896;
    border-radius: 20px;
    padding: 0.3rem 1rem;
    font-family: 'Jost', sans-serif;
    font-size: 0.78rem;
    color: #6C4118;
    letter-spacing: 0.05em;
    margin-top: 0.5rem;
}

/* ── HELPER INFO ── */
.info-note {
    font-family: 'Jost', sans-serif;
    font-size: 0.75rem;
    color: #9E7A52;
    font-style: italic;
    margin-top: 0.4rem;
}

/* hide streamlit branding */
#MainMenu, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── HELPERS ──────────────────────────────────────────────────────────────────
def fmt_idr(amount):
    return "Rp {:,.0f}".format(amount).replace(",", ".")

def parse_tier(label):
    """Extract price from tier label string like 'Tier 1 – Rp 10.000.000'"""
    import re
    nums = re.findall(r'[\d\.]+', label.replace(".", ""))
    for n in reversed(nums):
        try:
            v = int(n)
            if v > 100:
                return v
        except:
            pass
    return 0

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="calc-hero">
    <h1>Wedding <em>Calculator</em></h1>
    <p>Estimasi Biaya Pernikahan Impian Anda</p>
</div>
<div class="divider-ornament">◆ ◇ ◆</div>
""", unsafe_allow_html=True)

# ── STATE INIT ───────────────────────────────────────────────────────────────
costs = {}

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 1 — TOTAL UNDANGAN
# ═══════════════════════════════════════════════════════════════════════════
st.markdown('<div class="section-card"><span class="section-icon">💌</span>', unsafe_allow_html=True)
st.markdown('<div class="section-label">01 — Tamu Undangan</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Total Undangan</div>', unsafe_allow_html=True)

undangan_opts = [200, 300, 400, 500]
undangan = st.selectbox("Jumlah Tamu", undangan_opts, format_func=lambda x: f"{x} Undangan", label_visibility="collapsed")
total_pax = undangan * 2
st.markdown(f'<div class="pax-chip">👥 Total Pax Catering: {total_pax} pax ({undangan} undangan × 2)</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 2 — WEDDING ORGANIZER
# ═══════════════════════════════════════════════════════════════════════════
st.markdown('<div class="section-card"><span class="section-icon">💼</span>', unsafe_allow_html=True)
st.markdown('<div class="section-label">02 — Pengelola Acara</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Wedding Organizer</div>', unsafe_allow_html=True)

wo_options = {
    "SamIRanA – Wedding Day Organizer": 3_499_000,
    "AruNikA – Full Wedding Organizer": 6_499_000,
    "CandRaMayA – Intimate Wedding Organizer": 4_499_000,
    "Lainnya (isi manual)": None,
}
wo_sel = st.selectbox("Pilih Paket WO", list(wo_options.keys()), label_visibility="collapsed")
if wo_options[wo_sel] is None:
    wo_manual = st.number_input("Masukkan nominal (Rp)", min_value=0, step=100_000, key="wo_manual", label_visibility="visible")
    costs["Wedding Organizer"] = wo_manual
else:
    costs["Wedding Organizer"] = wo_options[wo_sel]
    st.markdown(f'<div class="info-note">✦ {fmt_idr(costs["Wedding Organizer"])}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# GENERIC TIER BUILDER
# ═══════════════════════════════════════════════════════════════════════════
def tier_section(num, icon, label_id, title, tiers: dict):
    st.markdown(f'<div class="section-card"><span class="section-icon">{icon}</span>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-label">{num} — {label_id}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)

    opts = list(tiers.keys()) + ["Lainnya (isi manual)"]
    sel = st.selectbox(f"Pilih {title}", opts, label_visibility="collapsed", key=f"sel_{num}")

    if sel == "Lainnya (isi manual)":
        val = st.number_input("Masukkan nominal (Rp)", min_value=0, step=100_000, key=f"manual_{num}", label_visibility="visible")
    else:
        val = tiers[sel]
        st.markdown(f'<div class="info-note">✦ {fmt_idr(val)}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    return val

# Venue
costs["Venue"] = tier_section(
    "03", "🏛️", "Tempat Resepsi", "Venue",
    {
        "Tier 1 — Ballroom Mewah": 10_000_000,
        "Tier 2 — Gedung Standar": 7_500_000,
        "Tier 3 — Outdoor / Rumah": 5_000_000,
    }
)

# Decoration
costs["Dekorasi"] = tier_section(
    "04", "🌸", "Tata Ruang & Estetika", "Decoration",
    {
        "Tier 1 — Full Custom Premium": 20_000_000,
        "Tier 2 — Paket Semi Custom": 15_000_000,
        "Tier 3 — Paket Standar": 10_000_000,
    }
)

# MUA
costs["Make Up Artist"] = tier_section(
    "05", "💄", "Penampilan Pengantin", "Make Up Artist",
    {
        "Tier 1 — MUA Senior / Award": 9_000_000,
        "Tier 2 — MUA Profesional": 7_000_000,
        "Tier 3 — MUA Lokal Terbaik": 5_000_000,
    }
)

# Wedding Attire
costs["Wedding Attire"] = tier_section(
    "06", "👗", "Busana Pengantin", "Wedding Attire",
    {
        "Tier 1 — Busana Premium / Desainer": 9_000_000,
        "Tier 2 — Busana Sewa Kualitas A": 7_000_000,
        "Tier 3 — Busana Sewa Standar": 5_000_000,
    }
)

# Documentation
costs["Dokumentasi"] = tier_section(
    "07", "📸", "Foto & Video", "Documentation",
    {
        "Tier 1 — Sinematik Full Team": 9_500_000,
        "Tier 2 — Foto & Video Profesional": 7_500_000,
        "Tier 3 — Paket Foto Standar": 6_000_000,
    }
)

# Entertainment
costs["Entertainment"] = tier_section(
    "08", "🎵", "Hiburan & Musik", "Entertainment",
    {
        "Tier 1 — Band / Artis Undangan": 10_000_000,
        "Tier 2 — Live Music Profesional": 7_500_000,
        "Tier 3 — Keyboard / Organ Tunggal": 5_000_000,
    }
)

# MC
costs["Master of Ceremony"] = tier_section(
    "09", "🎤", "Pemandu Acara", "Master of Ceremony",
    {
        "Tier 1 — MC Nasional / Selebritis": 5_000_000,
        "Tier 2 — MC Profesional Daerah": 4_000_000,
        "Tier 3 — MC Lokal Berpengalaman": 3_500_000,
    }
)

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 10 — WEDDING CATERING (SPECIAL)
# ═══════════════════════════════════════════════════════════════════════════
st.markdown('<div class="section-card"><span class="section-icon">🍽️</span>', unsafe_allow_html=True)
st.markdown('<div class="section-label">10 — Sajian Pernikahan</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Wedding Catering</div>', unsafe_allow_html=True)

catering_tiers = {
    "Tier 1 — Premium (Rp 75.000/pax)": 75_000,
    "Tier 2 — Standar (Rp 60.000/pax)": 60_000,
    "Tier 3 — Ekonomis (Rp 45.000/pax)": 45_000,
    "Lainnya (isi manual per pax)": None,
}

cat_sel = st.selectbox("Pilih Tier Catering", list(catering_tiers.keys()), label_visibility="collapsed", key="catering_tier")

if catering_tiers[cat_sel] is None:
    harga_pax = st.number_input("Harga per pax (Rp)", min_value=0, step=1_000, key="cat_manual", label_visibility="visible")
else:
    harga_pax = catering_tiers[cat_sel]

# Buffet % selector
buffet_pct_opts = {"80% Buffet / 20% Stall": 0.80, "70% Buffet / 30% Stall": 0.70, "60% Buffet / 40% Stall": 0.60}
buffet_sel = st.selectbox("Komposisi Penyajian", list(buffet_pct_opts.keys()), label_visibility="visible", key="buffet_pct")
buffet_pct = buffet_pct_opts[buffet_sel]
stall_pct  = 1 - buffet_pct

# Calculations
pax_buffet    = total_pax * buffet_pct
pax_stall_per = total_pax * stall_pct
pax_stall_tot = pax_stall_per * 3   # 3 macam stall

cost_buffet = pax_buffet * harga_pax
cost_stall  = pax_stall_tot * harga_pax
total_catering = cost_buffet + cost_stall

costs["Catering"] = total_catering

# Visual split display
st.markdown(f"""
<div class="catering-split">
  <div class="catering-side">
    <div class="catering-side-title">🍱 Buffet</div>
    <div class="catering-side-sub">Hidangan Prasmanan</div>
    <div class="catering-calc-row">Total Pax <span>{total_pax} pax</span></div>
    <div class="catering-calc-row">Porsi Buffet <span>{int(buffet_pct*100)}%</span></div>
    <div class="catering-calc-row">Pax Buffet <span>{int(pax_buffet)} pax</span></div>
    <div class="catering-calc-row">Harga/pax <span>{fmt_idr(harga_pax)}</span></div>
    <div class="catering-subtotal">Subtotal <span>{fmt_idr(cost_buffet)}</span></div>
  </div>
  <div class="catering-side">
    <div class="catering-side-title">🥘 Stall × 3</div>
    <div class="catering-side-sub">3 Macam Booth Makanan</div>
    <div class="catering-calc-row">Total Pax <span>{total_pax} pax</span></div>
    <div class="catering-calc-row">Porsi Stall <span>{int(stall_pct*100)}%</span></div>
    <div class="catering-calc-row">Pax/Stall <span>{int(pax_stall_per)} pax</span></div>
    <div class="catering-calc-row">× 3 Stall <span>{int(pax_stall_tot)} pax</span></div>
    <div class="catering-calc-row">Harga/pax <span>{fmt_idr(harga_pax)}</span></div>
    <div class="catering-subtotal">Subtotal <span>{fmt_idr(cost_stall)}</span></div>
  </div>
</div>
<div style="text-align:right; margin-top:1rem; font-family:'Jost',sans-serif; font-size:0.82rem; color:#6C4118;">
    Total Catering &nbsp;→&nbsp; <strong style="font-size:1rem;">{fmt_idr(total_catering)}</strong>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# BREAKDOWN SUMMARY
# ═══════════════════════════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="divider-ornament">◆ ◇ ◆</div>
""", unsafe_allow_html=True)

grand_total = sum(costs.values())

# Breakdown table
breakdown_rows = ""
for label, val in costs.items():
    breakdown_rows += f"""
    <div class="breakdown-row">
        <span class="breakdown-label">{label}</span>
        <span class="breakdown-value">{fmt_idr(val)}</span>
    </div>
    """

st.markdown(f"""
<div class="breakdown-wrapper">
    <div class="breakdown-title">✦ Rincian Estimasi Biaya</div>
    {breakdown_rows}
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# GRAND TOTAL
# ═══════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="total-box">
    <div class="total-ornament">◆ ◇ ◆</div>
    <div class="total-label">Estimasi Total Biaya Pernikahan</div>
    <div class="total-amount">{fmt_idr(grand_total)}</div>
    <div class="total-note">* Estimasi dapat berubah sesuai negosiasi & kondisi vendor &nbsp;|&nbsp; Konsultasikan dengan tim Kidung Sore</div>
</div>
""", unsafe_allow_html=True)

# CTA
st.markdown("""
<div style="text-align:center; padding: 1rem 0 2rem 0;">
    <p style="font-family:'Jost',sans-serif; font-size:0.8rem; color:#9E7A52; letter-spacing:0.15em; text-transform:uppercase;">
        💍 Hubungi kami untuk konsultasi & penawaran terbaik
    </p>
</div>
""", unsafe_allow_html=True)
