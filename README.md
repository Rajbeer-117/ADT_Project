# ADT_Project

# Hybrid Cybersecurity Threat Intelligence Retrieval using Vector Databases

## Project Title

**Comparative Analysis of Vector Database Systems for Hybrid Cybersecurity Threat Intelligence Retrieval**

## Project Overview

This project focuses on evaluating and comparing modern vector database systems for hybrid cybersecurity threat intelligence retrieval. The study uses cybersecurity datasets such as NVD/CVE vulnerability records and MITRE ATT&CK technique descriptions to analyze how different database systems perform when handling both structured filtering and semantic similarity search.

The project compares three database systems:

- PostgreSQL with pgvector
- Milvus
- Weaviate

The main goal is to understand how these systems behave under cybersecurity-specific workloads where analysts may need to search for semantically similar vulnerabilities or attack techniques while also applying filters such as severity, platform, date, or attack category.

## Problem Statement

Cybersecurity threat intelligence data is often large, complex, and mixed in format. Traditional relational databases are effective for structured queries, but they do not handle semantic similarity search efficiently. Vector databases support semantic retrieval, but they may face challenges when combined with structured filters.

This project investigates how PostgreSQL, Milvus, and Weaviate perform when executing hybrid queries that combine:

- Vector similarity search
- Metadata filtering
- Severity-based filtering
- Temporal filtering
- Cybersecurity-specific query workloads

## Objectives

The main objectives of this project are:

- Collect and preprocess cybersecurity datasets from NVD/CVE and MITRE ATT&CK.
- Design a unified schema for storing cybersecurity records.
- Generate text embeddings using Sentence-BERT.
- Store and query embeddings in PostgreSQL, Milvus, and Weaviate.
- Develop hybrid benchmark queries.
- Measure and compare query latency, recall, indexing performance, and memory usage.
- Analyze the strengths and limitations of each database system.
- Provide experimental findings for cybersecurity threat intelligence retrieval.

## Technologies Used

- Python
- PostgreSQL
- pgvector
- Milvus
- Weaviate
- Docker
- Docker Compose
- Sentence-BERT
- NumPy
- Pandas
- Matplotlib
- NVD/CVE Dataset
- MITRE ATT&CK Dataset

## System Architecture

The project follows a modular architecture with the following major components:

1. **Data Collection Module**  
   Collects cybersecurity data from NVD/CVE and MITRE ATT&CK sources.

2. **Data Preprocessing Module**  
   Cleans, normalizes, and prepares raw cybersecurity records for storage and embedding generation.

3. **Embedding Generation Module**  
   Uses Sentence-BERT to convert vulnerability descriptions and attack technique descriptions into vector embeddings.

4. **Database Storage Layer**  
   Stores structured metadata and embeddings in PostgreSQL with pgvector, Milvus, and Weaviate.

5. **Benchmark Execution Module**  
   Runs hybrid query workloads across all three systems.

6. **Metrics Collection Module**  
   Collects latency, recall, indexing time, memory usage, and system performance metrics.

7. **Result Analysis Module**  
   Compares database performance and generates visualizations for the final report and presentation.

## Dataset

The project uses cybersecurity threat intelligence datasets including:

- **NVD/CVE Dataset**  
  Contains vulnerability records, descriptions, severity scores, publication dates, affected products, and other metadata.

- **MITRE ATT&CK Dataset**  
  Contains attack techniques, tactics, descriptions, and related cybersecurity knowledge.

These datasets are processed into a unified schema to support fair comparison across all database systems.

## Unified Data Schema

The unified schema includes fields such as:

- Document ID
- Source type
- CVE ID or ATT&CK technique ID
- Title
- Description
- Severity score
- Attack tactic
- Affected platform
- Publication date
- Metadata fields
- Embedding vector

This schema allows the same dataset to be loaded into PostgreSQL, Milvus, and Weaviate for consistent benchmarking.

## Benchmark Queries

The benchmark includes hybrid queries that combine semantic search with structured filters. Example query types include:

- Find vulnerabilities semantically similar to a given threat description.
- Retrieve high-severity CVEs related to a specific attack category.
- Search for attack techniques similar to a given malware behavior.
- Filter vulnerabilities by severity, platform, and publication date.
- Compare top-k retrieval results across PostgreSQL, Milvus, and Weaviate.

## Evaluation Metrics

The systems are evaluated using the following metrics:

- Query latency
- Recall@10
- Recall@50
- Index build time
- Memory usage
- Storage size
- Scalability across dataset sizes
- Performance under hybrid structured-semantic workloads




