# Link Analytics Prototype

A small Flask backend that summarizes link performance using in-memory demonstration data. It calculates click-through rates and returns rule-based suggestions; it does not use an LLM.

## Repository map

- `backend/analytics.py`: per-link and overall CTR calculations and suggestions.
- `backend/database.py`: sample users, links, impressions, and click counts.
- `backend/app.py`: intended `POST /chatbot` endpoint.
- `frontend/`: a basic interface for displaying insights.

## Development status

This is an unfinished learning prototype. The current backend has a trailing unmatched parenthesis, and `requirements.txt` needs conversion to a valid dependency list before installation. `seed_data.py` expects MongoDB collections while the active database is a set of Python lists. The frontend calls a separate localhost origin without a configured cross-origin strategy.

## Next steps

1. Fix application startup and dependency installation.
2. Add input validation and handle unknown users, empty results, and zero impressions.
3. Add tests for CTR aggregation and API responses.
4. Serve the frontend from the backend or configure a deliberate cross-origin policy.
5. Choose and document a persistence layer before adding authentication or deployment.

The demo data is synthetic. No production readiness or model-performance claims are made.
