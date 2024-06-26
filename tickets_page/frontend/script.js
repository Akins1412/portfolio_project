document.getElementById('language-select').addEventListener('change', async (event) => {
  const language = event.target.value;
  const elementsToUpdate = document.querySelectorAll('[data-key]');

  for (const element of elementsToUpdate) {
    const key = element.getAttribute('data-key');
    const textToTranslate = element.textContent;

    try {
      const response = await fetch('/translate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          text: textToTranslate,
          target: language
        })
      });

      if (!response.ok) {
        throw new Error('Translation request failed');
      }

      const data = await response.json();
      element.textContent = data.translation;
    } catch (error) {
      console.error('Error fetching translations:', error);
    }
  }
});

document.addEventListener('DOMContentLoaded', () => {
  const defaultLanguage = 'en';
  document.getElementById('language-select').value = defaultLanguage;
  document.getElementById('language-select').dispatchEvent(new Event('change'));
});
