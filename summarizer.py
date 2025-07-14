from langchain_community.document_loaders import WebBaseLoader
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Setup LLM
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama3-8b-8192",
    temperature=0
)

# Load documents from a URL
def load_documents(url):
    loader = WebBaseLoader(url)
    docs = loader.load()
    return docs

# Split documents into chunks
def split_documents(docs, chunk_size=1000, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    split_docs = splitter.split_documents(docs)
    return split_docs

# Summarize using Map-Reduce
def summarize_docs(docs):
    split_docs = split_documents(docs)  # 👈 split here!
    chain = load_summarize_chain(
        llm,
        chain_type="map_reduce",  
        return_intermediate_steps=False
    )

    result = chain.run(split_docs)
    return result
