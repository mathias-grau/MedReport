# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForQuestionAnswering
from config import Config

tokenizer = AutoTokenizer.from_pretrained(Config.SUMMARIZATION_MODEL_NAME, cache_dir='./')    
model = AutoModelForCausalLM.from_pretrained(Config.SUMMARIZATION_MODEL_NAME, cache_dir='./').to(Config.DEVICE)

tokenizer = AutoTokenizer.from_pretrained(Config.TOKENIZER_NAME, cache_dir='./')
model = AutoModelForQuestionAnswering.from_pretrained(Config.QA_MODEL_NAME, cache_dir='./').to(Config.DEVICE)