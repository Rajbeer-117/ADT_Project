# Windows / VS Code Quick Start

Open PowerShell terminal in the main project folder. The prompt should end with:

```powershell
...\hybrid_cyber_vector_project>
```

Run these commands one by one:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python run_sample.py
```

Expected result:

```text
Local sample benchmark completed.
Documents: 12
Queries: 4
Results: data/results/local_sample_results.json
```

## To prepare data manually

Use this command, not `python scripts/prepare_data.py`, if your PowerShell cannot find the `src` module:

```powershell
python -m scripts.prepare_data --input data/sample_cyber_docs.jsonl --output data/processed_docs.jsonl
```

## Full database version

The full PostgreSQL, Milvus, and Weaviate benchmark requires Docker Desktop. If `docker` is not recognized, install and open Docker Desktop first, then restart VS Code.

After Docker works, install full dependencies:

```powershell
pip install -r requirements-full.txt
```

Then run:

```powershell
docker compose up -d postgres weaviate etcd minio milvus
python -m scripts.init_postgres
python -m scripts.prepare_data --input data/sample_cyber_docs.jsonl --output data/processed_docs.jsonl
python -m scripts.load_postgres --input data/processed_docs.jsonl
python -m scripts.load_milvus --input data/processed_docs.jsonl
python -m scripts.load_weaviate --input data/processed_docs.jsonl
python -m scripts.run_benchmark --systems postgres milvus weaviate --queries data/benchmark_queries.json --output data/results/benchmark_results.json
```

## Frontend demo

```powershell
uvicorn backend.main:app --reload --port 8000
```

Then open `frontend/index.html` in your browser.
