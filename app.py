import streamlit as st
import time

# ==========================
# KONFIGURASI HALAMAN
# ==========================
st.set_page_config(
    page_title="Fibonacci Visualizer",
    page_icon="🔢",
    layout="centered"
)

# ==========================
# CSS LIGHT MODE
# ==========================
st.markdown("""
<style>
body {
    background-color: #ffffff;
    color: #000000;
}
.main-title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: #2c7be5;
}
.sub-title {
    text-align: center;
    font-size: 18px;
    color: #555555;
}
.card {
    background-color: #f5f7fa;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    margin-top: 20px;
}
.box {
    display: inline-block;
    padding: 12px 16px;
    margin: 6px;
    border-radius: 10px;
    background-color: #e9ecef;
    font-weight: bold;
}
.active {
    background-color: #ffb703;
    color: #000;
}
.result {
    background-color: #2ea44f;
    color: #fff;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# JUDUL
# ==========================
st.markdown("<div class='main-title'>🔢 Fibonacci Visualizer</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Visualisasi pembentukan deret Fibonacci</div>", unsafe_allow_html=True)

# ==========================
# INPUT
# ==========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    n = st.slider("📌 Pilih jumlah suku Fibonacci", 2, 15, 8)
    start = st.button("🚀 Tampilkan Fibonacci")

    st.markdown("</div>", unsafe_allow_html=True)

# ==========================
# PROSES FIBONACCI
# ==========================
if start:
    st.markdown("### 🔄 Proses Perhitungan")

    fib = [0, 1]
    container = st.empty()

    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])

        with container:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            for j, val in enumerate(fib):
                if j == i:
                    st.markdown(
                        f"<span class='box active'>{val}</span>",
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"<span class='box'>{val}</span>",
                        unsafe_allow_html=True
                    )
            st.markdown("</div>", unsafe_allow_html=True)

        time.sleep(0.7)

    # ==========================
    # HASIL AKHIR
    # ==========================
    st.markdown("### ✅ Hasil Akhir")

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    for val in fib:
        st.markdown(
            f"<span class='box result'>{val}</span>",
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)

    st.info(f"📍 Nilai Fibonacci ke-{n} adalah **{fib[n - 1]}**")
