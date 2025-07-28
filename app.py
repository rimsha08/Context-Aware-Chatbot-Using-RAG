import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Load FAISS vectorstore
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# Streamlit page config
st.set_page_config(page_title="Context-Aware RAG Chatbot", layout="wide")

# ---------- SIDEBAR (Left Panel) ----------
with st.sidebar:
    st.markdown("### 🤖 About the Chatbot")
    st.markdown("This **Context-Aware RAG Chatbot** uses Retrieval-Augmented Generation (RAG) to give accurate, context-aware answers using memory and a custom document store.")

    st.markdown("---")

    st.markdown("### 🧠 Tech Stack")
    st.markdown("""
    - **Model:** GPT (gpt-3.5-turbo via OpenAI)
    - **Vector Store:** FAISS (custom document embedding index)
    - **Embeddings:** OpenAIEmbeddings (text-embedding-ada-002)
    - **Frameworks:** LangChain, Python 3.11
    - **Memory:** ConversationBufferMemory (LangChain)
    - **UI:** Streamlit
    - **Data Source:** Custom uploaded document corpus
    """)

    st.markdown("---")

    st.markdown("### 📘 Trained Topics")
    topics = [
        "Artificial Intelligence", "Climate Change", "Quantum Computing", "Electric Vehicles",
        "Human Microbiome", "Cybersecurity", "Machine Learning", "Space Exploration",
        "Renewable Energy", "Crypto Currency", "Mental Health", "Remote Work",
        "Blockchain", "Augmented Reality", "Nutrition and Health"
    ]

    for topic in topics:
        st.markdown(f"📌 {topic}")


# ---------- MAIN CHATBOT UI ----------
st.title("📚 Context-Aware RAG Chatbot")

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

    st.session_state.qa_chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(temperature=0),
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        memory=st.session_state.memory,
        return_source_documents=True,
        output_key="answer",
    )

st.markdown("#### 🗨️ Ask me anything about the trained topics below:")

user_input = st.text_input("Your Question")

if user_input:
    result = st.session_state.qa_chain({"question": user_input})
    st.markdown(f"**🧠 Bot:** {result['answer']}")


