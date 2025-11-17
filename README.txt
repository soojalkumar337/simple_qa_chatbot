Simple LangChain Chatbot with Groq API 

This project is a simple yet powerful chatbot application built using Streamlit, LangChain, and Groq API.
It demonstrates how to integrate LLMs (LLaMA-3.1 8B Instant) using the langchain_groq package, and how to build a clean conversational UI with Streamlit.

The project is packaged and run using uv (Astral’s ultra-fast Python package manager).

🚀 Features

🔹 Streamlit-based web UI

🔹 LangChain prompt template

🔹 ChatGroq LLaMA-3.1 model integration

🔹 .env support for API keys

🔹 Clean and minimal chatbot workflow

🔹 Runs using uv instead of pip/venv

📂 Project Structure
project/
│── simple_qa_chatbot.py
│── .env
│── uv.lock
│── pyproject.toml
│── README.md

🔧 Installation & Setup (Using uv)
1️⃣ Install uv (if not installed)
pip install uv

2️⃣ Clone the Repository
git clone https://github.com/soojalkumar337/simple_qa_chatbot.git
cd simple_qa_chatbot

3️⃣ Create .env File

Inside the project folder create a .env file and add:

GROQ_API_KEY=your_api_key_here


5️⃣ Start the App
uv run streamlit run app.py

▶️ Usage

Run the application.

A browser window will open with the chatbot interface.

Type any question or prompt.

The chatbot responds using Groq LLaMA-3.1 model.

🧠 How It Works

The app loads environment variables using dotenv.

A LangChain prompt template is created:

system message (rules for the model)

user message (input field)

The ChatGroq LLM is initialized with the model:

llama-3.1-8b-instant


A chain is formed using:
Prompt → LLM → OutputParser

Streamlit displays the result in the UI.


🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you'd like to change.