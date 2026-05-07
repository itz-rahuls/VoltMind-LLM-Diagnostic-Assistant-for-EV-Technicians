from langchain_community.document_loaders import PyPDFLoader
import os

def load_pdfs_from_folder(folder_path):
    documents = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pdf"):
                path = os.path.join(root, file)

                try:
                    loader = PyPDFLoader(path)
                    docs = loader.load()

                    for doc in docs:
                        doc.metadata["source"] = file
                        doc.metadata["folder"] = os.path.basename(root)

                    documents.extend(docs)

                except Exception as e:
                    print(f"❌ Skipped {file} due to error: {e}")

    return documents