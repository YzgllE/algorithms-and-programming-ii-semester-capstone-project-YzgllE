
import streamlit as st
from algorithm import rabin_karp
from utils import highlight_text

st.title("🔍 Rabin-Karp String Matching Visualizer")

text = st.text_area("Metin (Text):", "ABABDABACDABABCABAB")
pattern = st.text_input("Desen (Pattern):", "ABABC")

if st.button("Eşleşmeleri Göster"):
    if pattern and text:
        matches, steps = rabin_karp(text, pattern)

        st.subheader("🧮 Adım Adım İşleyiş")
        for step in steps:
            st.code(
                f"İndeks {step['index']}: '{step['window']}' | Hash: {step['current_hash']} | {'✔️ Eşleşme' if step['match'] else '❌'}"
            )

        st.subheader("✅ Eşleşme Sonuçları")
        if matches:
            for idx in matches:
                st.markdown(highlight_text(text, idx, len(pattern)))
        else:
            st.warning("Eşleşme bulunamadı.")

