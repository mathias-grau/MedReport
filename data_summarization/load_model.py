from transformers import AutoTokenizer, AutoModelForCausalLM

# Specify the model name and target directory (current directory in this case)
model_name = "SumayyaAli/tiny-llama-1.1b-chat-medical"
cache_dir = "./"  # Current directory

# Download the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_dir)

print("Model and tokenizer downloaded successfully.")
