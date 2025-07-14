import streamlit as st
from summarizer import load_documents, summarize_docs

st.title("📄 Map-Reduce Summarizer with Groq + LangChain")

url = st.text_input("Enter a webpage URL to summarize:")

if url:
    st.write("🔄 Loading and summarizing...")
    docs = load_documents(url)
    summary = summarize_docs(docs)
    st.markdown("## 📝 Summary:")
    st.write(summary)
