from database import links, click_events

def analyze_user(user_id):
    user_links = [link for link in links if link["user_id"] == user_id]

    report = []
    total_impressions = 0
    total_clicks = 0

    for link in user_links:
        stats = next((item for item in click_events if item["link_id"] == link["link_id"]), None)
        if not stats:
            continue

        impressions = stats["impressions"]
        clicks = stats["clicks"]
        ctr = round((clicks / impressions) * 100, 2)

        total_impressions += impressions
        total_clicks += clicks

        report.append({
            "title": link["title"],
            "impressions": impressions,
            "clicks": clicks,
            "ctr": ctr,
            "peak_time": stats["peak_time"]
        })

    overall_ctr = round((total_clicks / total_impressions) * 100, 2)

    return report, overall_ctr


def generate_insights(report, overall_ctr):
    advice = []

    if overall_ctr < 5:
        advice.append("Your overall CTR is low. Improve link titles and thumbnails.")
    elif overall_ctr < 8:
        advice.append("Your CTR is average. Try posting during peak engagement hours.")
    else:
        advice.append("Your CTR is strong. Keep your current strategy consistent.")

    worst = min(report, key=lambda x: x["ctr"])
    best = max(report, key=lambda x: x["ctr"])

    advice.append(f"Your lowest performing link is '{worst['title']}'. Improve its call-to-action or position.")
    advice.append(f"Your best performing link is '{best['title']}'. Keep it near the top of your hub.")

    return advice

