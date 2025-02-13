import os

class Config:
    # Example: can be overridden by environment variables
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

    # For QA
    QA_MODEL_NAME = "etalab-ia/camembert-base-squadFR-fquad-piaf"  # or environment variable
    TOKENIZER_NAME = "etalab-ia/camembert-base-squadFR-fquad-piaf"

    # For Summarization
    SUMMARIZATION_MODEL_NAME = "facebook/bart-large-cnn"

    # Device for PyTorch
    # In many production setups, you might want to do detection automatically (CPU or GPU).
    # Or set an env variable like 'CPU' or 'CUDA'.
    import torch
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
