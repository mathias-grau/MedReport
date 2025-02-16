from PIL import Image
import pytesseract
image = Image.open('./data/exemple.png')
text = pytesseract.image_to_string( image )
print(text)

from huggingface_hub import whoami

print(whoami())  # Should display your Hugging Face account details

import torch
from transformers import pipeline

model_id = "meta-llama/Llama-3.2-1B"

pipe = pipeline(
    "text-generation", 
    model=model_id, 
    torch_dtype=torch.bfloat16, 
    device_map="auto"
)

pipe("The key to life is")
