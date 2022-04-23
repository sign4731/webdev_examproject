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
        const text = await connection.text()
        form.querySelector(".error_message").textContent = text
        return;
    }

    let response = await connection.text()
    console.log(response);


    form.innerHTML = `
    <h2>You successfully signed up!</h2>
    <button onclick="toggleModal('login'); return false">Log in</button>
    `;

}