from rank_bm25 import BM25Okapi
import pickle
import os

BM25_PATH = "vectorstore/bm25_index.pkl"

def build_bm25_index(chunks):
    print("🔍 Building BM25 index...")

    tokenized = [doc.page_content.split() for doc in chunks]
    bm25 = BM25Okapi(tokenized)

    with open(BM25_PATH, "wb") as f:
        pickle.dump((bm25, chunks), f)

    print("✅ BM25 index saved!")


def load_bm25_index():
    if not os.path.exists(BM25_PATH):
        raise ValueError("BM25 index not found. Run ingestion again.")

    with open(BM25_PATH, "rb") as f:
        bm25, docs = pickle.load(f)

    return bm25, docs


def bm25_search(query, bm25, docs, top_k=5):
    tokenized_query = query.split()
    scores = bm25.get_scores(tokenized_query)

    ranked = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in ranked[:top_k]]