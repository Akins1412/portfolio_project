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

  // Update placeholder text based on language
  const searchInput = document.querySelector("input[name='search']");
  const translatedPlaceholder = await translateText("Search Movies...", language);
  searchInput.setAttribute('placeholder', translatedPlaceholder);
}

// Event listener for language selection
document.getElementById('language-select').addEventListener('change', (event) => {
  const selectedLanguage = event.target.value;
  translatePage(selectedLanguage);
});

// Existing functionality
const searchInput = document.querySelector("input[name='search']");

searchInput.addEventListener("focus", function() {
  this.placeholder = "Enter Movie Title...";
});

searchInput.addEventListener("blur", function() {
  this.placeholder = "Search Movies...";
});

const ticketBtn = document.querySelector(".ticket-btn");

ticketBtn.addEventListener("mouseover", function() {
  this.style.backgroundColor = "#28a745";
});

ticketBtn.addEventListener("mouseout", function() {
  this.style.backgroundColor = "#1a6e67";
});
