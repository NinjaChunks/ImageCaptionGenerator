from transformers import GPT2TokenizerFast, ViTImageProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests
import torch
import numpy as np

model_raw = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
image_processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = GPT2TokenizerFast.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

print(model_raw.config)

def generate_caption(image):
    pil_image = Image.open(image)
    pixel_values = image_processor(pil_image, return_tensors="pt").pixel_values
    
    if torch.cuda.is_available():
        pixel_values = pixel_values.cuda()
    
    generated_ids = model_raw.generate(pixel_values, max_new_tokens=30)
    generated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
    return generated_text
