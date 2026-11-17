# AI Data Analyst

Turn natural language questions into executable SQL against your local SQLite database. This project uses LangChain with local Ollama models and runs on the ultra-fast `uv` Python package manager.

## Features
- Automatic schema extraction from `amazon.db`
- Natural language to SQL using local LLM (Ollama)
- Deterministic SQL generation (`temperature=0`)
- Simple Python API (`get_data_from_database(prompt)`) for integration
- Fast environment setup and dependency management via `uv`

## Tech Stack
- Python 3.11+
- SQLite (`amazon.db`)
- SQLAlchemy for schema introspection
- LangChain Core + Community + Ollama integration
- Ollama local models (recommend: `qwen2.5-coder:7b` for speed) if system is not capable enought use 'qwen2.5-coder:7b' results may be less accurate if used, but can run on low end systems
- `uv` for dependency resolution, syncing, and running

## Architecture
1. Extract schema using SQLAlchemy inspector
2. Feed schema + user question to an LLM prompt template
3. Model returns a SQL query (reasoning models may include `<think>` blocks – we strip or avoid them)
4. Execute SQL safely against `amazon.db`
5. Return results list

```
