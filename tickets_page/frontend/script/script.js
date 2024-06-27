const searchInput = document.querySelector("input[name='search']");
const hover = document.querySelectorAll(".nshowing3 img");
const book = document.querySelector(".hover-book");

console.log(hover)
console.log(book)


hover.forEach((img) => {
  img.addEventListener("mouseover", () => {
    book.classList.remove("hidden");
    // book.forEach((hov) => {
    //   hov.classList.remove("hidden");
    //   console.log("entred")
    // });
  })
})

hover.forEach((img) => {
  img.addEventListener("mouseout", () => {
    book.classList.add("hidden");

    // book.forEach((hov) => {
    //   hov.classList.remove("hidden");
    //   console.log("entred")
    // });
  })
})

