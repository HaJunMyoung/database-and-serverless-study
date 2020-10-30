console.log('hello world');

let h1 = document.createElement("h1");

h1.innerHTML = "rly? ";

document.addEventListener("DOMContentLoaded", function () {
    let body = document.getElementById('body');
    body.appendChild(h1);
})

