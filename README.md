# 📚 Context-Aware RAG Chatbot

A **Retrieval-Augmented Generation (RAG)** chatbot built using **LangChain**, **OpenAI**, and **FAISS**, designed to answer user questions with contextual awareness based on a custom document corpus. The chatbot maintains conversational memory and provides accurate responses grounded in uploaded knowledge.
---

## 🚀 Features

- 🔍 **Contextual QA:** Uses custom documents to give relevant answers
- 💬 **Conversational Memory:** Remembers past interactions during a session
- 🔗 **Retrieval-Augmented Generation:** Combines LLM with vector search
- 🧠 **FAISS Vector Store:** For fast and accurate document retrieval
- 🖥️ **Interactive UI:** Built with Streamlit, responsive and user-friendly
- 📑 **Sidebar Info Panel:** About, tech stack, and trained topics

---

## 🧠 Tech Stack

- **Model:** GPT (gpt-3.5-turbo via OpenAI)
- **Vector Store:** FAISS (custom document embedding index)
- **Embeddings:** OpenAIEmbeddings (text-embedding-ada-002)
- **Frameworks:** LangChain, Python 3.11
- **Memory:** ConversationBufferMemory (LangChain)
- **UI:** Streamlit
- **Data Source:** Custom uploaded document corpus

---

## 📘 Trained Topics

This chatbot is trained to answer questions on:

- 📌 Artificial Intelligence  
- 📌 Climate Change  
- 📌 Quantum Computing  
- 📌 Electric Vehicles  
- 📌 Human Microbiome  
- 📌 Cybersecurity  
- 📌 Machine Learning  
- 📌 Space Exploration  
- 📌 Renewable Energy  
- 📌 Crypto Currency  
- 📌 Mental Health  
- 📌 Remote Work  
- 📌 Blockchain  
- 📌 Augmented Reality  
- 📌 Nutrition and Health  

---
## Project Structure

├── app.py                  # Streamlit main app
├── faiss_index/            # Precomputed FAISS vector store
├── .env                    # API keys and secrets
├── requirements.txt        # Python dependencies
└── README.md               # Project description

---
## 🛠️ Setup Instructions

1. **Clone the repository**
git clone https://github.com/your-username/context-aware-chatbot.git
cd context-aware-chatbot

2. **Create a .env file**
OPENAI_API_KEY=your_openai_key_here

