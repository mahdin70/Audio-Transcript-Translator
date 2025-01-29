import streamlit as st
from transcriber import transcribe_audio
from translator import translate_text

st.set_page_config(page_title="AI Powered Transcript Translator", layout="centered")
st.markdown("<h2 style='text-align: center;'>🎙️ AI Powered Transcript Translator</h2>", unsafe_allow_html=True)

if "transcript" not in st.session_state:
    st.session_state.transcript = None

if "translated_text" not in st.session_state:
    st.session_state.translated_text = None

uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if uploaded_file:
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button("Transcribe", use_container_width=True):
            with st.spinner("Transcribing..."):
                st.session_state.transcript = transcribe_audio(uploaded_file)
                st.session_state.translated_text = None 

if st.session_state.transcript:
    if not st.session_state.transcript.startswith("Error"):
        st.subheader("Transcribed Text")
        st.markdown(
            f"<div style='border: 2px solid #4CAF50; padding: 10px; border-radius: 5px; margin-bottom: 30px;'>"
            f"{st.session_state.transcript}"
            f"</div>",
            unsafe_allow_html=True,
        )

        target_language = st.selectbox("Select a language to translate", ["Bangla", "Hindi", "Spanish", "German"], key="language_select")

        col1, col2, col3 = st.columns([2, 1, 2])
        with col2:
            if st.button("Translate", use_container_width=True):
                with st.spinner("Translating..."):
                    st.session_state.translated_text = translate_text(st.session_state.transcript, target_language)

        if st.session_state.translated_text:
            st.subheader("Translated Text")
            st.markdown(
                f"<div style='border: 2px solid #2196F3; padding: 10px; border-radius: 5px;'>"
                f"{st.session_state.translated_text}"
                f"</div>",
                unsafe_allow_html=True,
            )
    else:
        st.error(st.session_state.transcript) 
