import streamlit as st

# --- CONTACT US PAGE ---
st.markdown("""
    <style>
    .contact-header {
        text-align: center;
        margin-bottom: 30px;
    }
    .contact-title {
        font-family: 'CinzelCustom', serif;
        color: #6C4118;
        font-size: 48px;
        margin-bottom: 10px;
    }
    .contact-subtitle {
        font-family: 'CanvaSansCustom', sans-serif;
        color: #6C4118;
        font-size: 18px;
        margin-bottom: 20px;
    }
    .contact-card {
        background: linear-gradient(135deg, #FBF2DC 0%, #F5E6C8 100%);
        border: 2px solid #6C4118;
        border-radius: 15px;
        padding: 30px;
        margin-bottom: 20px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }
    .contact-icon {
        font-size: 40px;
        margin-bottom: 15px;
        text-align: center;
    }
    .contact-label {
        font-family: 'CinzelCustom', serif;
        color: #6C4118;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 8px;
        text-align: center;
    }
    .contact-info {
        font-family: 'CanvaSansCustom', sans-serif;
        color: #6C4118;
        font-size: 16px;
        text-align: center;
        line-height: 1.6;
    }
    .contact-link {
        color: #6C4118;
        text-decoration: none;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .contact-link:hover {
        color: #291808;
        text-decoration: underline;
    }
    .social-buttons {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 20px;
        flex-wrap: wrap;
    }
    .social-btn {
        background-color: #6C4118;
        color: #FBF2DC;
        padding: 12px 25px;
        border-radius: 8px;
        text-decoration: none;
        font-family: 'CanvaSansCustom', sans-serif;
        font-weight: bold;
        transition: all 0.3s ease;
        display: inline-block;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .social-btn:hover {
        background-color: #291808;
        transform: translateY(-2px);
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
    }
    .map-container {
        background-color: #FBF2DC;
        border: 2px solid #6C4118;
        border-radius: 15px;
        padding: 20px;
        margin-top: 30px;
    }
    .cta-box {
        background: linear-gradient(135deg, #6C4118 0%, #291808 100%);
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        margin-top: 30px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    .cta-text {
        font-family: 'CanvaSansCustom', sans-serif;
        color: #FBF2DC;
        font-size: 20px;
        margin-bottom: 20px;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class="contact-header">
        <h1 class="contact-title">Hubungi Kami</h1>
        <p class="contact-subtitle">
            Kami siap membantu mewujudkan pernikahan impian Anda.<br>
            Jangan ragu untuk menghubungi kami melalui berbagai channel di bawah ini.
        </p>
    </div>
""", unsafe_allow_html=True)

# --- CONTACT INFORMATION GRID ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="contact-card">
            <div class="contact-icon">📱</div>
            <div class="contact-label">WhatsApp</div>
            <div class="contact-info">
                <a href="https://wa.me/62XXXXXXXXXXX" class="contact-link" target="_blank">
                    +62 XXX-XXXX-XXXX
                </a>
                <br><br>
                <strong>GANTI NOMOR DI SINI</strong><br>
                Format: 62XXXXXXXXXXX<br>
                (tanpa tanda + dan spasi)
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="contact-card">
            <div class="contact-icon">📧</div>
            <div class="contact-label">Email</div>
            <div class="contact-info">
                <a href="mailto:info@kidungsore.com" class="contact-link">
                    info@kidungsore.com
                </a>
                <br><br>
                <strong>GANTI EMAIL DI SINI</strong><br>
                Masukkan email resmi bisnis Anda
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="contact-card">
            <div class="contact-icon">🕐</div>
            <div class="contact-label">Jam Operasional</div>
            <div class="contact-info">
                <strong>Senin - Jumat</strong><br>
                09:00 - 17:00 WIB<br><br>
                <strong>Sabtu</strong><br>
                09:00 - 14:00 WIB<br><br>
                <strong>GANTI JAM DI SINI</strong>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- SOCIAL MEDIA & CONTACT BUTTONS ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="contact-card">
            <div class="contact-icon">📍</div>
            <div class="contact-label">Alamat Kantor</div>
            <div class="contact-info">
                Jl. Nama Jalan No. XX<br>
                Kelurahan/Desa, Kecamatan<br>
                Kota, Provinsi 12345<br>
                Indonesia<br><br>
                <strong>GANTI ALAMAT LENGKAP DI SINI</strong>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="contact-card">
            <div class="contact-icon">🌐</div>
            <div class="contact-label">Sosial Media</div>
            <div class="contact-info">
                <strong>Instagram:</strong> 
                <a href="https://instagram.com/kidungsore.wo" class="contact-link" target="_blank">
                    @kidungsore.wo
                </a><br>
                <strong>GANTI USERNAME INSTAGRAM</strong><br><br>
                
                <strong>Facebook:</strong> 
                <a href="https://facebook.com/kidungsorewo" class="contact-link" target="_blank">
                    Kidung Sore WO
                </a><br>
                <strong>GANTI NAMA/URL FACEBOOK</strong><br><br>
                
                <strong>TikTok:</strong> 
                <a href="https://tiktok.com/@kidungsore.wo" class="contact-link" target="_blank">
                    @kidungsore.wo
                </a><br>
                <strong>GANTI USERNAME TIKTOK</strong>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- SOCIAL MEDIA BUTTONS ---
st.markdown("""
    <div class="social-buttons">
        <a href="https://wa.me/62XXXXXXXXXXX" class="social-btn" target="_blank">
            💬 Chat WhatsApp
        </a>
        <a href="https://instagram.com/kidungsore.wo" class="social-btn" target="_blank">
            📷 Follow Instagram
        </a>
        <a href="mailto:info@kidungsore.com" class="social-btn" target="_blank">
            ✉️ Kirim Email
        </a>
    </div>
    <br>
    <p style="text-align: center; font-family: 'CanvaSansCustom', sans-serif; color: #6C4118; font-size: 14px;">
        <strong>GANTI SEMUA LINK DI ATAS SESUAI DENGAN KONTAK ANDA</strong>
    </p>
""", unsafe_allow_html=True)

# --- GOOGLE MAPS EMBED (OPTIONAL) ---
st.markdown("""
    <div class="map-container">
        <div class="contact-label" style="margin-bottom: 15px;">📍 Lokasi Kami</div>
""", unsafe_allow_html=True)

# GANTI DENGAN EMBED CODE GOOGLE MAPS ANDA
# Cara mendapatkan: Buka Google Maps > Cari lokasi Anda > Klik "Share" > "Embed a map" > Copy HTML
st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <iframe 
            src="https://www.google.com/maps/embed?pb=GANTI_DENGAN_EMBED_CODE_ANDA" 
            width="100%" 
            height="400" 
            style="border:0; border-radius: 10px;" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade">
        </iframe>
        <br><br>
        <p style="font-family: 'CanvaSansCustom', sans-serif; color: #6C4118; font-size: 14px;">
            <strong>CARA MENGGANTI MAPS:</strong><br>
            1. Buka Google Maps dan cari lokasi kantor Anda<br>
            2. Klik tombol "Share" atau "Bagikan"<br>
            3. Pilih tab "Embed a map"<br>
            4. Copy kode HTML yang muncul<br>
            5. Ganti bagian src="..." di atas dengan URL dari kode tersebut
        </p>
    </div>
    </div>
""", unsafe_allow_html=True)

# --- CALL TO ACTION BOX ---
st.markdown("""
    <div class="cta-box">
        <p class="cta-text">
            💍 <strong>Siap Merencanakan Pernikahan Impian Anda?</strong> 💍<br>
            Konsultasi gratis untuk paket wedding organizer kami!<br>
            Hubungi kami sekarang dan dapatkan penawaran spesial.
        </p>
        <a href="https://wa.me/62XXXXXXXXXXX?text=Halo%20Kidung%20Sore%2C%20saya%20tertarik%20dengan%20paket%20wedding%20organizer" 
           class="social-btn" 
           target="_blank" 
           style="background-color: #FBF2DC; color: #6C4118; font-size: 18px; padding: 15px 30px;">
            🎉 Konsultasi Gratis Sekarang
        </a>
        <br><br>
        <p style="font-family: 'CanvaSansCustom', sans-serif; color: #FBF2DC; font-size: 14px;">
            <strong>GANTI NOMOR WHATSAPP DI LINK DI ATAS</strong>
        </p>
    </div>
""", unsafe_allow_html=True)

# --- FOOTER NOTE ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
    <div style="background-color: #FBF2DC; padding: 20px; border-radius: 10px; text-align: center; border: 1px solid #6C4118;">
        <p style="font-family: 'CanvaSansCustom', sans-serif; color: #6C4118; margin: 0; font-size: 14px;">
            <strong>📋 CHECKLIST INFORMASI YANG PERLU DIGANTI:</strong><br><br>
            ✅ Nomor WhatsApp (3 tempat)<br>
            ✅ Email<br>
            ✅ Jam Operasional<br>
            ✅ Alamat Lengkap<br>
            ✅ Username Instagram<br>
            ✅ Nama/URL Facebook<br>
            ✅ Username TikTok<br>
            ✅ Google Maps Embed Code<br>
            ✅ Link tombol sosial media (WhatsApp, Instagram, Email)<br>
            ✅ Link CTA button WhatsApp dengan text otomatis
        </p>
    </div>
""", unsafe_allow_html=True)
