"use strict"


const form = document.querySelector(".form");
const error = document.querySelector(".error");


form.addEventListener("submit", (e) => {
    e.preventDefault();
    const username = document.querySelector(".username").value;
    const password = document.querySelector(".password").value;

    const data = { username, password };
    const loginUrl = "http://127.0.0.1:2000/api/v1/auth/login";

    // console.log(data)
    fetch(loginUrl, {
        method: "POST",
        headers: {
            "accept": "application/json",
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response => {
        console.log(response.status)
        return response.json()
    })
        .then(data => {
            console.log(data);
            if (data == "Invalid username or password") {
                error.textContent = data;
                error.classList.remove("hidden");
            } else {
                window.location.replace("http://127.0.0.1:5500/frontend/home/index.html")
            }
        }).catch(error => {
            console.error('error', error);
        })
});
// console.log(submitBtn)

