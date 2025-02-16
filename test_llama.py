import torch
from transformers import pipeline

model_path = "./models--meta-llama--Llama-3.2-3B/snapshots/13afe5124825b4f3751f836b40dafda64c1ed062"  # Adjust this path if needed

pipe = pipeline(
    "text-generation",
    model=model_path,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

response = pipe("The key to life is", max_length=50)  # Adjust max_length as needed
print(response)
