# 🏞️ Travel Image Caption Generator using BLIP + Gemini

This project uses **BLIP** (Bootstrapped Language-Image Pretraining) to generate image captions, then **Gemini 1.5 Flash** to rewrite those captions in a specific **social media style**. It's perfect for creating Instagram-worthy travel posts from your photos.

The app supports:

- Generating image captions using a vision-language model (`Salesforce/blip-image-captioning-base`)
- Rewriting them in expressive styles like poetic, minimalist, or influencer-style
- Streamlit UI for easy user interaction (if running frontend)

---

## 🧠 How It Works

1. Upload an image of your travel moment.
2. BLIP generates a base caption from the photo.
3. Gemini rewrites the caption into your chosen social media style.
4. You get the **top 2 rewritten captions** ready to post.

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Mani-Rmk/AI-suggests-engaging-captions.git
cd AI-suggests-engaging-captions
# Step 2–4: Setup environment, install dependencies, and set API key
python -m venv venv && \
source venv/bin/activate && \
pip install -r requirements.txt && \
echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env
