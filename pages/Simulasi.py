import streamlit as st

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Jost:wght@300;400;500;600&display=swap');

/* BASE */
section[data-testid="stMain"]        { background: #FFFFFF !important; }
.block-container                      { padding: 2rem 3rem 4rem 3rem !important; max-width: 860px !important; margin: 0 auto; }

/* HERO */
.calc-hero { text-align: center; padding: 2.5rem 1rem 1.5rem 1rem; margin-bottom: 1.5rem; }
.calc-hero h1 {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 3rem !important; font-weight: 300 !important;
    color: #3D2008 !important; letter-spacing: 0.04em;
    margin: 0 0 0.4rem 0 !important; line-height: 1.1;
}
.calc-hero h1 em { font-style: italic; color: #6C4118; }
.calc-hero p {
    font-family: 'Jost', sans-serif; font-size: 0.82rem; font-weight: 300;
    letter-spacing: 0.28em; text-transform: uppercase; color: #9E7A52; margin: 0;
}
.divider-orn {
    text-align: center; color: #C8A96E; font-size: 11px;
    letter-spacing: 10px; margin: 0.5rem 0 1.8rem 0;
}

/* CARD */
.s-card {
    background: #FAFAFA;
    border: 1px solid #E8D9C0;
    border-left: 3px solid #6C4118;
    border-radius: 6px;
    padding: 1.4rem 1.6rem 1.2rem 1.6rem;
    margin-bottom: 1rem;
}
.s-num  { font-family:'Jost',sans-serif; font-size:0.68rem; font-weight:600; letter-spacing:0.22em; text-transform:uppercase; color:#9E7A52; margin-bottom:0.2rem; }
.s-title{ font-family:'Cormorant Garamond',serif; font-size:1.45rem; font-weight:400; color:#3D2008; margin-bottom:0.8rem; }
.info-note { font-family:'Jost',sans-serif; font-size:0.76rem; color:#9E7A52; font-style:italic; margin-top:0.3rem; }
.pax-chip {
    display:inline-block; background:#F5ECD8; border:1px solid #D4B896;
    border-radius:20px; padding:0.28rem 1rem;
    font-family:'Jost',sans-serif; font-size:0.77rem; color:#6C4118; margin-top:0.5rem;
}

/* CATERING SPLIT */
.cat-box {
    background:#F5ECD8; border:1px solid #E0CCA8; border-radius:6px;
    padding:1rem 1.2rem; height:100%;
}
.cat-box-title { font-family:'Cormorant Garamond',serif; font-size:1.1rem; color:#6C4118; margin-bottom:0.15rem; }
.cat-box-sub   { font-family:'Jost',sans-serif; font-size:0.7rem; color:#9E7A52; letter-spacing:0.12em; text-transform:uppercase; margin-bottom:0.7rem; }
.cat-row       { font-family:'Jost',sans-serif; font-size:0.82rem; color:#6C4118; display:flex; justify-content:space-between; padding:0.22rem 0; border-bottom:1px dashed #D4B896; }
.cat-total     { font-family:'Cormorant Garamond',serif; font-size:1.1rem; color:#3D2008; font-weight:600; display:flex; justify-content:space-between; margin-top:0.5rem; }
.cat-grand     { font-family:'Jost',sans-serif; font-size:0.85rem; color:#6C4118; text-align:right; margin-top:0.8rem; }

/* TOTAL */
.total-box {
    background: linear-gradient(135deg, #6C4118 0%, #3D2008 100%);
    border-radius:8px; padding:2.8rem 2rem; text-align:center; margin:0.5rem 0 2rem 0;
}
.total-label  { font-family:'Jost',sans-serif; font-size:0.72rem; letter-spacing:0.28em; text-transform:uppercase; color:#C8A96E; margin-bottom:0.9rem; }
.total-amount { font-family:'Cormorant Garamond',serif; font-size:3.6rem; font-weight:300; color:#FBF2DC; line-height:1; margin-bottom:0.4rem; }
.total-note   { font-family:'Jost',sans-serif; font-size:0.7rem; color:#C8A96E; letter-spacing:0.12em; margin-top:1rem; opacity:0.8; }

/* WIDGET LABELS */
div[data-testid="stSelectbox"] label,
div[data-testid="stNumberInput"] label {
    font-family:'Jost',sans-serif !important; font-size:0.76rem !important;
    font-weight:500 !important; letter-spacing:0.1em !important;
    text-transform:uppercase !important; color:#9E7A52 !important;
}
div[data-testid="stSelectbox"] > div > div {
    background:#FFFFFF !important; border:1px solid #D4B896 !important;
    border-radius:4px !important; color:#3D2008 !important;
    font-family:'Jost',sans-serif !important; font-size:0.88rem !important;
}
div[data-testid="stNumberInput"] input {
    background:#FFFFFF !important; border:1px solid #D4B896 !important;
    border-radius:4px !important; color:#3D2008 !important;
    font-family:'Jost',sans-serif !important;
}

#MainMenu, footer { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

# ── HELPERS ──────────────────────────────────────────────────────────────────
def idr(n):
    return "Rp {:,.0f}".format(n).replace(",", ".")

costs = {}

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="calc-hero">
    <h1>Wedding <em>Calculator</em></h1>
</div>
<div class="divider-orn">◆ ◇ ◆</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# 01 — TOTAL UNDANGAN
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="s-card">', unsafe_allow_html=True)
st.markdown('<div class="s-num">01 — Tamu Undangan</div><div class="s-title">Total Undangan</div>', unsafe_allow_html=True)

undangan  = st.selectbox("Jumlah Undangan", [200, 300, 400, 500],
                          format_func=lambda x: f"{x} Undangan",
                          label_visibility="collapsed", key="undangan")
total_pax = undangan * 2
st.markdown(f'<div class="pax-chip">Total Pax Catering : {total_pax} pax &nbsp;({undangan} undangan x 2)</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# HELPER: TIER SECTION
# ═══════════════════════════════════════════════════════════════════════════════
def tier_section(num, sublabel, title, tiers: dict, ks: str):
    st.markdown(f'<div class="s-card"><div class="s-num">{num} — {sublabel}</div><div class="s-title">{title}</div>', unsafe_allow_html=True)
    opts = list(tiers.keys()) + ["Lainnya (isi manual)"]
    sel  = st.selectbox(f"Pilih {title}", opts, label_visibility="collapsed", key=f"sel_{ks}")
    if sel == "Lainnya (isi manual)":
        val = st.number_input("Masukkan nominal (Rp)", min_value=0, step=100_000, key=f"man_{ks}")
    else:
        val = tiers[sel]
        st.markdown(f'<div class="info-note">✦ {idr(val)}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    return val

# ═══════════════════════════════════════════════════════════════════════════════
# 02 — WEDDING ORGANIZER
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="s-card"><div class="s-num">02 — Pengelola Acara</div><div class="s-title">Wedding Organizer</div>', unsafe_allow_html=True)
wo_opts = {
    "SamIRanA — Wedding Day Organizer":        3_499_000,
    "AruNikA — Full Wedding Organizer":         6_499_000,
    "CandRaMayA — Intimate Wedding Organizer":  4_499_000,
    "Lainnya (isi manual)": None,
}
wo_sel = st.selectbox("Pilih WO", list(wo_opts.keys()), label_visibility="collapsed", key="wo")
if wo_opts[wo_sel] is None:
    wo_val = st.number_input("Masukkan nominal (Rp)", min_value=0, step=100_000, key="wo_man")
else:
    wo_val = wo_opts[wo_sel]
    st.markdown(f'<div class="info-note">✦ {idr(wo_val)}</div>', unsafe_allow_html=True)
costs["Wedding Organizer"] = wo_val
st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# 03 – 09
# ═══════════════════════════════════════════════════════════════════════════════
costs["Venue"] = tier_section("03", "Tempat Resepsi", "Venue", {
    "Tier 1 — Ballroom Mewah":   10_000_000,
    "Tier 2 — Gedung Standar":    7_500_000,
    "Tier 3 — Outdoor / Rumah":   5_000_000,
}, "venue")

costs["Decoration"] = tier_section("04", "Tata Ruang & Estetika", "Decoration", {
    "Tier 1 — Full Custom Premium": 20_000_000,
    "Tier 2 — Paket Semi Custom":   15_000_000,
    "Tier 3 — Paket Standar":       10_000_000,
}, "deco")

costs["Make Up Artist"] = tier_section("05", "Penampilan Pengantin", "Make Up Artist", {
    "Tier 1 — MUA Senior / Award": 9_000_000,
    "Tier 2 — MUA Profesional":    7_000_000,
    "Tier 3 — MUA Lokal Terbaik":  5_000_000,
}, "mua")

costs["Wedding Attire"] = tier_section("06", "Busana Pengantin", "Wedding Attire", {
    "Tier 1 — Busana Premium / Desainer": 9_000_000,
    "Tier 2 — Sewa Kualitas A":           7_000_000,
    "Tier 3 — Sewa Standar":              5_000_000,
}, "attire")

costs["Documentation"] = tier_section("07", "Foto & Video", "Documentation", {
    "Tier 1 — Sinematik Full Team":  9_500_000,
    "Tier 2 — Foto & Video Pro":     7_500_000,
    "Tier 3 — Paket Foto Standar":   6_000_000,
}, "doc")

costs["Entertainment"] = tier_section("08", "Hiburan & Musik", "Entertainment", {
    "Tier 1 — Band / Artis Undangan": 10_000_000,
    "Tier 2 — Live Music Profesional": 7_500_000,
    "Tier 3 — Keyboard / Organ":       5_000_000,
}, "ent")

costs["Master of Ceremony"] = tier_section("09", "Pemandu Acara", "Master of Ceremony", {
    "Tier 1 — MC Nasional":          5_000_000,
    "Tier 2 — MC Profesional Daerah":4_000_000,
    "Tier 3 — MC Lokal Berpengalaman":3_500_000,
}, "mc")

# ═══════════════════════════════════════════════════════════════════════════════
# 10 — WEDDING CATERING
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="s-card"><div class="s-num">10 — Sajian Pernikahan</div><div class="s-title">Wedding Catering</div>', unsafe_allow_html=True)

cat_tiers = {
    "Tier 1 — Premium (Rp 75.000/pax)":  75_000,
    "Tier 2 — Standar (Rp 60.000/pax)":  60_000,
    "Tier 3 — Ekonomis (Rp 45.000/pax)": 45_000,
    "Lainnya (isi manual per pax)": None,
}
cat_sel = st.selectbox("Pilih Tier Catering", list(cat_tiers.keys()), label_visibility="collapsed", key="cat")
if cat_tiers[cat_sel] is None:
    harga_pax = st.number_input("Harga per pax (Rp)", min_value=0, step=1_000, key="cat_man")
else:
    harga_pax = cat_tiers[cat_sel]

buffet_opts = {
    "80% Buffet  /  20% Stall": 0.80,
    "70% Buffet  /  30% Stall": 0.70,
    "60% Buffet  /  40% Stall": 0.60,
}
buf_sel    = st.selectbox("Komposisi Penyajian", list(buffet_opts.keys()), key="buf")
buf_pct    = buffet_opts[buf_sel]
stall_pct  = 1 - buf_pct

pax_buf       = int(total_pax * buf_pct)
pax_stall_1   = int(total_pax * stall_pct)
pax_stall_tot = pax_stall_1 * 3
cost_buf      = pax_buf * harga_pax
cost_stall    = pax_stall_tot * harga_pax
total_cat     = cost_buf + cost_stall
costs["Catering"] = total_cat

# Catering split — st.columns
c1, c2 = st.columns(2)
with c1:
    st.markdown(f"""
    <div class="cat-box">
        <div class="cat-box-title">Buffet (Prasmanan)</div>
        <div class="cat-box-sub">Hidangan utama</div>
        <div class="cat-row"><span>Total Pax</span><span>{total_pax} pax</span></div>
        <div class="cat-row"><span>Porsi Buffet</span><span>{int(buf_pct*100)}%</span></div>
        <div class="cat-row"><span>Pax Buffet</span><span>{pax_buf} pax</span></div>
        <div class="cat-row"><span>Harga/pax</span><span>{idr(harga_pax)}</span></div>
        <div class="cat-total"><span>Subtotal</span><span>{idr(cost_buf)}</span></div>
    </div>""", unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="cat-box">
        <div class="cat-box-title">Stall x 3 Macam</div>
        <div class="cat-box-sub">3 booth makanan berbeda</div>
        <div class="cat-row"><span>Total Pax</span><span>{total_pax} pax</span></div>
        <div class="cat-row"><span>Porsi Stall</span><span>{int(stall_pct*100)}%</span></div>
        <div class="cat-row"><span>Pax / Stall</span><span>{pax_stall_1} pax</span></div>
        <div class="cat-row"><span>x 3 Stall</span><span>{pax_stall_tot} pax total</span></div>
        <div class="cat-row"><span>Harga/pax</span><span>{idr(harga_pax)}</span></div>
        <div class="cat-total"><span>Subtotal</span><span>{idr(cost_stall)}</span></div>
    </div>""", unsafe_allow_html=True)

st.markdown(f"""
<div class="cat-grand">
    Total Catering &nbsp;&#8594;&nbsp;
    <strong style="font-size:1rem; color:#3D2008;">{idr(total_cat)}</strong>
</div>""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # end catering card

# ═══════════════════════════════════════════════════════════════════════════════
# RINCIAN BREAKDOWN — pure st.columns, no broken HTML
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="divider-orn">◆ ◇ ◆</div>', unsafe_allow_html=True)

# Title
st.markdown("""
<div style="background:#FAFAFA; border:1px solid #E8D9C0; border-left:3px solid #6C4118;
            border-radius:6px; padding:1rem 1.6rem 0.5rem 1.6rem; margin-bottom:0;">
    <p style="font-family:'Cormorant Garamond',serif; font-size:1.3rem; color:#3D2008; margin:0 0 0.8rem 0;">
        ✦ Rincian Estimasi Biaya
    </p>
</div>
""", unsafe_allow_html=True)

# Rows via st.columns
row_style_l = """
    font-family:'Jost',sans-serif; font-size:0.88rem; color:#6C4118;
    padding:0.5rem 1.6rem; background:#FAFAFA;
    border-left:3px solid #6C4118; border-right:1px solid #E8D9C0;
    border-bottom:1px dashed #E8D9C0;
"""
row_style_r = """
    font-family:'Jost',sans-serif; font-size:0.88rem; font-weight:600; color:#3D2008;
    text-align:right; padding:0.5rem 1.6rem; background:#FAFAFA;
    border-right:1px solid #E8D9C0; border-bottom:1px dashed #E8D9C0;
"""

for label, val in costs.items():
    col_l, col_r = st.columns([3, 2])
    with col_l:
        st.markdown(f'<div style="{row_style_l}">{label}</div>', unsafe_allow_html=True)
    with col_r:
        st.markdown(f'<div style="{row_style_r}">{idr(val)}</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# GRAND TOTAL
# ═══════════════════════════════════════════════════════════════════════════════
grand_total = sum(costs.values())

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"""
<div class="total-box">
    <div class="total-label">Estimasi Total Biaya Pernikahan</div>
    <div class="total-amount">{idr(grand_total)}</div>
    <div class="total-note">
        ◆ &nbsp; Estimasi dapat berubah sesuai negosiasi dan kondisi vendor &nbsp; ◆<br>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; padding:0.5rem 0 2rem 0;">
    <p style="font-family:'Jost',sans-serif; font-size:0.78rem; color:#9E7A52;
              letter-spacing:0.18em; text-transform:uppercase;">
        Hubungi kami untuk konsultasi dan penawaran khusus
    </p>
</div>
""", unsafe_allow_html=True)
