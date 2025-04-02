function uploadFile() {
    const fileInput = document.getElementById("fileInput");
    const outputDiv = document.getElementById("output");
  
    if (!fileInput.files[0]) {
      alert("Please select a file!");
      return;
    }
  
    const formData = new FormData();
    formData.append("file", fileInput.files[0]);
  
    outputDiv.innerHTML = "⏳ Analyzing...";
    outputDiv.classList.remove("hidden");
  
    fetch("http://127.0.0.1:8000/extract/", {
      method: "POST",
      body: formData
    })
      .then(res => res.json())
      .then(data => {
        if (data.error) {
          outputDiv.innerHTML = `❌ Error: ${data.error}`;
          return;
        }
  
        const reqOutput = formatOutput(data.requirements_output);
        const emotions = formatEmotionBars(data.emotion_summary);
  
        outputDiv.innerHTML = `
          <h3>📦 Extracted Requirements</h3>
          <pre>${reqOutput}</pre>
          <h3 style="margin-top:20px;">❤️ Emotion Summary</h3>
          ${emotions}
        `;
      })
      .catch(err => {
        outputDiv.innerHTML = `❌ Error: ${err}`;
      });
  }
  
  function formatOutput(text) {
    return text.replace(/\*\*(.*?)\*\*/g, (_, title) => `\n🔹 ${title.toUpperCase()}\n`)
               .replace(/\n{2,}/g, "\n\n")
               .replace(/\n- /g, "\n• ");
  }
  
  function formatEmotionBars(emotions) {
    return Object.entries(emotions).map(([emotion, value]) => {
      const percent = Math.round(value * 100);
      return `
        <div>
          <strong>${emotion}</strong>
          <div style="background:#eee;border-radius:4px;">
            <div style="width:${percent}%;background:#4f46e5;height:10px;border-radius:4px;"></div>
          </div>
          <span>${percent}%</span>
        </div>
      `;
    }).join("<br>");
  }
  