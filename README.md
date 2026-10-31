# Link Analytics Prototype

A runnable Flask demo that summarizes link performance using in-memory demonstration data. It calculates click-through rates (CTR) and returns rule-based suggestions; it does not use an LLM.

## Run locally

Python 3.10 or newer is required.

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python backend/app.py
```

On Windows, activate with `.venv\Scripts\activate` instead. Open http://127.0.0.1:5000 and select **Get My Insights**. Flask serves both the page and API from the same origin. Debug mode is off by default.

## API

```sh
curl http://127.0.0.1:5000/chatbot \
  -H 'Content-Type: application/json' \
  -d '{"user_id":"u123"}'
```

The response contains `overall_ctr`, a `link_report`, and `insights`. For the bundled sample, total clicks are 288 over 3,500 impressions, giving **8.23% overall CTR**. Overall CTR is calculated from totals, not the unweighted mean of per-link percentages.

Invalid JSON, non-object bodies, and missing/invalid user IDs return JSON errors with HTTP 400. Unknown users return 404. Known users with no recorded impressions receive a successful empty-data response instead of an exception. Zero-impression links have a display CTR of zero and are excluded from best/worst-link advice because their performance is not yet measurable.

## Test

```sh
python -m unittest discover -s tests -v
```

Tests cover weighted CTR, invalid requests, unknown users, absent data, zero impressions, ranking of observed links, and same-origin page/script delivery.

## Repository map

- `backend/analytics.py`: per-link and overall CTR calculations and suggestions.
- `backend/database.py`: sample users, links, impressions, and click counts, loaded automatically.
- `backend/app.py`: page delivery and `POST /chatbot` endpoint.
- `frontend/`: demo interface, including request error handling.
- `tests/`: regression tests using Flask's test client and Python's unittest.

## Scope and next steps

This is a local learning demo, not a production service. There is no authentication, persistent storage, real event ingestion, or LLM integration. The sample user ID is fixed in the frontend; the API is not suitable for exposing private analytics.

`backend/seed_data.py` is an older MongoDB-oriented experiment and is **not part of the runnable demo**. Do not run it with the current list-based storage. No seeding command or MongoDB installation is needed.

Next steps are to reconcile that legacy seed script with a deliberate persistence design, add event ingestion and authorization, and measure behavior under realistic data volumes before deployment. All bundled analytics data is synthetic.
