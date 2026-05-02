document.getElementById("analyzeBtn").addEventListener("click", async () => {
  const url = document.getElementById("urlInput").value.trim();
  const resultDiv = document.getElementById("result");
  const loadingDiv = document.getElementById("loading");
  const errorDiv = document.getElementById("error");

  // Reset UI
  resultDiv.style.display = "none";
  errorDiv.style.display = "none";
  loadingDiv.style.display = "block";

  try {
    const response = await fetch("http://127.0.0.1:8000/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url: url })
    });

    const data = await response.json();
    loadingDiv.style.display = "none";

    // Pick color based on score
    let scoreClass = "low";
    if (data.risk_score >= 7) scoreClass = "high";
    else if (data.risk_score >= 4) scoreClass = "moderate";

    resultDiv.innerHTML = `
      <div class="score ${scoreClass}">${data.risk_score}/10</div>
      <div class="explanation">${data.explanation}</div>
      <div class="tags">
        <span class="tag ${data.suspicious_tld ? 'yes' : 'no'}">
          ${data.suspicious_tld ? "⚠ Suspicious TLD" : "✓ Normal TLD"}
        </span>
        <span class="tag ${data.misleading_brand ? 'yes' : 'no'}">
          ${data.misleading_brand ? "⚠ Brand Impersonation" : "✓ No Impersonation"}
        </span>
      </div>
    `;

    resultDiv.style.display = "block";

  } catch (err) {
    loadingDiv.style.display = "none";
    errorDiv.textContent = "Could not connect to backend. Make sure it is running.";
    errorDiv.style.display = "block";
  }
});