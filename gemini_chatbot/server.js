const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const app = express();
const PORT = 3000;

const API_KEY = 'AIzaSyCoa42LfPskvkheHpWqqg-L3WHzjyQrzL4'; // Replace with your real key

app.use(bodyParser.json());
app.use(express.static('.'));

app.post('/chat', async (req, res) => {
  const userMessage = req.body.message;
  console.log("User message:", userMessage);

  try {
    const response = await axios.post(
      `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${API_KEY}`,
      {
        contents: [
          {
            parts: [{ text: userMessage }]
          }
        ]
      },
      {
        headers: {
          'Content-Type': 'application/json'
        }
      }
    );

    console.log("Gemini raw response:", JSON.stringify(response.data, null, 2));
    const reply = response.data?.candidates?.[0]?.content?.parts?.[0]?.text || "No reply from Gemini.";
    res.json({ reply });

  } catch (error) {
    console.error("Gemini error:", error.response?.data || error.message);
    res.status(500).json({ reply: "Server error occurred." });
  }
});

app.listen(PORT, () => {
  console.log(`✅ Server running at http://localhost:${PORT}`);
});
