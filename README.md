# ccs-ai-name-matcher-proto

A lightweight **FastAPI-based microservice** for **LLM-powered name matching**, designed to match an input string (e.g. buyer or supplier name) to the most appropriate option from a list of candidate strings.

This service is intended to be reusable across CCS projects and supports both:
- **Azure OpenAI (via LangChain)** for production usage
- **Mock LLM logic** for local development and testing without external dependencies

## Overview
The service exposes a simple HTTP API that:
1. Accepts an `input_string`
2. Accepts a list of `candidates`
3. Uses an LLM to determine the best match (or returns `None`)

The core logic is intentionally minimal and modular so it can:
- Run as a standalone microservice
- Be called by dashboards, batch jobs or data pipelines
- Switch between mock and Azure OpenAI with minimal changes

## Project Structure
ccs-ai-name-matcher-proto/
│
├── app/
│ ├── main.py 
│ ├── config.py 
│ ├── model_factory.py 
│ ├── langchain_matcher.py 
│ └── services/
│ └── mock_langchain_model.py # Mock LLM for local/dev use
│
├── prompts/
│ └── buyer_match_v*.txt # Prompt templates (versioned)
│
├── env.example.txt 
├── requirements.txt 
├── app.py 
└── README.md


### Using Azure OpenAI

To enable Azure OpenAI instead of the mock LLM, update in `env.example.txt` (or your `.env` file) with valid Azure OpenAI credentials:

```env
AZURE_OPENAI_ENDPOINT=https://<your-resource-name>.openai.azure.com/
AZURE_OPENAI_KEY=<your-api-key>
AZURE_OPENAI_DEPLOYMENT_NAME=<your-deployment-name>
AZURE_OPENAI_API_VERSION=2024-02-15-preview

## Running Locally
### 1. Create and activate a virtual environment

bash
python -m venv .venv

windows-    .\.venv\Scripts\Activate.ps1

### 2. Install dependencies
pip install -r requirements.txt
### 3. configure env variables
cp env.example.txt .env
### 4.Run this service

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Or run via Python entrypoint (still uses uvicorn under the hood):

```bash
python app.py


## API Endpoints
### Health check
**GET /health**

Used to verify the service is running.

```bash
curl http://127.0.0.1:8000/health

### Name matching
**GET /match**
```bash
curl "http://127.0.0.1:8000/match?input_string=Home%20Ofice&candidates=Home%20Office&candidates=HMRC"





