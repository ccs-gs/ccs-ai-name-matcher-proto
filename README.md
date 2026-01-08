# ccs-ai-name-matcher-proto

A lightweight fastapi interface to allow us to match an input string to one of a list of strings using a LangChain model.

## Run locally

Create a virtualenv, install deps, and run the server:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Set environment variables (see `env.example.txt`):

- Recommended: copy the example file to `.env` and edit it (the app will load `.env` automatically):

```bash
cp env.example.txt .env
```

Or export them in your shell:

```bash
export AZURE_OPENAI_ENDPOINT="https://<resource>.openai.azure.com/"
export AZURE_OPENAI_KEY="..."
export AZURE_OPENAI_DEPLOYMENT_NAME="..."
export AZURE_OPENAI_API_VERSION="2024-02-15-preview"
```

Run via uvicorn CLI:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Or run via Python entrypoint (still uses uvicorn under the hood):

```bash
python app.py
```

## API

### GET /match

Example:

```bash
curl "http://localhost:8000/match?input_string=Acme%20Corp&candidates=ACME%20Corporation&candidates=Other%20Inc"
```

