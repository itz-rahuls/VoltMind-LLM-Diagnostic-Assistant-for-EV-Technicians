from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from utils.bm25 import load_bm25_index, bm25_search

DB_PATH = "vectorstore/faiss_index"


def load_faiss():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    return FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)


def remove_duplicates(docs):
    seen = set()
    unique = []

    for doc in docs:
        if doc.page_content not in seen:
            unique.append(doc)
            seen.add(doc.page_content)

    return unique


def hybrid_search(query, k=5):
    print("🧠 Loading FAISS...")
    db = load_faiss()

    print("🔍 Loading BM25...")
    bm25, docs = load_bm25_index()

    print("⚡ Running FAISS search...")
    faiss_results = db.similarity_search(query, k=k)

    print("⚡ Running BM25 search...")
    bm25_results = bm25_search(query, bm25, docs, top_k=k)

    combined = faiss_results + bm25_results

    # remove duplicates
    unique_docs = remove_duplicates(combined)

    return unique_docs[:k]