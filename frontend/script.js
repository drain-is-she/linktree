async function getInsights() {
  const response = await fetch("http://localhost:5000/chatbot", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: "u123" })
  });

  const data = await response.json();

  let text = "Overall CTR: " + data.overall_ctr + "%\n\n";
  text += "Insights:\n";

  data.insights.forEach(line => {
    text += "- " + line + "\n";
  });

  document.getElementById("output").innerText = text;
}
