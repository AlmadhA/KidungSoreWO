import streamlit as st
import base64
import os

# --- 1. SETTING HALAMAN ---
st.set_page_config(page_title="Kidung Sore Wedding Organizer", layout="wide", page_icon="assets/images/Logo Icon.png")

# --- FULL WIDTH ---
st.markdown("""
    <style>
    .block-container {
        max-width: 100% !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNGSI UNTUK KONVERSI FONT & GAMBAR ---
def get_base64_font(font_path):
    with open(font_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

# --- LOAD FONT ---
path_cinzel = "assets/fonts/CinzelDecorative-Bold.ttf"
path_canva = "assets/fonts/CanvaSans-Regular.otf"

if os.path.exists(path_cinzel) and os.path.exists(path_canva):
    font_cinzel = get_base64_font(path_cinzel)
    font_canva = get_base64_font(path_canva)

    st.markdown(f"""
        <style>
        @font-face {{ font-family: 'CinzelCustom'; src: url(data:font/ttf;base64,{font_cinzel}) format('truetype'); }}
        @font-face {{ font-family: 'CanvaSansCustom'; src: url(data:font/otf;base64,{font_canva}) format('opentype'); }}

        /* Sembunyikan navigasi & sidebar bawaan Streamlit */
        [data-testid="stSidebarNav"] {{ display: none; }}
        [data-testid="stSidebar"] {{ display: none; }}

        /* Styling Tab */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 8px;
            background-color: transparent;
            border-bottom: 2px solid #6C4118;
            margin-bottom: 20px;
        }}
        .stTabs [data-baseweb="tab"] {{
            background-color: #FBF2DC;
            color: #6C4118;
            border-radius: 8px 8px 0px 0px;
            font-family: 'CanvaSansCustom', sans-serif;
            font-weight: 800;
            font-size: 15px;
            padding: 10px 20px;
            border: 1px solid #6C4118;
            border-bottom: none;
        }}
        .stTabs [aria-selected="true"] {{
            background-color: #6C4118 !important;
            color: #FBF2DC !important;
        }}
        .stTabs [data-baseweb="tab"]:hover {{
            background-color: #e8dcc8;
            color: #6C4118;
        }}

        /* Judul & Subjudul */
        .title-kidung {{ font-family: 'CinzelCustom', serif; color: #6C4118; font-size: 50px !important; line-height: 1; margin-bottom: 0px; }}
        .subtitle-wo {{ font-family: 'CanvaSansCustom', sans-serif; color: #6C4118; font-size: 25px !important; letter-spacing: 0px; margin-top: 5px; margin-bottom: -5px; }}

        /* Grid Style */
        .box-grid {{
            background-color: #FBF2DC;
            border: 1px solid #6C4118;
            display: flex; align-items: center; justify-content: center;
            color: #6C4118; font-family: 'CanvaSansCustom', sans-serif;
            margin-bottom: 15px; text-align: center;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- FUNGSI RENDER GAMBAR ---
def render_box_image(image_path, height, label_fallback):
    img_b64 = get_base64_image(image_path)
    if img_b64:
        st.markdown(f"""
            <div class="box-grid" style="height: {height}px; padding: 0px; overflow: hidden; border: 0px solid #6C4118; border-radius: 5px;">
                <img src="data:image/png;base64,{img_b64}" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="box-grid" style="height: {height}px; display: flex; align-items: center; justify-content: center; background-color: #FBF2DC; border: 2px dashed #6C4118; color: #6C4118; text-align: center;">
                {label_fallback}<br>(Image Not Found)
            </div>
        """, unsafe_allow_html=True)

# --- HEADER: LOGO + JUDUL ---
logo_path = "assets/images/logo(kecil).png"
img_base64 = get_base64_image(logo_path)

if img_base64:
    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 25px;">
            <img src="data:image/png;base64,{img_base64}" width="100" style="object-fit: contain;">
            <div>
                <p class="title-kidung">KIDUnG SOrE</p>
                <p class="subtitle-wo">WEDDING ORGANIZER</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.error(f"Logo tidak ditemukan di path: {logo_path}")

# --- NAVIGASI TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["HOME", "PRICELIST", "WEDDING CALCULATOR", "CONTACT"])

# ===================== TAB HOME =====================
with tab1:
    render_box_image("assets/images/Banner 60x25.png", 400, "MAIN HERO BANNER")
    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([20, 18, 20])
    with c1:
        render_box_image("assets/images/Banner 20x15.png", 250, "Layanan A")
    with c2:
        render_box_image("assets/images/Banner 18x15.png", 250, "Layanan B")
    with c3:
        render_box_image("assets/images/Banner 20x15 (2).png", 250, "Layanan C")

    st.markdown("<br>", unsafe_allow_html=True)
    render_box_image("assets/images/Banner 60x15.png", 250, "PORTFOLIO HIGHLIGHTS")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
        <div style="background-color: #6C4118; padding: 20px; border-radius: 10px; text-align: center;">
            <p style="font-family: 'CanvaSansCustom', sans-serif; color: #FBF2DC; margin: 0;">
                💍 <strong>Semua paket dapat disesuaikan dengan kebutuhan Anda</strong> 💍<br>
                Hubungi kami untuk konsultasi gratis dan penawaran khusus!
            </p>
        </div>
    """, unsafe_allow_html=True)

# ===================== TAB PRICELIST =====================
with tab2:
    exec(open("pages/Pricelist.py", encoding='utf-8').read())

# ===================== TAB WEDDING CALCULATOR =====================
with tab3:
    exec(open("pages/Simulasi.py", encoding='utf-8').read())

# ===================== TAB CONTACT =====================
with tab4:
    exec(open("pages/About Us.py", encoding='utf-8').read())


