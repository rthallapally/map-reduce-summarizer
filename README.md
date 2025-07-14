# 📄 Map-Reduce Summarizer with Groq + LangChain

This project is a webpage summarizer that uses LangChain’s map-reduce summarization chain, powered by Groq’s Llama3 LLM, and wrapped in a Streamlit web app.

You input a URL, and it fetches the page, splits it into chunks, summarizes each chunk, and then reduces those summaries into a concise final summary.

# 🚀 Features

Summarizes long webpages (like blogs, papers, articles) using map-reduce strategy.

Uses Groq LLM (llama3-8b-8192) for fast, cost-efficient inference.

Chunking of large text to avoid exceeding model context limits.

Streamlit UI for easy interaction.

.env support to keep your API keys secure.

# 📂 Project Structure
.
├── app.py                # Streamlit app
├── summarizer.py         # Core summarization logic
├── .env                  # (Not tracked) Your API keys
├── .gitignore            # Ignore sensitive & unnecessary files
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

# 🔧 Installation

1️⃣ Clone the repository

git clone <your-repo-url>

cd map-reduce-summarizer

2️⃣ Create and activate a virtual environment

python -m venv venv

venv\Scripts\activate          # Windows

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Add your Groq API key

Create a .env file in the root folder:

GROQ_API_KEY=your_groq_api_key_here

# 📝 Usage

Run the app:

streamlit run app.py

# Steps

1️⃣ Open the Streamlit app in your browser.

2️⃣ Enter a URL to a webpage (e.g. blog post or article).

3️⃣ The app will load the webpage, chunk it, summarize each chunk (map), and combine those into a final summary (reduce).

4️⃣ Read and review the summary on the page.


# 📜 Techniques Used

🔷 Map-Reduce Summarization

Map step: Each document chunk is summarized independently.

Reduce step: Partial summaries are combined into the final result.

This is more scalable than stuffing all text into one prompt, and avoids hitting token limits.


🔷 Tools & Libraries

LangChain – LLM orchestration & summarization chains.

Groq – Ultra-fast inference with Llama3.

Streamlit – Interactive web app.

BeautifulSoup – (via LangChain) for scraping content.

# ⚠️ Notes
Some very large pages may still exceed Groq’s token limits — you can reduce chunk_size in summarizer.py if needed.

.env is ignored in .gitignore. Never push your API keys to GitHub.

Tested with Groq llama3-8b-8192.
