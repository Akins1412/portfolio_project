const express = require('express');
const bodyParser = require('body-parser');
const { Translate } = require('@google-cloud/translate').v2;

const app = express();
const translate = new Translate();

app.use(bodyParser.json());

// Endpoint to handle translation requests
app.post('/translate', async (req, res) => {
  const { text, target } = req.body;

  try {
    // Perform translation using Google Cloud Translation API
    const [translation] = await translate.translate(text, target);
    res.json({ text, translation });
  } catch (error) {
    console.error('Error translating text:', error);
    res.status(500).json({ error: 'Translation failed' });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
