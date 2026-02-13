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
        color: #FBF2DC !important;
        padding: 12px 25px;
        border-radius: 8px;
        text-decoration: none !important;
        font-family: 'CanvaSansCustom', sans-serif;
        font-weight: bold;
        transition: all 0.3s ease;
        display: inline-block;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .social-btn:hover {
        background-color: #291808;
        color: #FBF2DC !important;
        transform: translateY(-2px);
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
        text-decoration: none !important;
    }
    .social-btn:visited {
        color: #FBF2DC !important;
    }
    .social-btn:active {
        color: #FBF2DC !important;
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
                <a href="https://wa.me/6282131936306" class="contact-link" target="_blank">
                    +62 821-3193-6306
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="contact-card">
            <div class="contact-icon">📧</div>
            <div class="contact-label">Email</div>
            <div class="contact-info">
                <a href="mailto:kidungsore.wo@gmail.com" class="contact-link">
                    kidungsore.wo@gmail.com
                </a>
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
                08:00 - 19:00 WIB<br><br>
                <strong>Sabtu</strong><br>
                08:00 - 17:00 WIB<br><br>
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
                Jl. Simpang Raya Langsep Gang 6 No.2,<br>
                RT.6/RW.2, Pisang C, Kec. Sukun,<br>
                Kota Malang, Jawa Timur 65146<br>
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
                <a href="https://instagram.com/kidungsore_wo" class="contact-link" target="_blank">
                    @kidungsore_wo
                </a><br>                
                <strong>TikTok:</strong> 
                <a href="https://tiktok.com/@kidungsore_wo" class="contact-link" target="_blank">
                    @kidungsore_wo
                </a><br>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- SOCIAL MEDIA BUTTONS ---
st.markdown("""
    <div class="social-buttons">
        <a href="https://wa.me/6282131936306" class="social-btn" target="_blank">
            💬 Chat WhatsApp
        </a>
        <a href="https://instagram.com/kidungsore_wo" class="social-btn" target="_blank">
            📷 Follow Instagram
        </a>
        <a href="mailto:kidungsore.wo@gmail.com" class="social-btn" target="_blank">
            ✉️ Kirim Email
        </a>
    </div>
    <br>
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
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3951.1965736615375!2d112.61143990000001!3d-7.978623700000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x82c3559fb0d241d%3A0x6121bc663ae492b6!2sKidung%20Sore%20Wedding%20Organizer!5e0!3m2!1sid!2sid!4v1770966250824!5m2!1sid!2sid" 
            width="100%" 
            height="400" 
            style="border:0; border-radius: 10px;" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade">
        </iframe>
        <br><br>
    </div>
    </div>
""", unsafe_allow_html=True)

# --- CALL TO ACTION BOX ---
st.markdown("""
    <div class="cta-box">
        <p class="cta-text">
            💍 <strong>Siap Merencanakan Pernikahan Impian Anda?</strong> 💍<br>
            Full Konsultasi Gratis kapan saja!<br>
            Hubungi kami sekarang dan dapatkan penawaran spesial.
        </p>
        <a href="https://wa.me/6282131936306?text=Halo%20Kidung%20Sore%2C%20saya%20ingin%20bertanya%20tentang%20paket-paket%20yang%20ada..." 
           class="social-btn" 
           target="_blank" 
           style="background-color: #FBF2DC; color: #6C4118 !important; font-size: 18px; padding: 15px 30px;">
            🎉 Konsultasi Gratis Sekarang
        </a>
    </div>
""", unsafe_allow_html=True)
