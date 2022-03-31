
window.addEventListener("load", init)

function init(){
    console.log("Page and script loaded");
}

function toggleModal(modal){
    console.log("heyhey");
    if (modal == "signup"){
        document.querySelector("#sign_up").classList.add("show_flex");
    } else if(modal == "login"){
        document.querySelector("#sign_up").classList.remove("show_flex");
        document.querySelector("#log_in").classList.add("show_flex");
    }else if(modal == "close"){
        console.log(event.target)
        event.target.parentElement.classList.remove("show_flex");
    }
}


async function signUp(){
    console.log("User is signed up");
    const form = event.target.parentElement;
    console.log(form);

    const connection = await fetch("/signup", {
        method: "POST",
        body: new FormData(form)
    });

    console.log(connection);
    if (!connection.ok) {
     form.querySelector(".error_message").textContent = "There was an issue signing you up, try changing the data."
    return;
    }

    let response = await connection.text()
    console.log(response);


    form.innerHTML = `
    <h2>You successfully signed up!</h2>
    <button onclick="toggleModal('login'); return false">Log in</button>
    `;

}

async function logIn(){
    console.log("Log in");
    const form = event.target.parentElement;
    console.log(form);

    const conneciton = await fetch("/login", {
        method: "POST",
        body: new FormData(form)
    });

    console.log(conneciton)
    if (!conneciton.ok) {
        form.querySelector(".error_message").textContent = "There was an issue logging in, try changing the data."
    return;
    }

    let response = await conneciton.text()
    console.log(response);
    if (response == "nonexistent") {
        form.querySelector(".error_message").textContent = "User does not exist. You need to sign up first"
    return;
    } else{
        form.querySelector(".error_message").textContent = ""
    }

    window.location.href = "/main";
}