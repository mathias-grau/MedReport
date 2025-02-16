# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-3B", cache_dir="./")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-3B", cache_dir="./")