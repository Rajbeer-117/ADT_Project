from __future__ import annotations

import json
from pathlib import Path
from src.data_pipeline import read_jsonl, write_jsonl, add_embeddings, load_queries
from src.db.local_adapter import LocalExactAdapter
from src.evaluation.benchmark import run_benchmark

input_path = Path("data/sample_cyber_docs.jsonl")
processed_path = Path("data/processed_docs.jsonl")
queries_path = Path("data/benchmark_queries.json")
output_path = Path("data/results/local_sample_results.json")

docs = add_embeddings(read_jsonl(input_path))
write_jsonl(processed_path, docs)
queries = load_queries(queries_path)
adapter = LocalExactAdapter(docs)
results = run_benchmark([adapter], queries, adapter, repeats=3)
output_path.parent.mkdir(parents=True, exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("Local sample benchmark completed.")
print(f"Documents: {len(docs)}")
print(f"Queries: {len(queries)}")
print(f"Results: {output_path}")
for item in results["systems"]["local_exact"]:
    print(f"\n{item['query_id']}: {item['query_text']}")
    for r in item["top_results"][:3]:
        print(f"  - {r['doc_id']} | score={r['score']:.3f} | {r['title']}")
