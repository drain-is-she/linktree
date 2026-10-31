import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))
import analytics
from app import app


class AnalyticsTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_demo_uses_weighted_ctr(self):
        response = self.client.post("/chatbot", json={"user_id": "u123"})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["overall_ctr"], 8.23)  # 288 / 3500, not mean link CTR
        self.assertEqual([row["ctr"] for row in data["link_report"]], [12.0, 8.0, 1.5])
        self.assertIn("YouTube", data["insights"][-1])

    def test_invalid_bodies(self):
        for body in [None, [], "u123", 1, {}, {"user_id": 1}, {"user_id": " "}]:
            with self.subTest(body=body):
                response = self.client.post("/chatbot", json=body)
                self.assertEqual(response.status_code, 400)
                self.assertIn("error", response.get_json())
        for payload, content_type in [("{", "application/json"), ("u123", "text/plain")]:
            response = self.client.post("/chatbot", data=payload, content_type=content_type)
            self.assertEqual(response.status_code, 400)

    def test_unknown_user(self):
        self.assertEqual(self.client.post("/chatbot", json={"user_id": "unknown"}).status_code, 404)

    def test_empty_data(self):
        with patch.object(analytics, "click_events", []):
            response = self.client.post("/chatbot", json={"user_id": "u123"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["link_report"], [])
        self.assertEqual(response.get_json()["overall_ctr"], 0)
        self.assertIn("No impression data", response.get_json()["insights"][0])

    def test_zero_impressions(self):
        events = [dict(row, impressions=0, clicks=0) for row in analytics.click_events]
        with patch.object(analytics, "click_events", events):
            response = self.client.post("/chatbot", json={"user_id": "u123"})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["overall_ctr"], 0)
        self.assertTrue(all(row["ctr"] == 0 for row in data["link_report"]))
        self.assertIn("No impression data", data["insights"][0])

    def test_no_links(self):
        with patch.object(analytics, "links", []):
            report, ctr = analytics.analyze_user("u123")
        self.assertEqual((report, ctr), ([], 0))

    def test_unobserved_link_not_ranked(self):
        events = [dict(row) for row in analytics.click_events]
        events[2].update(impressions=0, clicks=0)
        with patch.object(analytics, "click_events", events):
            report, ctr = analytics.analyze_user("u123")
        self.assertEqual(ctr, 10.22)
        insights = analytics.generate_insights(report, ctr)
        self.assertIn("Instagram", insights[-2])
        self.assertNotIn("Merch Store", " ".join(insights))

    def test_same_origin_demo(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertIn(b'/static/script.js', page.data)
        script = self.client.get("/static/script.js")
        self.assertEqual(script.status_code, 200)
        self.assertIn(b'fetch("/chatbot"', script.data)
        self.assertEqual(self.client.get("/static/../backend/database.py").status_code, 404)


if __name__ == "__main__":
    unittest.main()
