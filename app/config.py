from pathlib import Path
import os

# --- Paths ---
BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "data" / "docs"
CHROMA_DIR = BASE_DIR / "chroma_db"

# --- Chunking parameters ---
CHUNK_SIZE = 500        # ~500 characters, balanced
CHUNK_OVERLAP = 100     # 20% overlap to preserve context

# --- Embedding models ---
# High-accuracy model (slower, 768 dims)
MPNET_MODEL = "sentence-transformers/all-mpnet-base-v2"
# Fast model (384 dims)
MINILM_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Default model can be overridden via env var: EMBEDDING_MODEL
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL", MPNET_MODEL)

# --- Other ---
TOP_K_RESULTS = 5
