.PHONY: install sample up down prepare load-postgres load-milvus load-weaviate benchmark api

install:
	pip install -r requirements.txt

sample:
	python run_sample.py

up:
	docker compose up -d postgres weaviate etcd minio milvus

down:
	docker compose down

prepare:
	python scripts/prepare_data.py --input data/sample_cyber_docs.jsonl --output data/processed_docs.jsonl

load-postgres:
	python scripts/init_postgres.py
	python scripts/load_postgres.py --input data/processed_docs.jsonl

load-milvus:
	python scripts/load_milvus.py --input data/processed_docs.jsonl

load-weaviate:
	python scripts/load_weaviate.py --input data/processed_docs.jsonl

benchmark:
	python scripts/run_benchmark.py --systems postgres milvus weaviate --queries data/benchmark_queries.json --output data/results/benchmark_results.json

api:
	uvicorn backend.main:app --reload --port 8000
