# 🤖 AI-Powered Pdf & CSV Q&A Chatbot

This is an AI-powered application that allows you to interact with structured CSV data and receive intelligent answers in natural language using LLaMA3 (via Groq), LangChain, and vector search. Built with a clean Streamlit interface for easy use.

---

## 🚀 Features

- 🧠 Uses **LLaMA** model via **Groq API**
- 📊 Upload and query structured data from a CSV file (`product.csv`)
- 💬 Chat-style Q&A interface powered by **LangChain**
- 🔎 Semantic search using **HuggingFace embeddings** and **ChromaDB**
- 🖥️ Simple and interactive **Streamlit UI**

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **LLM**: Groq LLaMA3
- **Framework**: LangChain
- **Embeddings**: HuggingFace (MiniLM)
- **Vector DB**: Chroma
- **Environment Management**: dotenv
- **Data**: CSV file (`data/product.csv`)

---

## 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/hemantkumarlearning/AI-File-Retrieval-Chatbot.git
cd AI-File-Retrieval-Chatbot
```

2. **Install dependencies**

```
pip install -r requirements.txt
```

3. **Add your API key**

Create a .env file in the root directory and add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```
4. **Run the app**

```
streamlit run app.py
```

## Demo
