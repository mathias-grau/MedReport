import os
import torch

class Config:
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

    # For QA
    QA_MODEL_NAME = "etalab-ia/camembert-base-squadFR-fquad-piaf"
    TOKENIZER_NAME = "camembert-base"

    SUMMARIZATION_MODEL_NAME = "meta-llama/Llama-3.2-3B-Instruct"

    # Device for PyTorch
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
