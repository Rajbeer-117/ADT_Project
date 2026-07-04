from __future__ import annotations

from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from pathlib import Path
from typing import Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.data_pipeline import read_jsonl, add_embeddings
from src.db.local_adapter import LocalExactAdapter

app = FastAPI(title="Hybrid Cyber Threat Intelligence Retrieval API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SearchRequest(BaseModel):
    text: str
    top_k: int = 5
    filters: dict[str, Any] = {}

_docs = None
_adapter = None

def get_adapter() -> LocalExactAdapter:
    global _docs, _adapter
    if _adapter is None:
        path = Path("data/processed_docs.jsonl")
        if path.exists():
            _docs = read_jsonl(path)
        else:
            _docs = add_embeddings(read_jsonl("data/sample_cyber_docs.jsonl"))
        _adapter = LocalExactAdapter(_docs)
    return _adapter

@app.get("/")
def root():
    return {"message": "Hybrid Cybersecurity Retrieval API", "docs": len(get_adapter().docs)}

@app.post("/search")
def search(req: SearchRequest):
    results = get_adapter().search(req.text, req.top_k, req.filters)
    return {"count": len(results), "results": [r.model_dump() for r in results]}

@app.get("/health")
def health():
    return {"status": "ok"}
