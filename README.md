# ⚡ VoltMind: LLM Diagnostic Assistant for EV Technicians

VoltMind is an AI-powered EV diagnostic assistant designed to help EV technicians identify and troubleshoot electric vehicle issues using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), FAISS vector search, BM25 retrieval, and automotive manuals.

The system analyzes user-reported EV problems, retrieves relevant information from technical manuals, generates intelligent diagnostics, suggests possible fixes, highlights safety precautions, and provides related repair/tutorial videos.

---

# 🚀 Features

* 🔋 AI-powered EV fault diagnosis
* 🧠 Retrieval-Augmented Generation (RAG)
* ⚡ Hybrid Retrieval (FAISS + BM25)
* 💬 Interactive chatbot interface
* 🎥 YouTube repair/tutorial suggestions
* 📚 Manual-based contextual understanding
* 🛡️ Safety-aware diagnostics
* 🌐 Modern Streamlit web interface

---

# 🧠 Tech Stack

| Component         | Technology             |
| ----------------- | ---------------------- |
| Frontend          | Streamlit              |
| AI Model          | Google Gemini API      |
| Vector Database   | FAISS                  |
| Retrieval         | BM25 + Semantic Search |
| Embeddings        | Sentence Transformers  |
| Backend           | Python                 |
| PDF Processing    | LangChain + PyPDF      |
| Video Suggestions | youtube-search-python  |

---

# 📁 Project Structure

```plaintext
VoltMind-LLM_Diagnostic_Assistant_for_EV_Technicians/
│
├── app/
│   ├── main.py
│   │
│   ├── pipeline/
│   │   ├── ingestion.py
│   │   ├── retriever.py
│   │   ├── generator.py
│   │   └── __init__.py
│   │
│   ├── utils/
│   │   ├── bm25.py
│   │   ├── pdf_loader.py
│   │   ├── text_splitter.py
│   │   ├── youtube_helper.py
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── data/
│   └── manuals/
│       ├── battery/
│       ├── braking/
│       ├── charging/
│       ├── motor/
│       ├── sensors/
│       ├── steering/
│       ├── thermal_management/
│       └── ...
│
├── vectorstore/
│   └── faiss_index/
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# 📚 Dataset / Manuals

Due to size and licensing restrictions, EV manuals are NOT included in this repository.

Create the following folder:

```plaintext
data/manuals/
```

Inside it, organize manuals into categories:

```plaintext
battery/
braking/
charging/
motor/
sensors/
steering/
thermal_management/
power_electronics/
body/
tires/
```

Supported file type:

```plaintext
PDF (.pdf)
```

Example manuals:

* EV battery manuals
* BMS manuals
* Charging system manuals
* Motor/inverter manuals
* Thermal management manuals
* EV troubleshooting guides
* Automotive electrical manuals

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone YOUR_GITHUB_REPO_LINK
cd VoltMind-LLM_Diagnostic_Assistant_for_EV_Technicians
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Gemini API Setup

VoltMind uses the Google Gemini API for AI-generated diagnostics.

---

## 1️⃣ Create Google AI Studio Account

Visit:

[https://aistudio.google.com/](https://aistudio.google.com/)

---

## 2️⃣ Generate API Key

Steps:

1. Sign in with Google
2. Click "Get API Key"
3. Create new API key
4. Copy the generated key

---

## 3️⃣ Create `.env` File

In the root project folder:

```plaintext
VoltMind-LLM_Diagnostic_Assistant_for_EV_Technicians/
```

Create:

```plaintext
.env
```

Inside `.env`:

```env
GEMINI_API_KEY=your_api_key_here
```

⚠️ Never upload `.env` to GitHub.

---

# 📦 Build Vector Database

After adding manuals, generate embeddings and build the FAISS database.

---

## ▶️ Run Ingestion Pipeline

Run the following command:

```bash
python -m app.pipeline.ingestion
```

This process automatically:

* Loads EV manuals from `data/manuals/`
* Splits documents into chunks
* Creates sentence embeddings
* Builds the FAISS vector database
* Builds the BM25 retrieval index
* Saves all indexes locally

---

## 🧠 Expected Console Output

```plaintext
Loading PDFs...
Splitting into chunks...
Creating embeddings...
Building FAISS index...
Saving vectorstore...
Ingestion complete!
Building BM25 index...
BM25 index saved!
```

---

## 📂 Generated Files

The following folders/files will be created automatically:

```plaintext
vectorstore/faiss_index/
```

and BM25 index files inside the project structure.

---

## ⚠️ Important

You only need to run ingestion:

* the first time setup
* after adding new manuals
* after changing datasets

You do NOT need to run ingestion every time you launch the app.

The chatbot directly loads the saved FAISS and BM25 indexes during runtime.

---

# ▶️ Run VoltMind

Start the Streamlit app:

```bash
streamlit run app/main.py
```

Application URL:

```plaintext
http://localhost:8501
```

---

# 💬 Example Queries

## Highway Power Loss

```plaintext
I was driving in hot weather for a long time and suddenly my EV lost power and won’t go above 30 km/h.
```

---

## Charging Failure

```plaintext
My EV charger connects but charging stops after a few minutes.
```

---

## Battery Drain

```plaintext
My EV battery drains very fast overnight even when parked.
```

---

## Motor Noise

```plaintext
I hear a whining noise while accelerating.
```

---

## Thermal Issue

```plaintext
The car reduced performance after heavy traffic driving in hot weather.
```

---

# 🧠 System Workflow

```plaintext
User Query
   ↓
Hybrid Retrieval (FAISS + BM25)
   ↓
Relevant Manual Context
   ↓
Gemini LLM Diagnosis
   ↓
Suggested Fix + Safety Info
   ↓
YouTube Repair Suggestions
```

---

# 🎥 Features Demonstrated

* Context-aware EV diagnostics
* Conversational chatbot support
* AI-generated troubleshooting
* Retrieval from automotive manuals
* Embedded repair/tutorial videos
* Safety-focused recommendations

---

# ⚠️ Important Notes

* Large manuals and vector databases are excluded from GitHub.
* Users must add their own EV manuals.
* First ingestion may take several minutes depending on dataset size.
* Internet connection is required for Gemini API and YouTube suggestions.

---


# 🚀 Future Improvements

* 🎙️ Voice-based diagnostics
* 🌐 Multi-language support
* 📷 OCR/manual image analysis
* 🔧 DTC code interpretation
* 📊 Diagnostic confidence scoring
* ☁️ Cloud deployment
* 📱 Mobile-responsive UI

---

# 👨‍💻 Author

Rahul S

---

# 📜 License

MIT License

---

# ⚡ VoltMind

### “Intelligence Behind Every Volt.”
