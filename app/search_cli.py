from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from .config import (
    CHROMA_DIR,
    EMBEDDING_MODEL_NAME,
    TOP_K_RESULTS,
)


def load_vector_store():
    """
    Load an existing Chroma vector store.
    """
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    vectordb = Chroma(
        embedding_function=embeddings,
        persist_directory=str(CHROMA_DIR),
    )
    return vectordb


def interactive_search():
    print("=== TechDocs Semantic Search ===")
    print(f"Embedding model: {EMBEDDING_MODEL_NAME}")
    print("Type 'exit' or 'quit' to leave.\n")

    vectordb = load_vector_store()

    while True:
        query = input("Search query> ").strip()
        if query.lower() in {"exit", "quit"}:
            print("Bye!")
            break

        if not query:
            continue

        # similarity_search_with_score returns (Document, score) pairs
        raw_results = vectordb.similarity_search_with_score(query, k=TOP_K_RESULTS)

        # Filter results by score threshold
        SCORE_THRESHOLD = 1.0
        results = [(doc, score) for doc, score in raw_results if score <= SCORE_THRESHOLD]


        print("\n--- Top Results ---")
        for i, (doc, score) in enumerate(results, start=1):
            source = doc.metadata.get("source", "unknown")
            print(f"\n[{i}] Score: {score:.4f} | Source: {source}")
            print("-" * 60)
            # Show small snippet
            content = doc.page_content.strip().replace("\n", " ")
            print(content[:500] + ("..." if len(content) > 500 else ""))
        print("\n")


def main():
    if not CHROMA_DIR.exists():
        raise SystemExit(
            f"ERROR: No Chroma DB found at {CHROMA_DIR}. "
            "Run the ingestion script first: `python -m app.ingest`"
        )

    interactive_search()


if __name__ == "__main__":
    main()
