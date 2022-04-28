async function onSearch(){
    console.log("You are searching!");
    const form = event.target.parentElement;
    console.log(form);
    const search_box = document.querySelector(".search_box");
    

    const connection = await fetch("/search", {
        method: "POST",
        body: new FormData(form)
    });

    console.log(connection);
    if (!connection.ok) {
        search_box.querySelector("p").innerText = "There was an issue searching, try again later"
    return;
    };

    let response = await connection.json();
    console.log(response);

    if(response.search_output.length >= 1){
        console.log("There is a match!");
        search_box.innerHTML = "";
        response.search_output.forEach(user => {
            console.log(user);
            let user_element = `
            <a href="/profile/${user['user_id']}" class="user">
                <input type="hidden" value="${user['user_id']}">
                <img src="../profile_images/${user['user_image']}" alt="user image" class="user_image">
                <div class="user__names">
                    <p>${user["user_first_name"]}</p>
                    <p>${user["user_tag"]}</p>
                </div>
            </a>`;
    
            
            search_box.insertAdjacentHTML("afterbegin", user_element);
        })
    } else if(form.input == "" | form.input == null){
        search_box.innerHTML = `<p>Try searching for people</p>`;
    } else {
        console.log("There is not a match!");
        search_box.innerHTML = `<p>Try searching for people</p>`;
    }

    

}