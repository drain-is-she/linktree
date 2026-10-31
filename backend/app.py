from pathlib import Path

from flask import Flask, jsonify, request
from analytics import analyze_user, generate_insights
from database import users

app = Flask(__name__, static_folder=str(Path(__file__).resolve().parents[1] / "frontend"),
            static_url_path="/static")


@app.get("/")
def index():
    return app.send_static_file("index.html")


@app.post("/chatbot")
def chatbot():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify(error="Send a JSON object containing user_id."), 400
    user_id = data.get("user_id")
    if not isinstance(user_id, str) or not user_id.strip():
        return jsonify(error="user_id must be a non-empty string."), 400
    user_id = user_id.strip()
    if not any(user["user_id"] == user_id for user in users):
        return jsonify(error="User not found."), 404

    report, overall_ctr = analyze_user(user_id)
    return jsonify(overall_ctr=overall_ctr, link_report=report,
                   insights=generate_insights(report, overall_ctr))


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=False)
