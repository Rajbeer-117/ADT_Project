# Midterm Progress Notes

## Project progress breakdown

The project implementation has been divided into four major components: data ingestion, database configuration, benchmark execution, and result analysis. The data ingestion component is responsible for collecting and normalizing cybersecurity intelligence records, including CVE/NVD-style vulnerability descriptions and MITRE ATT&CK-style technique descriptions. The database configuration component prepares PostgreSQL with pgvector, Milvus, and Weaviate using Docker Compose so that each system can be tested under comparable conditions. The benchmark execution component runs hybrid queries that combine semantic similarity search with structured filters such as platform, severity, source, and tactic. The result analysis component produces latency and recall measurements that can be used for the final report and presentation.

## Completed work

The repository structure, sample cybersecurity dataset, unified schema, embedding pipeline, local exact-search baseline, PostgreSQL schema, Milvus adapter, Weaviate adapter, benchmark runner, metrics module, chart generation script, API backend, and simple frontend demonstration have been prepared. A small sample dataset is included so that the prototype can be executed immediately without waiting for the full NVD and MITRE downloads.

## Remaining work

The remaining work is to run the benchmark on larger datasets, capture screenshots and terminal outputs for the report, tune database indexes, compare results across PostgreSQL, Milvus, and Weaviate, and finalize the analysis graphs. The final experiment should include larger dataset tiers such as 50K, 250K, and, if resources allow, 1M records.

## Novel insight to highlight

The main novelty is that this project evaluates hybrid structured-semantic retrieval rather than pure vector search. The expected insight is that structured filters can change the behavior of vector indexes by reducing candidate sets and affecting recall, especially when filter selectivity becomes very strict. This can produce latency and recall trade-offs that are not visible in standard vector-only benchmarks.
