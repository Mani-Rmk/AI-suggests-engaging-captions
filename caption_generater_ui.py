import streamlit as st
from caption_generater import load_image, generate_captions, rewrite_caption

st.set_page_config(page_title="AI Travel Caption Generator", layout="centered")

st.title("✈️ Travel Image Caption Generator")
st.markdown("Upload your travel photo and select a caption style. Let AI turn your moment into magic!")

uploaded_file = st.file_uploader("📤 Upload a travel image", type=["jpg", "png"])

if uploaded_file:
    image = load_image(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    style = st.selectbox("🎨 Choose caption style:", ["poetic", "funny", "romantic", "adventurous"])

    if st.button("✨ Generate Captions"):
        with st.spinner("Generating with AI..."):
            base_caption = generate_captions(image)
            final_caption = rewrite_caption(base_caption, style)
            st.success("Here are your AI captions:")

            # Split into 2 captions if separated by newline or numbering
            for i, cap in enumerate(final_caption, start=1):
                st.markdown(f"**Caption {i}:** {cap}")

