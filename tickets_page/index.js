const form = document.querySelector("#loginForm");

console.log(form)

form.addEventListener("submit", (event) =>{
    event.preventDefault();

    const username = document.querySelector("#username").value;
    const password = document.querySelector("#password").value;

    const url = "http://127.0.0.1:5000/api/v1/login"
    const data = {username, password}

    // console.log(data)
    fetch(url,{
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
        console.log(data)
    }).catch(error =>{
        console.error('error',error);
    })
})