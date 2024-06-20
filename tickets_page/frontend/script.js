const searchInput = document.querySelector("input[name='search']");

searchInput.addEventListener("focus", function() {
  this.placeholder = "Enter Movie Title...";
});

searchInput.addEventListener("blur", function() {
  this.placeholder = "Search Movies...";
});

const ticket-Btn = document.querySelector(".ticket-btn");

ticket-Btn.addEventListener("mouseover", function() {
  this.style.backgroundColor = "#28a745"; // Change to desired hover color
});

ticket-Btn.addEventListener("mouseout", function() {
  this.style.backgroundColor = "#1a6e67"; // Change back to original color
});

