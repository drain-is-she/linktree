async function getInsights() {
  const output = document.getElementById("output");
  output.innerText = "Loading insights…";
  try {
    const response = await fetch("/chatbot", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: "u123" })
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Unable to load insights.");
    output.innerText = "Overall CTR: " + data.overall_ctr + "%\n\nInsights:\n" +
      data.insights.map(line => "- " + line).join("\n");
  } catch (error) {
    output.innerText = "Could not load insights: " + error.message;
  }
}
