import streamlit as st
import pandas as pd
import joblib
import re
from data import STUDY_TIPS, TOPIC_DISTRIBUTION, QUESTIONS
from data import TOTAL_SCORE_TARGET, MAX_SCORE
from kunci_jawaban import KUNCI_JAWABAN, KOLOM_MAPPING

# ============================================
# KONFIGURASI HALAMAN
# ============================================
st.set_page_config(
    page_title="🌿 JLPT N4 Predictor | Prediksi Kelulusan",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CUSTOM CSS - TEMA HIJAU HITAM PUTIH
# ============================================
st.markdown("""
<style>
    /* Background utama - Hitam */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0d0d0d 100%);
    }
    
    /* Hide default Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom card */
    .custom-card {
        background: rgba(30, 30, 30, 0.9);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 28px;
        border: 1px solid rgba(46, 204, 113, 0.3);
        box-shadow: 0 8px 32px 0 rgba(46, 204, 113, 0.1);
        margin-bottom: 20px;
    }
    
    /* Main title */
    .main-title {
        text-align: center;
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #2ecc71 0%, #27ae60 50%, #1abc9c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        letter-spacing: 2px;
    }
    
    .subtitle {
        text-align: center;
        color: #888888;
        font-size: 0.95rem;
        margin-bottom: 2rem;
        letter-spacing: 1px;
    }
    
    .badge-pass {
        background: linear-gradient(135deg, #2ecc71, #27ae60);
        color: white;
        padding: 12px 28px;
        border-radius: 40px;
        font-weight: bold;
        font-size: 1.2rem;
        display: inline-block;
        box-shadow: 0 4px 15px rgba(46, 204, 113, 0.3);
    }
    
    .badge-fail {
        background: linear-gradient(135deg, #e74c3c, #c0392b);
        color: white;
        padding: 12px 28px;
        border-radius: 40px;
        font-weight: bold;
        font-size: 1.2rem;
        display: inline-block;
        box-shadow: 0 4px 15px rgba(231, 76, 60, 0.3);
    }
    
    .score-box {
        background: rgba(46, 204, 113, 0.1);
        border-radius: 16px;
        padding: 15px;
        text-align: center;
        border: 1px solid rgba(46, 204, 113, 0.3);
        transition: all 0.3s ease;
    }
    
    .score-box:hover {
        background: rgba(46, 204, 113, 0.2);
        transform: translateY(-3px);
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0a0a 0%, #111111 100%);
        border-right: 1px solid rgba(46, 204, 113, 0.3);
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: #dddddd;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #2ecc71, #27ae60);
        color: white;
        border: none;
        border-radius: 40px;
        padding: 12px 28px;
        font-weight: bold;
        font-size: 1rem;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(46, 204, 113, 0.4);
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(30, 30, 30, 0.8);
        border-radius: 16px;
        padding: 6px;
        border: 1px solid rgba(46, 204, 113, 0.2);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 12px;
        padding: 10px 24px;
        color: #cccccc;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #2ecc71, #27ae60);
        color: white;
    }
    
    .stNumberInput input {
        background: rgba(30, 30, 30, 0.8);
        border: 1px solid rgba(46, 204, 113, 0.3);
        border-radius: 12px;
        color: white;
    }
    
    .stNumberInput input:focus {
        border-color: #2ecc71;
        box-shadow: 0 0 5px rgba(46, 204, 113, 0.5);
    }
    
    [data-testid="stMetricValue"] {
        font-size: 2rem !important;
        font-weight: bold;
        color: #2ecc71 !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: #aaaaaa !important;
    }
    
    .stProgress > div > div {
        background: linear-gradient(90deg, #2ecc71, #27ae60);
    }
    
    .streamlit-expanderHeader {
        background: rgba(46, 204, 113, 0.1);
        border-radius: 12px;
        color: #dddddd;
        border: 1px solid rgba(46, 204, 113, 0.2);
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(46, 204, 113, 0.2);
    }
    
    .stAlert {
        background: rgba(46, 204, 113, 0.1);
        border: 1px solid rgba(46, 204, 113, 0.3);
        border-radius: 16px;
        color: #dddddd;
    }
    
    .stSuccess {
        background: rgba(46, 204, 113, 0.15);
        border: 1px solid #2ecc71;
        border-radius: 16px;
    }
    
    .stError {
        background: rgba(231, 76, 60, 0.15);
        border: 1px solid #e74c3c;
        border-radius: 16px;
    }
    
    .dataframe {
        background: rgba(30, 30, 30, 0.8);
        border-radius: 12px;
    }
    
    .footer {
        text-align: center;
        color: #666666;
        font-size: 11px;
        padding: 25px;
        margin-top: 40px;
        border-top: 1px solid rgba(46, 204, 113, 0.2);
    }
    
    .sidebar-header {
        color: #2ecc71;
        font-size: 1.1rem;
        font-weight: bold;
        margin-top: 15px;
        margin-bottom: 10px;
    }
    
    .green-text {
        color: #2ecc71;
    }
    
    .white-text {
        color: #ffffff;
    }
    
    .status-benar {
        color: #2ecc71 !important;
        font-weight: bold;
    }
    
    .status-salah {
        color: #e74c3c !important;
        font-weight: bold;
    }
    
    .rekomendasi-box {
        background: rgba(46, 204, 113, 0.05);
        border-left: 4px solid #2ecc71;
        padding: 10px 15px;
        border-radius: 8px;
        margin: 5px 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# HEADER
# ============================================
st.markdown('<div class="main-title">🌿 JLPT N4 Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Sistem Prediksi Kesiapan Ujian JLPT N4 | Machine Learning</div>', unsafe_allow_html=True)
st.markdown("---")

# ============================================
# LOAD MODEL
# ============================================
@st.cache_resource
def load_model():
    try:
        return joblib.load('model_jlpt.pkl')
    except:
        return None

model = load_model()

# ============================================
# FUNGSI HITUNG TOTAL POIN
# ============================================
def hitung_total_poin(kanji, kosakata, grammar, reading):
    total_persen = kanji + kosakata + grammar + reading
    total_poin = total_persen * 0.3
    return round(total_poin, 1)

def get_status_dan_alasan(total_poin):
    if total_poin >= TOTAL_SCORE_TARGET:
        return "SIAP", "🌿✅", f"Total poin {total_poin} ≥ {TOTAL_SCORE_TARGET}"
    else:
        return "BELUM SIAP", "⚠️❌", f"Total poin {total_poin} < {TOTAL_SCORE_TARGET}"

# ============================================
# SIDEBAR
# ============================================
with st.sidebar:
    st.markdown("### 🌿 JLPT N4 Predictor")
    st.markdown("---")
    
    st.markdown("#### 📖 Tentang Aplikasi")
    st.markdown("""
    Aplikasi ini menggunakan algoritma **Decision Tree** 
    untuk memprediksi kelulusan JLPT N4 berdasarkan hasil tryout.
    """)
    
    st.markdown("---")
    
    st.markdown('<p class="sidebar-header">📊 Kriteria Kelulusan</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🎯 Target", f"{TOTAL_SCORE_TARGET} poin")
    with col2:
        st.metric("📈 Maksimal", f"{MAX_SCORE} poin")
    
    st.markdown("**Rumus Perhitungan:**")
    st.code("(Kanji + Kosakata + Grammar + Reading) × 0.3", language="python")
    
    st.markdown("---")
    
    st.markdown('<p class="sidebar-header">💡 Tips Belajar Cepat</p>', unsafe_allow_html=True)
    
    with st.expander("📚 Grammar", expanded=False):
        st.markdown("• Latih 5-7 pola kalimat/hari\n• Gunakan sumber: Try! JLPT N4 Grammar\n• Buat contoh kalimat sendiri")
    
    with st.expander("📖 Reading", expanded=False):
        st.markdown("• Baca 2-3 teks pendek/hari\n• Gunakan NHK News Easy\n• Latihan mencari ide pokok")
    
    with st.expander("📝 Kanji & Kosakata", expanded=False):
        st.markdown("• Hafal 10-15 kanji/hari\n• Gunakan flashcards Anki\n• Buat kartu ingatan")
    
    st.markdown("---")
    st.caption("© 2024 - JLPT N4 Predictor\nBuilt with Streamlit")

# ============================================
# FUNGSI EKSTRAK ANGKA JAWABAN
# ============================================
def ekstrak_angka(jawaban_text):
    if pd.isna(jawaban_text):
        return None
    jawaban_str = str(jawaban_text).strip()
    match = re.match(r'^(\d+)', jawaban_str)
    if match:
        return int(match.group(1))
    return None

def get_nomor_dari_kolom(nama_kolom):
    nama = nama_kolom.strip()
    
    if nama in KOLOM_MAPPING:
        return KOLOM_MAPPING[nama]
    
    for key, value in KOLOM_MAPPING.items():
        if key in nama or nama in key:
            return value
    
    match = re.match(r'^\((\d+)\)', nama)
    if match:
        return int(match.group(1))
    
    match = re.match(r'^(\d+)\.', nama)
    if match:
        return int(match.group(1))
    
    return None

def get_option_text(nomor_soal, pilihan_angka):
    if nomor_soal in QUESTIONS and 1 <= pilihan_angka <= 4:
        options = QUESTIONS[nomor_soal].get('options', [])
        if pilihan_angka <= len(options):
            return options[pilihan_angka - 1]
    return None

def get_soal_text(nomor_soal):
    if nomor_soal in QUESTIONS:
        return QUESTIONS[nomor_soal].get('text', '')
    return None

def koreksi_jawaban_csv(df_responses):
    kolom_info = []
    for col in df_responses.columns:
        nomor = get_nomor_dari_kolom(col)
        if nomor is not None:
            kolom_info.append({'nomor': nomor, 'kolom': col})
    
    semua_hasil = []
    
    for idx, row in df_responses.iterrows():
        nama = row.get('NAMA :', f'Responden_{idx+1}')
        if pd.isna(nama):
            nama = f'Responden_{idx+1}'
        
        jawaban_peserta = {}
        
        for info in kolom_info:
            nomor = info['nomor']
            kolom = info['kolom']
            jawaban_text = row.get(kolom, None)
            jawaban_angka = ekstrak_angka(jawaban_text)
            
            if jawaban_angka is not None and 1 <= nomor <= 70:
                jawaban_peserta[nomor] = jawaban_angka
        
        skor_topik = {}
        detail_per_soal = {}
        
        for topik, soal_list in TOPIC_DISTRIBUTION.items():
            benar = 0
            total = 0
            for nomor in soal_list:
                if nomor in jawaban_peserta and nomor in KUNCI_JAWABAN:
                    total += 1
                    kunci = KUNCI_JAWABAN[nomor]
                    jawaban = jawaban_peserta[nomor]
                    is_benar = (jawaban == kunci)
                    if is_benar:
                        benar += 1
                    
                    detail_per_soal[nomor] = {
                        'topik': topik,
                        'jawaban': jawaban,
                        'is_benar': is_benar,
                        'jawaban_teks': get_option_text(nomor, jawaban),
                        'soal_text': get_soal_text(nomor)
                    }
            skor_topik[topik] = (benar / total * 100) if total > 0 else 0
        
        kanji_persen = skor_topik.get("文字・語彙", 0)
        grammar_persen = skor_topik.get("文法", 0)
        reading_persen = skor_topik.get("読解", 0)
        kosakata_persen = skor_topik.get("文字・語彙", 0)
        
        total_poin = hitung_total_poin(kanji_persen, kosakata_persen, grammar_persen, reading_persen)
        
        semua_hasil.append({
            'nama': nama,
            'detail_skor': skor_topik,
            'detail_per_soal': detail_per_soal,
            'total_poin': total_poin,
            'kanji': kanji_persen,
            'kosakata': kosakata_persen,
            'grammar': grammar_persen,
            'reading': reading_persen
        })
    
    return semua_hasil

def tampilkan_hasil_koreksi(hasil):
    for h in hasil:
        st.markdown("---")
        
        # Header responden
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            st.markdown(f"""
            <div style='text-align: center;'>
                <div style='background: linear-gradient(135deg, #2ecc71, #27ae60); 
                            width: 60px; height: 60px; border-radius: 50%; 
                            display: inline-flex; align-items: center; justify-content: center;
                            font-size: 28px; margin-bottom: 10px;'>
                    🧑
                </div>
                <h3 style='color: #ffffff;'>{h['nama']}</h3>
            </div>
            """, unsafe_allow_html=True)
        
        total_poin = h['total_poin']
        status, icon, alasan = get_status_dan_alasan(total_poin)
        
        # Result card
        col1, col2 = st.columns([2, 1])
        with col1:
            if status == "SIAP":
                st.markdown(f'<div class="badge-pass">{icon} {status}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="badge-fail">{icon} {status}</div>', unsafe_allow_html=True)
            st.caption(alasan)
        
        with col2:
            st.metric("Total Skor", f"{total_poin:.1f} / {MAX_SCORE}")
            st.progress(int(min(total_poin / MAX_SCORE * 100, 100)))
        
        # Score cards
        st.markdown("#### 📊 Skor per Kategori")
        col1, col2, col3, col4 = st.columns(4)
        scores = [
            (col1, "📖 Kanji & Kosakata", (h['kanji'] + h['kosakata']) / 2),
            (col2, "📚 Grammar", h['grammar']),
            (col3, "📰 Reading", h['reading']),
        ]
        
        for col, label, skor in scores:
            with col:
                st.markdown(f"""
                <div class='score-box'>
                    <div style='font-size: 0.9rem; opacity: 0.8;'>{label}</div>
                    <div style='font-size: 1.8rem; font-weight: bold; color: #2ecc71;'>{skor:.0f}%</div>
                    <div style='font-size: 0.8rem;'>{'✓ Baik' if skor >= 60 else '⚠️ Perlu belajar'}</div>
                </div>
                """, unsafe_allow_html=True)
        
        # ===== DETAIL JAWABAN PER SOAL (TANPA KUNCI) =====
        st.markdown("#### 📝 Analisis Jawaban per Soal")
        st.info("💡 Bagian ini menampilkan soal yang perlu dipelajari ulang berdasarkan jawaban yang salah.")
        
        # Pisahkan soal benar dan salah
        soal_benar = []
        soal_salah = []
        
        for nomor in sorted(h['detail_per_soal'].keys()):
            detail = h['detail_per_soal'][nomor]
            if detail['is_benar']:
                soal_benar.append(nomor)
            else:
                soal_salah.append({
                    'No': nomor,
                    'Topik': detail['topik'],
                    'Soal': detail['soal_text'][:60] + '...' if detail['soal_text'] and len(detail['soal_text']) > 60 else detail['soal_text'],
                    'Jawaban Anda': f"{detail['jawaban']}. {detail['jawaban_teks']}" if detail['jawaban_teks'] else str(detail['jawaban'])
                })
        
        # Tampilkan soal yang salah
        if soal_salah:
            st.markdown("##### ❌ Soal yang Perlu Dipelajari Ulang")
            df_salah = pd.DataFrame(soal_salah)
            st.dataframe(
                df_salah,
                use_container_width=True,
                height=min(400, len(soal_salah) * 35 + 38)
            )
            
            # Rekomendasi berdasarkan topik yang salah
            st.markdown("##### 📚 Rekomendasi Belajar berdasarkan Soal Salah")
            
            # Hitung jumlah salah per topik
            salah_per_topik = {}
            for item in soal_salah:
                topik = item['Topik']
                if topik not in salah_per_topik:
                    salah_per_topik[topik] = 0
                salah_per_topik[topik] += 1
            
            for topik, jumlah in sorted(salah_per_topik.items(), key=lambda x: x[1], reverse=True):
                tips = STUDY_TIPS.get(topik, {})
                st.markdown(f"""
                <div class='rekomendasi-box'>
                    <b>⚠️ {topik}</b> - {jumlah} soal salah<br>
                    💡 {tips.get('tips', 'Perbanyak latihan')}<br>
                    🎯 Target: {tips.get('daily_target', 'Latihan rutin')}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.success("🎉 Selamat! Semua soal dijawab dengan benar!")
        
        # Tampilkan statistik
        st.markdown("##### 📊 Statistik Jawaban")
        total_soal = len(h['detail_per_soal'])
        total_benar = len(soal_benar)
        total_salah = len(soal_salah)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Soal", total_soal)
        with col2:
            st.metric("✅ Benar", total_benar)
        with col3:
            st.metric("❌ Salah", total_salah)
        
        # ===== REKOMENDASI UMUM =====
        st.markdown("#### 📚 Rekomendasi Belajar")
        topik_skor = list(h['detail_skor'].items())
        topik_skor.sort(key=lambda x: x[1])
        
        rekomendasi = []
        for topik, skor in topik_skor:
            if skor < 60:
                tips = STUDY_TIPS.get(topik, {})
                rekomendasi.append({
                    'topik': topik,
                    'skor': skor,
                    'tips': tips.get('tips', 'Perbanyak latihan'),
                    'resources': tips.get('resources', []),
                    'daily_target': tips.get('daily_target', 'Latihan rutin')
                })
        
        if rekomendasi:
            for i, r in enumerate(rekomendasi, 1):
                with st.expander(f"⚠️ {r['topik']} - Skor: {r['skor']:.0f}% (Prioritas {i})"):
                    st.markdown(f"💡 **Tips:** {r['tips']}")
                    st.markdown(f"🎯 **Target harian:** {r['daily_target']}")
                    st.markdown("📖 **Sumber belajar:**")
                    for res in r['resources']:
                        st.markdown(f"- {res}")
        else:
            st.success("🎉 Selamat! Semua kategori di atas 60%!")
            st.info("📖 Pertahankan dengan review rutin 2x seminggu.")

def get_rekomendasi(kanji, kosakata, grammar, reading):
    rekomendasi = []
    skor_dict = {
        '文字・語彙': (kosakata + kanji) / 2,
        '文法': grammar,
        '読解': reading
    }
    skor_terurut = sorted(skor_dict.items(), key=lambda x: x[1])
    for topik, skor in skor_terurut:
        if skor < 60:
            tips = STUDY_TIPS.get(topik, {})
            rekomendasi.append({
                'topik': topik,
                'skor': skor,
                'tips': tips.get('tips', 'Perbanyak latihan'),
                'resources': tips.get('resources', []),
                'daily_target': tips.get('daily_target', 'Latihan rutin')
            })
    return rekomendasi

# ============================================
# MAIN TABS
# ============================================
tab1, tab2 = st.tabs(["📝 Input Skor Manual", "📁 Upload CSV Jawaban"])

# ============================================
# TAB 1: INPUT MANUAL
# ============================================
with tab1:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown("### 📝 Masukkan Skor Tryout Anda")
    st.caption(f"🎯 Target lulus: ≥ {TOTAL_SCORE_TARGET} poin dari {MAX_SCORE} poin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        kanji = st.number_input("📖 Kanji (文字)", min_value=0, max_value=100, value=50, step=1, key="manual_kanji")
        kosakata = st.number_input("📝 Kosakata (語彙)", min_value=0, max_value=100, value=50, step=1, key="manual_kosakata")
    
    with col2:
        grammar = st.number_input("📚 Grammar (文法)", min_value=0, max_value=100, value=50, step=1, key="manual_grammar")
        reading = st.number_input("📰 Reading (読解)", min_value=0, max_value=100, value=50, step=1, key="manual_reading")
    
    total_poin = hitung_total_poin(kanji, kosakata, grammar, reading)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if total_poin >= TOTAL_SCORE_TARGET:
            st.success(f"🌿 **Total Skor Anda: {total_poin:.1f} / {MAX_SCORE}** ✅")
        else:
            st.warning(f"📊 **Total Skor Anda: {total_poin:.1f} / {MAX_SCORE}**")
            st.caption(f"⚠️ Perlu meningkatkan {TOTAL_SCORE_TARGET - total_poin:.1f} poin lagi")
    
    if st.button("🌿 Prediksi Sekarang", type="primary", use_container_width=True, key="manual_prediksi"):
        st.markdown("---")
        total_poin = hitung_total_poin(kanji, kosakata, grammar, reading)
        status, icon, alasan = get_status_dan_alasan(total_poin)
        
        col1, col2 = st.columns([2, 1])
        with col1:
            if status == "SIAP":
                st.markdown(f'<div class="badge-pass">{icon} {status}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="badge-fail">{icon} {status}</div>', unsafe_allow_html=True)
            st.caption(alasan)
        with col2:
            st.metric("Total Skor", f"{total_poin:.1f} / {MAX_SCORE}")
            st.progress(int(min(total_poin / MAX_SCORE * 100, 100)))
        
        st.markdown("### 📊 Ringkasan Skor per Kategori")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class='score-box'>
                <div>📖 Kanji</div>
                <div style='font-size: 2rem; font-weight: bold; color: #2ecc71;'>{kanji}%</div>
                <div>{'✓ Baik' if kanji >= 60 else '⚠️ Perlu belajar'}</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class='score-box'>
                <div>📝 Kosakata</div>
                <div style='font-size: 2rem; font-weight: bold; color: #2ecc71;'>{kosakata}%</div>
                <div>{'✓ Baik' if kosakata >= 60 else '⚠️ Perlu belajar'}</div>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class='score-box'>
                <div>📚 Grammar</div>
                <div style='font-size: 2rem; font-weight: bold; color: #2ecc71;'>{grammar}%</div>
                <div>{'✓ Baik' if grammar >= 60 else '⚠️ Perlu belajar'}</div>
            </div>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown(f"""
            <div class='score-box'>
                <div>📰 Reading</div>
                <div style='font-size: 2rem; font-weight: bold; color: #2ecc71;'>{reading}%</div>
                <div>{'✓ Baik' if reading >= 60 else '⚠️ Perlu belajar'}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 📚 Rekomendasi Belajar Personal")
        rekomendasi = get_rekomendasi(kanji, kosakata, grammar, reading)
        
        if rekomendasi:
            for i, r in enumerate(rekomendasi, 1):
                with st.expander(f"🌿 {r['topik']} - Skor: {r['skor']:.0f}% (Prioritas {i})"):
                    st.markdown(f"💡 **Tips:** {r['tips']}")
                    st.markdown(f"🎯 **Target harian:** {r['daily_target']}")
                    st.markdown("📖 **Sumber belajar:**")
                    for res in r['resources']:
                        st.markdown(f"- {res}")
        else:
            st.success("🎉 Selamat! Semua kategori di atas 60%!")
            st.info("📖 Pertahankan dengan review rutin.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# TAB 2: UPLOAD CSV
# ============================================
with tab2:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown("### 📁 Upload File CSV Hasil Google Form")
    st.markdown(f"""
    **Instruksi:**
    1. Export respons dari Google Form ke CSV
    2. Upload file CSV di bawah
    3. Sistem akan otomatis mengoreksi jawaban
    
    **Kriteria Kelulusan:** Total skor ≥ {TOTAL_SCORE_TARGET} poin
    """)
    
    uploaded_file = st.file_uploader("🌿 Pilih file CSV", type=['csv'], key="csv_uploader")
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success(f"✅ Berhasil membaca {len(df)} responden")
            
            with st.expander("📋 Preview Data"):
                st.dataframe(df.head())
                st.caption(f"Total kolom: {len(df.columns)}")
            
            with st.spinner("🔍 Sedang mengoreksi jawaban..."):
                hasil_koreksi = koreksi_jawaban_csv(df)
            
            st.markdown("---")
            st.markdown("## 📊 Hasil Koreksi dan Prediksi")
            tampilkan_hasil_koreksi(hasil_koreksi)
            
            hasil_df = pd.DataFrame([{
                'Nama': h['nama'],
                'Kanji(%)': h['kanji'],
                'Kosakata(%)': h['kosakata'],
                'Grammar(%)': h['grammar'],
                'Reading(%)': h['reading'],
                'Total_Poin': h['total_poin'],
                'Status': 'Siap' if h['total_poin'] >= TOTAL_SCORE_TARGET else 'Belum Siap'
            } for h in hasil_koreksi])
            
            csv_result = hasil_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                "📥 Download Hasil Prediksi (CSV)",
                csv_result,
                "hasil_prediksi.csv",
                "text/csv",
                key="download_csv"
            )
            
        except Exception as e:
            st.error(f"❌ Error membaca file: {e}")
            st.info("Pastikan file CSV adalah export dari Google Form dengan format yang benar.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================
st.markdown(f"""
<div class='footer'>
    🌿 <strong>JLPT N4 Predictor</strong> | Built with Streamlit & Machine Learning<br>
    Kriteria Kelulusan: Total Skor ≥ {TOTAL_SCORE_TARGET} dari {MAX_SCORE} poin<br>
    Rumus: (Kanji + Kosakata + Grammar + Reading) × 0.3
</div>
""", unsafe_allow_html=True)
