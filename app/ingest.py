from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from .config import (
    DOCS_DIR,
    CHROMA_DIR,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    EMBEDDING_MODEL_NAME,
)

def load_documents(doc_dir: Path):
    """
    Load all .txt and .md files from doc_dir as LangChain Documents.
    """
    docs = []
    for path in doc_dir.rglob("*"):
        if path.suffix.lower() not in {".txt", ".md"}:
            continue
        loader = TextLoader(str(path), encoding="utf-8")
        file_docs = loader.load()
        # Attach source metadata (file path)
        for d in file_docs:
            d.metadata["source"] = str(path.relative_to(doc_dir))
        docs.extend(file_docs)
    return docs


def chunk_documents(documents):
    """
    Smart document chunking with overlap to preserve context.
    Uses RecursiveCharacterTextSplitter which respects sentence boundaries
    where possible.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        add_start_index=True,
    )
    return splitter.split_documents(documents)


def build_vector_store(chunks):
    """
    Build (or rebuild) a Chroma vector store from document chunks.
    """
    # Embedding model from HuggingFace (Sentence-Transformers)
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    # Remove existing DB if you want a clean rebuild
    if CHROMA_DIR.exists():
        print(f"[INFO] Removing existing Chroma DB at: {CHROMA_DIR}")
        for item in CHROMA_DIR.iterdir():
            if item.is_file():
                item.unlink()
            else:
                # Just in case there are subdirs
                for sub in item.rglob("*"):
                    if sub.is_file():
                        sub.unlink()
                item.rmdir()

    print("[INFO] Creating new Chroma vector store...")
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),
    )
    print(f"[INFO] Chroma DB automatically persisted to: {CHROMA_DIR}")
    return vectordb


def main():
    print(f"[INFO] Using docs directory: {DOCS_DIR}")
    print(f"[INFO] Using embedding model: {EMBEDDING_MODEL_NAME}")

    if not DOCS_DIR.exists():
        raise FileNotFoundError(
            f"Docs directory not found: {DOCS_DIR}. "
            "Create it and add some .txt/.md files."
        )

    docs = load_documents(DOCS_DIR)
    print(f"[INFO] Loaded {len(docs)} document(s).")

    chunks = chunk_documents(docs)
    print(f"[INFO] Split into {len(chunks)} chunk(s).")
    print(f"[INFO] Example chunk:\n{chunks[0].page_content[:300]}...\n")

    build_vector_store(chunks)
    print("[INFO] Ingestion completed successfully.")


if __name__ == "__main__":
    main()
