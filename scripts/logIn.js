async function logIn(){
    console.log("Log in");
    const form = event.target.parentElement;
    console.log(form);

    const connection = await fetch("/login", {
        method: "POST",
        body: new FormData(form)
    });


    
    if (!connection.ok) {
        const text = await connection.text()
        form.querySelector(".error_message").textContent = text;
        return;
    }
    

    let response = await connection.text()
    console.log(response);
    if (response == "nonexistent") {
        form.querySelector(".error_message").textContent = "User does not exist. You need to sign up first"
    return;
    } else{
        form.querySelector(".error_message").textContent = ""
    }

    window.location.href = "/main";
}