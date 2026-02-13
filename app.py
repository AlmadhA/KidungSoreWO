import streamlit as st
import base64
import os
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# --- 1. SETTING HALAMAN & CSS ---
st.set_page_config(page_title="Kidung Sore Wedding Organizer", layout="wide")

# --- FUNGSI GOOGLE SHEETS (MENGGUNAKAN SECRETS) ---
def save_to_gsheet(nama, wa, ig):
    try:
        # Tentukan Scope
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        
        # Ambil info dari secrets
        creds_info = dict(st.secrets["gcp_service_account"])
        
        # Bersihkan private_key dari karakter escape yang mengganggu
        creds_info["private_key"] = creds_info["private_key"].replace("\\n", "\n")
        
        # Proses Kredensial dengan library google-auth
        creds = Credentials.from_service_account_info(creds_info, scopes=scopes)
        client = gspread.authorize(creds)
        
        # Buka sheet
        sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1_iKrqO4LF3weiPAnPv-xKAymSFrjKpXvmn2_nSBm3ZA/edit?usp=sharing").sheet1
        
        # Ambil nomor urut
        no_urut = len(sheet.get_all_values()) 
        waktu_input = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Simpan data
        sheet.append_row([no_urut, waktu_input, nama, wa, ig])
        return True
    except Exception as e:
        st.error(f"Gagal menyimpan ke Google Sheets: {e}")
        return False

# --- FUNGSI UNTUK KONVERSI GAMBAR & FONT ---
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

        [data-testid="stSidebar"] {{ background : linear-gradient(90deg, #6C4118 90%, #291808 100%) }}
        
        /* Styling Button Sidebar agar menjadi tombol penuh */
        .stButton>button {{
            background-color: #FBF2DC; 
            color: #6C4118;
            font-family: 'CanvaSansCustom', sans-serif;
            border: none; 
            border-radius: 8px; /* Tidak terlalu rounded (sebelumnya 25px) */
            font-weight: 800;   /* Font Bold extra */
            margin-bottom: 12px;
            width: 100%;        /* Memastikan semua tombol sama panjang */
            height: 55px;       /* Tinggi seragam */
            transition: all 0.2s ease-in-out;
            /* Efek bayangan awal (timbul halus) */
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            text-transform: uppercase; /* Opsional: membuat teks kapital semua agar seragam */
        }}
        
        .stButton>button:hover {{
            background-color: #ffffff;
            color: #6C4118;
            transform: translateY(-2px);
            box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
        }}

        .stButton>button:active {{
            transform: translateY(1px); /* Tombol seolah tertekan ke bawah */
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1); /* Bayangan mengecil */
        }}

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

# --- 2. LOGIKA NAVIGASI ---
if 'menu' not in st.session_state:
    st.session_state.menu = 'HOME'

def navigate_to(page):
    st.session_state.menu = page

# --- 3. SIDEBAR CUSTOM BUTTONS ---
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("HOME", use_container_width=True): navigate_to('HOME')
    if st.button("PRICELIST", use_container_width=True): navigate_to('PRICELIST')
    if st.button("WEDDING CALCULATOR", use_container_width=True): navigate_to('CALCULATOR')
    if st.button("CONTACT", use_container_width=True): navigate_to('CONTACT')

# --- 4. ROUTING HALAMAN ---

# --- PATH LOGO ---
logo_path = "assets/images/logo(kecil).png"

# Pastikan file ada sebelum diproses
if os.path.exists(logo_path):
    img_base64 = get_base64_image(logo_path)
    
    # --- HEADER DENGAN LOGO DI SEBELAH KIRI ---
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
