const searchInput = document.querySelector("input[name='search']");
const url = ""

searchInput.addEventListener("focus", function () {
  this.placeholder = "Enter Movie Title...";
});

searchInput.addEventListener("blur", function () {
  this.placeholder = "Search Movies...";
});

const ticketBtn = document.querySelector(".ticket-btn");

ticketBtn.addEventListener("mouseover", function () {
  this.style.backgroundColor = "#28a745";
});

ticketBtn.addEventListener("mouseout", function () {
  this.style.backgroundColor = "#1a6e67";
});

// FECTHING THE MOVIE
fetch()
