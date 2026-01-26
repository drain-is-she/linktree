from flask import Flask, jsonify, request
from analytics import analyze_user, generate_insights

app = Flask(__name__)

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    user_id = data.get("user_id")

    report, overall_ctr = analyze_user(user_id)
    insights = generate_insights(report, overall_ctr)

    return jsonify({
        "overall_ctr": overall_ctr,
        "link_report": report,
        "insights": insights
    })

if __name__ == "__main__":
    app.run(debug=True)
