# E-commerce AI Agent: Natural Language to SQL Analytics

Welcome to the E-commerce AI Agent! This project connects a Large Language Model (LLM) to your e-commerce database, enabling anyone to ask questions in plain English and receive answers powered by live SQL over your data.

## 📋 Project Overview

- **Goal:** Let users get insights from their e-commerce data simply by asking questions—no SQL knowledge required.
- **How it works:**
  1. User enters a question in a web interface or sends it to an API endpoint.
  2. The backend sends the question and a description of your DB schema to a local LLM (runs on Ollama).
  3. The LLM returns a SQL query.
  4. The FastAPI backend runs this SQL on your SQLite database and returns the result to the user.

- **Tech Stack:**
  - Python (FastAPI, SQLAlchemy, Pandas)
  - SQLite (pre-loaded with your e-commerce data)
  - Ollama + LLM (Llama 3.2, Gemma, DeepSeek—choose your model)
  - HTML/JavaScript frontend
  - Runs fully locally and offline.

## 🚀 Features

- **Ask in plain English:** e.g., "What is my total sales?", "Which product had the highest CPC?"
- **No SQL needed:** The AI generates queries for you.
- **Works locally:** No data leaves your machine.
- **Web UI:** Minimal, user-friendly web form included.
- **API:** FastAPI `/ask` endpoint for programmatic access.
- **Compatible with recent open models:** Llama 3, DeepSeek, Gemma, etc.

## 🏁 How to Deploy & Run the Project

### 1. **Clone This Repository**

```sh
git clone https://github.com/yourusername/ecommerce-ai-agent.git
cd ecommerce-ai-agent
```

### 2. **(Optional) Set Up Python Virtual Environment**

**Note:** Never upload your `venv` folder to GitHub. Each user creates it locally.

```sh
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. **Install Requirements**

```sh
pip install -r requirements.txt
```
*(includes fastapi, pandas, sqlalchemy, jinja2, requests, and any other needed packages)*

### 4. **Download or Generate the Database**

- Your SQLite DB (`ecommerce.db`) should be in the `/data` folder.
- If needed, follow project instructions or run scripts in `/scripts` to convert CSVs to SQLite.

### 5. **Install and Start Ollama (LLM Engine)**

- Download Ollama from [https://ollama.com/](https://ollama.com/) and install for your OS.
- Pull your desired model (e.g., Llama 3.2):
  ```sh
  ollama pull llama3.2
  ```
- Start the Ollama server:
  ```sh
  ollama serve
  ```
- The server runs at `http://127.0.0.1:3000` by default.

### 6. **Run the FastAPI App**

**Recommended:**
```sh
uvicorn main:app --reload
# or
python -m uvicorn main:app --reload
```

- The API server will be available at [http://localhost:8000/](http://localhost:8000/)

### 7. **Use the Web Interface**

Open your browser and go to:
```
http://127.0.0.1:8000/
```
- Enter your analytical question.
- View SQL and answer returned below.

### 8. **Or Use the API Directly**

Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Send a POST to `/ask` with:
```json
{
  "question": "What is my total sales?"
}
```

## 🛠 Project Structure

| File/Folder                  | Purpose                              |
|------------------------------|--------------------------------------|
| `main.py`                    | FastAPI backend & API routes         |
| `llm/ollama_client.py`       | Handles LLM (Ollama) communication   |
| `database/connection.py`     | SQLAlchemy DB connection setup       |
| `database/models.py`         | Table/column introspection utilities |
| `static/ask.html`            | User-facing web interface            |
| `data/ecommerce.db`          | Your SQLite database                 |
| `requirements.txt`           | List of Python dependencies          |

## ⚡ Deployment/Production Tips

- You do **not** upload or track your Python `venv` folder or any local environment files in GitHub—every collaborator creates their own.
- Never commit real API keys or production secrets (use `.env` files, add to `.gitignore`).
- For sharing demos, provide a sample database or clear instructions for data import.

## 💬 Example Questions

Try these in the web UI or API:
- What is my total sales?
- Calculate the RoAS (Return on Ad Spend).
- Which product had the highest CPC (Cost Per Click)?
- How many products are currently eligible?
- Which product had the highest number of impressions?

## 📺 Demo

To submit for grading or share your project:
- Record a terminal demo showing API/web interactions
- Show the answers for key business questions
- Push code/README/videos to your GitHub

## 📝 FAQ

**Q: Why not upload `venv`?**  
A: The virtualenv is local to your computer (contains OS-dependent binaries and lots of cache). Each user builds it themselves from `requirements.txt`.

**Q: Can I switch LLMs?**  
A: Yes—just change the model name in `llm/ollama_client.py` and pull the model using `ollama pull model_name`.

**Q: Is my data ever sent outside my machine?**  
A: No; all processing and analytics are local unless you explicitly use a cloud LLM.

## 🙏 Credits & License

Built using FastAPI, Pandas, SQLAlchemy, and modern open LLMs (Ollama).

---
**Feel free to fork, expand, and innovate! If you have issues, open an issue or pull request on GitHub.**
