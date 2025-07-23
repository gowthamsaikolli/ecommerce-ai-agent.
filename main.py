from fastapi import FastAPI
from pydantic import BaseModel
from llm.ollama_client import ask_ollama
from database.connection import engine
import pandas as pd
import numpy as np
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import re

app = FastAPI()

# Serve static files from the /static path.
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=FileResponse)
async def serve_html():
    return FileResponse("static/ask.html")

class QuestionInput(BaseModel):
    question: str

def extract_sql(text):
    # Extracts the first SQL SELECT ... ; statement.
    match = re.search(r"(SELECT[\s\S]+?;)", text, re.IGNORECASE)
    if match:
        return match.group(1)
    # Otherwise, just look for the first line starting with SELECT
    for line in text.split("\n"):
        if line.strip().upper().startswith('SELECT'):
            return line.strip()
    return text.strip()

@app.post("/ask")
async def ask_endpoint(input: QuestionInput):
    user_question = input.question

    # STRONG, UNIFORM PROMPT — exact same always!
    prompt = (
        "You are an expert database analyst. "
        "Given these SQLite tables (with columns):\n"
        "ad_sales(date, item_id, ad_sales, impressions, ad_spend, clicks, units_sold)\n"
        "eligibility(eligibility_datetime_utc, item_id, eligibility, message)\n"
        "total_sales(date, item_id, total_sales, total_units_ordered)\n"
        " For example:\n"
        "Question: Which product had the highest number of impressions?\n"
        "Answer: SELECT item_id FROM ad_sales ORDER BY impressions DESC LIMIT 1;\n"
        "Question: How many products are currently eligible?\n"
        "Answer: SELECT COUNT(*) FROM eligibility WHERE eligibility = 'Eligible';\n"
        "Write ONLY the SQL SELECT statement (no explanation , extra text,one line) to answer this question: "
        f"{user_question}\n"
        "Only return the column(s) necessary to answer the question, not all columns. Do not output ad_sales unless asked."
    )
    print("LLM Prompt Sent:", prompt)  # For debugging

    # Get SQL from LLM
    sql_query = ask_ollama(prompt)
    print("Raw SQL from LLM:", sql_query)
    sql_query = extract_sql(sql_query)
    print("Executing SQL:", sql_query)

    try:
        df = pd.read_sql_query(sql_query, engine)
        df.reset_index(drop=True, inplace=True)
        df = df.where(pd.notnull(df), None)
        answer = df.to_dict(orient="records")
    except Exception as e:
        answer = f"SQL execution error: {str(e)}"

    return {"sql": sql_query, "answer": answer}
