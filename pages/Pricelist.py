import streamlit as st

# --- INISIALISASI SESSION STATE UNTUK EXPAND/COLLAPSE ---
if 'show_paket_a' not in st.session_state:
    st.session_state.show_paket_a = False
if 'show_paket_b' not in st.session_state:
    st.session_state.show_paket_b = False
if 'show_paket_c' not in st.session_state:
    st.session_state.show_paket_c = False

# --- FUNGSI TOGGLE ---
def toggle_paket(paket):
    if paket == 'A':
        st.session_state.show_paket_a = not st.session_state.show_paket_a
    elif paket == 'B':
        st.session_state.show_paket_b = not st.session_state.show_paket_b
    elif paket == 'C':
        st.session_state.show_paket_c = not st.session_state.show_paket_c

# --- KONTEN PRICELIST ---
st.markdown("""
    <div style="text-align: center;">
        <h2 style="color: #6C4118; margin-bottom: 0px; font-size: 32px; text-align: left; ">Paket Layanan Wedding Organizer</h2>
        <p style="color: #6C4118; font-size: 18px; text-align: left; ">Pilih paket yang sesuai dengan kebutuhan pernikahan impian Anda</p>
    </div>
    <br>
""", unsafe_allow_html=True)

# --- 3 KOLOM PAKET ---
col1, col2, col3 = st.columns(3)

# === PAKET A ===
with col1:
    st.markdown("""
        <div style="background-color: #FBF2DC; border: 2px solid #6C4118; border-radius: 15px; padding: 25px; text-align: center; height: 100%;">
            <h2 style="font-family: 'CinzelCustom', serif; color: #6C4118; margin-bottom: 0px; font-size: 46px; ">SamIRanA</h2>
            <h3 style="font-family: 'CanvaSansCustom', sans-serif; color: #6C4118; margin-bottom: 15px; font-size: 40px;">Rp 3.499.000</h3>
            <p style="font-family: 'CanvaSansCustom', sans-serif; color: #6C4118; font-size: 16px;">
                <strong>WEDDING DAY ORGANIZER</strong><br>                
                Layanan manajemen hari bahagia yang dirancang untuk memastikan seluruh rangkaian acara terlaksana secara presisi.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("View Details" if not st.session_state.show_paket_a else "View Details", key="btn_a"):
        toggle_paket('A')
    
    if st.session_state.show_paket_a:
        st.markdown("""
            <div style="background-color: #FFFFFF; border: 2px solid #6C4118; border-radius: 15px; padding: 20px; margin-top: 15px;">
                <h4 style="font-family: 'CinzelCustom', serif; color: #6C4118; margin-bottom: 15px;">Detail SamIRanA</h4>
                <div style="font-family: 'CanvaSansCustom', sans-serif; color: #6C4118; text-align: left;">
                    <ul>
                        <li><strong>Orkestrasi Alur Acara<strong></li>
                        <p>Bertanggung jawab penuh atas implementasi rundown secara presisi dan adaptif di lapangan guna menjaga ritme acara tetap harmonis.</p>
                        <li>Tim Pendamping Profesional</li>
                        <p>Dukungan personil ahli (4–5 Specialist Crew) yang bertugas secara spesifik untuk mendampingi pengantin, keluarga, hingga urusan teknis lainnya.</p>
                        <li>Konsolidasi Vendor & Keluarga</li>
                        <p>Sesi koordinasi strategis pra-acara guna menyatukan visi, memastikan kesiapan teknis seluruh vendor, dan menyelaraskan ekspektasi keluarga besar.</p>
                        <li>Pengawasan Operasional Vendor</li>                    
                        <p>Manajemen pengawasan di area acara untuk memastikan seluruh vendor rekanan memberikan layanan terbaik sesuai kontrak dan tepat waktu.</p>                  
                    </ul>
                </div>
            </div>
        """, unsafe_allow_html=True)

# === PAKET B ===
with col2:
    st.markdown("""
        <div style="background-color: #6C4118; border: 2px solid #FBF2DC; border-radius: 15px; padding: 25px; text-align: center; height: 100%;">
            <h2 style="font-family: 'CinzelCustom', serif; color: #FBF2DC; margin-bottom: 0px; font-size: 46px;">AruNikA</h2>
            <h3 style="font-family: 'CanvaSansCustom', sans-serif; color: #FBF2DC; margin-bottom: 15px; font-size: 40px;">Rp 6.499.000</h3>
            <p style="font-family: 'CanvaSansCustom', sans-serif; color: #FBF2DC; font-size: 16px;">
                <strong>FULL WEDDING ORGAZNIZER</strong><br>
                Sebuah layanan komprehensif yang dirancang untuk mewujudkan visi pernikahan impian Anda tanpa kerumitan proses persiapan.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("View Details" if not st.session_state.show_paket_b else "View Details", key="btn_b"):
        toggle_paket('B')
    
    if st.session_state.show_paket_b:
        st.markdown("""
            <div style="background-color: #FFFFFF; border: 2px solid #6C4118; border-radius: 15px; padding: 20px; margin-top: 15px;">
                <h4 style="font-family: 'CinzelCustom', serif; color: #6C4118; margin-bottom: 15px;">Detail AruNikA</h4>
                <div style="font-family: 'CanvaSansCustom', sans-serif; color: #6C4118; text-align: left;">
                    <ul>
                        <li><strong>Orkestrasi Alur Acara<strong></li>
                        <p>Bertanggung jawab penuh atas implementasi rundown secara presisi dan adaptif di lapangan guna menjaga ritme acara tetap harmonis.</p>
                        <li>Tim Pendamping Profesional</li>
                        <p>Dukungan personil ahli (6–7 Specialist Crew) yang bertugas secara spesifik untuk mendampingi pengantin, keluarga, hingga urusan teknis lainnya.</p>
                        <li>Konsolidasi Vendor dan Keluarga</li>
                        <p>Sesi koordinasi strategis pra-acara guna menyatukan visi, memastikan kesiapan teknis seluruh vendor, dan menyelaraskan ekspektasi keluarga besar.</p>
                        <li>Pengawasan Operasional Vendor</li>
                        <p>Manajemen pengawasan di area acara untuk memastikan seluruh vendor rekanan memberikan layanan terbaik sesuai kontrak dan tepat waktu.</p>
                        <li><strong>Konsultasi Strategis & Brainstorming Konsep<strong></li>
                        <p>Diskusi mendalam untuk membedah visi dan estetika pernikahan guna menciptakan konsep yang autentik dan personal.</p>
                        <li>Sesi Koordinasi Berkala</li>                    
                        <p>Pertemuan rutin secara tatap muka maupun daring untuk memastikan setiap tahapan persiapan berjalan sesuai jadwal.</p>                  
                    </ul>
                </div>
            </div>
        """, unsafe_allow_html=True)

# === PAKET C ===
with col3:
    st.markdown("""
        <div style="background-color: #FBF2DC; border: 2px solid #6C4118; border-radius: 15px; padding: 25px; text-align: center; height: 100%;">
            <h2 style="font-family: 'CinzelCustom', serif; color: #6C4118; margin-bottom: 0px; font-size: 46px; ">CAndRaMayA</h2>
            <h3 style="font-family: 'CanvaSansCustom', sans-serif; color: #6C4118; margin-bottom: 15px; font-size: 40px;">Rp 4.499.000</h3>
            <p style="font-family: 'CanvaSansCustom', sans-serif; color: #6C4118; font-size: 16px;">
                <strong>INTIMATE WEDDING ORGANIZER</strong><br>                
                Mewujudkan pernikahan intim yang hangat dan teduh, menciptakan kemewahan dengan makna yang mendalam dalam setiap perayaan berskala terbatas.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("View Details" if not st.session_state.show_paket_c else "View Details", key="btn_c"):
        toggle_paket('C')
    
    if st.session_state.show_paket_c:
        st.markdown("""
            <div style="background-color: #FFFFFF; border: 2px solid #6C4118; border-radius: 15px; padding: 20px; margin-top: 15px;">
                <h4 style="font-family: 'CinzelCustom', serif; color: #6C4118; margin-bottom: 15px;">Detail AruNikA</h4>
                <div style="font-family: 'CanvaSansCustom', sans-serif; color: #6C4118; text-align: left;">
                    <ul>
                        <li><strong>Orkestrasi Alur Acara<strong></li>
                        <p>Bertanggung jawab penuh atas implementasi rundown secara presisi dan adaptif di lapangan guna menjaga ritme acara tetap harmonis.</p>
                        <li>Tim Pendamping Profesional</li>
                        <p>Dukungan personil ahli (4–5 Specialist Crew) yang bertugas secara spesifik untuk mendampingi pengantin, keluarga, hingga urusan teknis lainnya.</p>
                        <li>Konsolidasi Vendor dan Keluarga</li>
                        <p>Sesi koordinasi strategis pra-acara guna menyatukan visi, memastikan kesiapan teknis seluruh vendor, dan menyelaraskan ekspektasi keluarga besar.</p>
                        <li>Pengawasan Operasional Vendor</li>
                        <p>Manajemen pengawasan di area acara untuk memastikan seluruh vendor rekanan memberikan layanan terbaik sesuai kontrak dan tepat waktu.</p>
                        <li><strong>Konsultasi Strategis & Brainstorming Konsep Intimate<strong></li>
                        <p>Diskusi mendalam untuk merancang konsep pernikahan yang personal, mengutamakan estetika yang hangat dan interaksi yang berkualitas.</p>
                        <li>Sesi Koordinasi Berkala</li>                    
                        <p>Pertemuan rutin secara tatap muka maupun daring untuk memastikan setiap tahapan persiapan berjalan sesuai jadwal.</p>                  
                    </ul>
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- FOOTER NOTE ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="background-color: #6C4118; padding: 20px; border-radius: 10px; text-align: center;">
        <p style="font-family: 'CanvaSansCustom', sans-serif; color: #FBF2DC; margin: 0;">
            💍 <strong>Semua paket dapat disesuaikan dengan kebutuhan Anda</strong> 💍<br>
            Hubungi kami untuk konsultasi gratis dan penawaran khusus!
        </p>
    </div>

""", unsafe_allow_html=True)
