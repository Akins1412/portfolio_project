"use strict"


const form = document.querySelector(".form");
const error = document.querySelector(".error");


form.addEventListener("submit", (e) => {
    e.preventDefault();
    const username = document.querySelector(".username").value;
    const email = document.querySelector(".email").value;
    const password = document.querySelector(".password").value;

    const data = { username, email, password };
    const regUrl = "http://127.0.0.1:2000/api/v1/register/";

    console.log(data)
    fetch(regUrl, {
        method: "POST",
        headers: {
            "accept": "application/json",
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response => {
        return response.json()
    })
        .then(data => {
            console.log(data);
            window.location.href = "http://127.0.0.1:5500/frontend/login/login.html"
        }).catch(error => {
            console.error('error', error);
        })
});
// console.log(submitBtn)

