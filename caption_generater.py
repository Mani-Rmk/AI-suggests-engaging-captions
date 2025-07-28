from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import google.generativeai as genai
import os
import re

#API key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))


# Load model and processor from Hugging Face
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

def load_image(image_source):
    return Image.open(image_source).convert('RGB')

def generate_captions(image):
  inputs=processor(image,return_tensors="pt")
  out=model.generate(**inputs)
  caption=processor.decode(out[0],skip_special_tokens=True)
  return caption

def rewrite_caption(base_caption, style):
    prompt = f"""Rewrite the following image description into a {style} travel caption. 
Make it suitable for sharing on social media. Be vivid, expressive, and aligned to the style.

Image description: "{base_caption}"

Caption:
#Output: return only best 2 captions
"""
    response = gemini_model.generate_content(prompt, generation_config={
        "temperature": 0.2,
        "max_output_tokens": 500
    })

    # Clean and split into captions
    text = response.text.strip()
    captions = []

    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue

        # Remove labels like "Caption 1:", "Option 2:", "1.", etc.
        cleaned = re.sub(r"^(caption|option)?\s*\d+[:.\-]?\s*", "", line, flags=re.IGNORECASE).strip()
        if cleaned:
            captions.append(cleaned)

    # Fallback if not formatted as expected
    if len(captions) < 2:
        fallback = [l.strip() for l in text.split("\n") if l.strip()]
        captions = fallback[:2]

    return captions

