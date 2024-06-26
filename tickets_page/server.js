const express = require('express');
const bodyParser = require('body-parser');
const { Translate } = require('@google-cloud/translate').v2;

const app = express();
const translate = new Translate();

app.use(bodyParser.json());

app.post('/translate', async (req, res) => {
  const { text, target } = req.body;

  try {
    const [translation] = await translate.translate(text, target);
    res.json({ text, translation });
  } catch (error) {
    res.status(500).send(error);
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

