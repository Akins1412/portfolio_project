// Google Cloud Translation setup
const {Translate} = require('@google-cloud/translate').v2;
const translate = new Translate();

async function translateText(text, targetLanguage) {
  let [translations] = await translate.translate(text, targetLanguage);
  translations = Array.isArray(translations) ? translations : [translations];
  return translations[0];
}

async function translatePage(language) {
  const elements = document.querySelectorAll('[data-key]');
  for (const element of elements) {
    const key = element.getAttribute('data-key');
    const originalText = element.textContent;
    const translatedText = await translateText(originalText, language);
    element.textContent = translatedText;
  }
}

document.getElementById('language-select').addEventListener('change', (event) => {
  const selectedLanguage = event.target.value;
  translatePage(selectedLanguage);
});
