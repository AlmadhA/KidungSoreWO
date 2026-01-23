import streamlit as st
import base64
import os

# --- 1. SETTING HALAMAN & CSS ---
st.set_page_config(page_title="Kidung Sore Wedding Organizer", layout="wide")

def get_base64_font(font_path):
    with open(font_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
# --- FUNGSI UNTUK KONVERSI GAMBAR KE BASE64 ---
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Font Paths
path_cinzel = "assets/fonts/CinzelDecorative-Bold.ttf"
path_canva = "assets/fonts/CanvaSans-Regular.otf"

if os.path.exists(path_cinzel) and os.path.exists(path_canva):
    font_cinzel = get_base64_font(path_cinzel)
    font_canva = get_base64_font(path_canva)
    
    st.markdown(f"""
        <style>
        @font-face {{ font-family: 'CinzelCustom'; src: url(data:font/ttf;base64,{font_cinzel}) format('truetype'); }}
        @font-face {{ font-family: 'CanvaSansCustom'; src: url(data:font/otf;base64,{font_canva}) format('opentype'); }}
        
        /* Menyembunyikan Navigasi Bawaan Streamlit */
        [data-testid="stSidebarNav"] {{
            display: none;
        }}
        [data-testid="stSidebar"] {{
            background : linear-gradient(90deg, #6C4118 90%, #291808 100%)
        }}
        /* Tombol Sidebar Custom */
        div[data-testid="stVerticalBlock"] > div[style*="flex-direction: column"] > div [data-testid="stVerticalBlock"] {{
            gap: 0rem; /* Menghilangkan jarak antar tombol agar rapat */
        }}
        
        /* Styling Button Sidebar agar menjadi tombol penuh */
        .stButton>button {{
            background-color: #FBF2DC; 
            color: #6C4118;
            font-family: 'CanvaSansCustom', sans-serif;
            border: none; 
            border-radius: 25px; 
            font-weight: bold; 
            margin-bottom: 8px;
            width: 100%;
            height: 50px;
            transition: 0.3s;
            display: block;
        }}
        
        .stButton>button:hover {{
            background-color: #ffffff;
            color: #6C4118;
        }}

        .title-kidung {{ font-family: 'CinzelCustom', serif;
            color: #6C4118;
            font-size: 50px;
            line-height: 0.8;
            margin: 0px; }}
        .subtitle-wo {{ font-family: 'CanvaSansCustom', sans-serif;
            color: #6C4118;
            font-size: 18px;
            letter-spacing: 0px;
            margin-top: 5px;
            margin-bottom: 0px; }}
        
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

# --- 2. LOGIKA NAVIGASI ---
if 'menu' not in st.session_state:
    st.session_state.menu = 'HOME'

def navigate_to(page):
    st.session_state.menu = page

# --- 3. SIDEBAR CUSTOM BUTTONS ---
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("HOME"): navigate_to('HOME')
    if st.button("PRICELIST"): navigate_to('PRICELIST')
    if st.button("WEDDING CALCULATOR"): navigate_to('CALCULATOR')
    if st.button("CONTACT"): navigate_to('CONTACT')

# --- 4. ROUTING HALAMAN ---

# --- PATH LOGO ---
logo_path = "assets/images/logo(kecil).png"

# Pastikan file ada sebelum diproses
if os.path.exists(logo_path):
    img_base64 = get_base64_image(logo_path)
    
    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 30px;">
            <img src="data:image/png;base64,{img_base64}" width="110" style="object-fit: contain;">
            
            <div style="display: flex; flex-direction: column; justify-content: center;">
                <p class="title-kidung">KIDUnG SOrE</p>
                <p class="subtitle-wo">WEDDING ORGANIZER</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.error(f"Logo tidak ditemukan di path: {logo_path}")

import streamlit as st
import base64
import os

# --- 1. FUNGSI HELPER UNTUK GAMBAR ---
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

def render_box_image(image_path, height, label_fallback):
    img_b64 = get_base64_image(image_path)
    if img_b64:
        # Menampilkan Gambar jika file ditemukan
        st.markdown(f"""
            <div class="box-grid" style="height: {height}px; padding: 0px; overflow: hidden; border: 0px solid #6C4118; border-radius: 5px;">
                <img src="data:image/png;base64,{img_b64}" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
        """, unsafe_allow_html=True)
    else:
        # Menampilkan Placeholder jika file tidak ditemukan
        st.markdown(f"""
            <div class="box-grid" style="height: {height}px; display: flex; align-items: center; justify-content: center; background-color: #FBF2DC; border: 2px dashed #6C4118; color: #6C4118; text-align: center;">
                {label_fallback}<br>(Image Not Found)
            </div>
        """, unsafe_allow_html=True)

# --- 2. LOGIKA KONTEN HOME ---
if st.session_state.menu == 'HOME':
    
    # --- MAIN HERO BANNER (60 x 25) ---
    render_box_image("assets/images/Banner 60x25.png", 400, "MAIN HERO BANNER")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- LAYANAN A, B, C ---
    c1, c2, c3 = st.columns([20, 18, 20])
    
    with c1:
        # Menggunakan Banner 20x15 (2) atau disesuaikan
        render_box_image("assets/images/Banner 20x15.png", 250, "Layanan A")
        
    with c2:
        render_box_image("assets/images/Banner 18x15.png", 250, "Layanan B")
        
    with c3:
        # Menggunakan Banner 20x15 (2)
        render_box_image("assets/images/Banner 20x15 (2).png", 250, "Layanan C")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- PORTFOLIO HIGHLIGHTS (60 x 15) ---
    render_box_image("assets/images/Banner 60x15.png", 250, "PORTFOLIO HIGHLIGHTS")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- ADS / TAGLINE (Kotak Terakhir) ---
    # Jika belum ada gambar khusus Ads, bisa gunakan placeholder atau teks saja
    st.markdown("""
        <div style="background-color: #6C4118; padding: 20px; border-radius: 10px; text-align: center;">
            <p style="font-family: 'CanvaSansCustom', sans-serif; color: #FBF2DC; margin: 0;">
                💍 <strong>Semua paket dapat disesuaikan dengan kebutuhan Anda</strong> 💍<br>
                Hubungi kami untuk konsultasi gratis dan penawaran khusus!
            </p>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.menu == 'PRICELIST':
    exec(open("pages/Pricelist.py", encoding='utf-8').read())

elif st.session_state.menu == 'CALCULATOR':
    exec(open("pages/Simulasi.py").read())

elif st.session_state.menu == 'CONTACT':

    exec(open("pages/About Us.py").read())
