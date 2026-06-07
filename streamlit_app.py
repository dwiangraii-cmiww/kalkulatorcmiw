import streamlit as st
import pandas as pd

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="🧪 Kalkulator Kimia Digital",
    page_icon="🧪",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. FUNGSI CACHED (Penting agar tidak load terus-menerus!)
@st.cache_data
def get_chemicals():
    """Load database zat - hanya sekali saat app pertama kali jalan"""
    return {
        "NaCl (Natrium Klorida)": 58.44,
        "KCl (Kalium Klorida)": 74.55,
        "Glukosa (C6H12O6)": 180.16,
        "NaOH (Natrium Hidroksida)": 40.00,
        "HCl (Asam Klorida)": 36.46,
        "H2SO4 (Asam Sulfat)": 98.08,
        "CH3COOH (Asam Asetat)": 60.05,
        "C2H5OH (Etanol)": 46.07,
        "CuSO4 (Tembaga Sulfat)": 159.61,
        "KMnO4 (Kalium Permanganat)": 158.03,
        "Na2CO3 (Natrium Karbonat)": 105.99,
        "NH4Cl (Amonium Klorida)": 53.49
    }

@st.cache_data
def get_periodic_table():
    """Load data tabel periodik - hanya sekali"""
    data = [
        {"No": 1, "Simbol": "H", "Nama": "Hidrogen", "Massa": 1.008, "Jenis": "Non-logam"},
        {"No": 2, "Simbol": "He", "Nama": "Helium", "Massa": 4.003, "Jenis": "Gas Mulia"},
        {"No": 3, "Simbol": "Li", "Nama": "Litium", "Massa": 6.941, "Jenis": "Logam Alkali"},
        {"No": 4, "Simbol": "Be", "Nama": "Berilium", "Massa": 9.012, "Jenis": "Logam Alkali Tanah"},
        {"No": 5, "Simbol": "B", "Nama": "Boron", "Massa": 10.81, "Jenis": "Metalloid"},
        {"No": 6, "Simbol": "C", "Nama": "Karbon", "Massa": 12.011, "Jenis": "Non-logam"},
        {"No": 7, "Simbol": "N", "Nama": "Nitrogen", "Massa": 14.007, "Jenis": "Non-logam"},
        {"No": 8, "Simbol": "O", "Nama": "Oksigen", "Massa": 15.999, "Jenis": "Non-logam"},
        {"No": 9, "Simbol": "F", "Nama": "Fluor", "Massa": 18.998, "Jenis": "Halogen"},
        {"No": 10, "Simbol": "Ne", "Nama": "Neon", "Massa": 20.180, "Jenis": "Gas Mulia"},
        {"No": 11, "Simbol": "Na", "Nama": "Natrium", "Massa": 22.990, "Jenis": "Logam Alkali"},
        {"No": 12, "Simbol": "Mg", "Nama": "Magnesium", "Massa": 24.305, "Jenis": "Logam Alkali Tanah"},
        {"No": 13, "Simbol": "Al", "Nama": "Aluminium", "Massa": 26.982, "Jenis": "Logam Post-Transisi"},
        {"No": 14, "Simbol": "Si", "Nama": "Silikon", "Massa": 28.086, "Jenis": "Metalloid"},
        {"No": 15, "Simbol": "P", "Nama": "Fosfor", "Massa": 30.974, "Jenis": "Non-logam"},
        {"No": 16, "Simbol": "S", "Nama": "Belerang", "Massa": 32.065, "Jenis": "Non-logam"},
        {"No": 17, "Simbol": "Cl", "Nama": "Klorin", "Massa": 35.453, "Jenis": "Halogen"},
        {"No": 18, "Simbol": "Ar", "Nama": "Argon", "Massa": 39.948, "Jenis": "Gas Mulia"},
        {"No": 19, "Simbol": "K", "Nama": "Kalium", "Massa": 39.098, "Jenis": "Logam Alkali"},
        {"No": 20, "Simbol": "Ca", "Nama": "Kalsium", "Massa": 40.078, "Jenis": "Logam Alkali Tanah"},
        {"No": 26, "Simbol": "Fe", "Nama": "Besi", "Massa": 55.845, "Jenis": "Logam Transisi"},
        {"No": 29, "Simbol": "Cu", "Nama": "Tembaga", "Massa": 63.546, "Jenis": "Logam Transisi"},
        {"No": 30, "Simbol": "Zn", "Nama": "Seng", "Massa": 65.38, "Jenis": "Logam Transisi"},
        {"No": 47, "Simbol": "Ag", "Nama": "Perak", "Massa": 107.868, "Jenis": "Logam Transisi"},
        {"No": 79, "Simbol": "Au", "Nama": "Emas", "Massa": 196.967, "Jenis": "Logam Transisi"},
    ]
    return pd.DataFrame(data)

# 3. INISIALISASI SESSION STATE (Menyimpan hasil perhitungan)
if 'result_prep' not in st.session_state:
    st.session_state.result_prep = None
if 'result_dil' not in st.session_state:
    st.session_state.result_dil = None
if 'result_dil_air' not in st.session_state:
    st.session_state.result_dil_air = None

# 4. TAMPILAN UTAMA
st.title("🧪 Kalkulator Kimia Digital")
st.markdown("---")

# Load data sekali saja
chemicals = get_chemicals()
df_periodik = get_periodic_table()

# Pilih Tab
tab1, tab2, tab3 = st.tabs(["💧 Pembuatan Larutan", "💧 Pengenceran", "📘 Tabel Periodik"])

# ==================== TAB 1: PEMBUATAN LARUTAN ====================
with tab1:
    st.header("Pembuatan Larutan")
    st.markdown("**Rumus: massa = M × V × Mr**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        selected_chem = st.selectbox(
            "Pilih Zat Terlarut", 
            options=list(chemicals.keys()),
            key="chem_select"
        )
        mr_val = chemicals[selected_chem]
        st.metric("Mr (Massa Molar)", f"{mr_val} g/mol")
        
    with col2:
        vol_ml = st.number_input("Volume (mL)", min_value=1.0, value=100.0, key="vol_ml_input")
        conc_m = st.number_input("Konsentrasi (M)", min_value=0.0001, value=0.1, step=0.1, format="%.4f", key="conc_m_input")

    if st.button("✅ Hitung Massa", type="primary", key="btn_calc_mass"):
        vol_l = vol_ml / 1000
        massa = conc_m * vol_l * mr_val
        st.session_state.result_prep = massa

    # Tampilkan hasil jika ada
    if st.session_state.result_prep is not None:
        st.success(f"⚖️ **Massa yang ditimbang: {st.session_state.result_prep:.4f} gram**")

# ==================== TAB 2: PENGENCERAN ====================
with tab2:
    st.header("Pengenceran Larutan")
    st.markdown("**Rumus: C₁V₁ = C₂V₂**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        c1 = st.number_input("Konsentrasi Stok (M)", min_value=0.01, value=1.0, format="%.2f", key="c1_input")
        
    with col2:
        c2 = st.number_input("Konsentrasi Target (M)", min_value=0.0001, value=0.1, format="%.4f", key="c2_input")
        
    v2 = st.number_input("Volume Target (mL)", min_value=1.0, value=100.0, step=10.0, key="v2_input")

    if st.button("✅ Hitung Volume", type="primary", key="btn_calc_dil"):
        if c1 <= c2:
            st.error("❌ Konsentrasi stok harus lebih besar dari target!")
        else:
            v1 = (c2 * v2) / c1
            air_tambah = v2 - v1
            st.session_state.result_dil = v1
            st.session_state.result_dil_air = air_tambah

    # Tampilkan hasil
    if st.session_state.result_dil is not None:
        st.success(f"📦 Ambil Volume Stok (V₁): **{st.session_state.result_dil:.2f} mL**")
        st.info(f"💧 Tambahkan air: **{st.session_state.result_dil_air:.2f} mL**")

# ==================== TAB 3: TABEL PERIODIK ====================
with tab3:
    st.header("Tabel Periodik Unsur")
    
    # Filter pencarian
    search = st.text_input("🔍 Cari Unsur (Nama/Simbol/No Atom)", placeholder="Contoh: Besi, Fe, atau 26")
    
    if search:
        filtered = df_periodik[
            df_periodik['Nama'].str.contains(search, case=False) | 
            df_periodik['Simbol'].str.contains(search, case=False) |
            df_periodik['No'].astype(str).str.contains(search)
        ]
    else:
        filtered = df_periodik
    
    # Tampilkan tabel dengan styling
    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True
    )
    
    st.caption(f"Menampilkan {len(filtered)} unsur dari {len(df_periodik)} total")

# 5. Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>🧪 Kalkulator Kimia Digital v1.0</div>", unsafe_allow_html=True)
