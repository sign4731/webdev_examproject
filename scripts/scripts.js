
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
    } else if(modal == "update"){
        console.log(event.target.form.parentElement.querySelector(".tweet_update"));
        event.target.form.parentElement.querySelector(".tweet_update").classList.add("show_flex");
    } else if(modal == "close"){
        console.log(event.target)
        event.target.parentElement.classList.remove("show_flex");
    }
}

function handleFileInput(){
    console.log("getting image");
    console.log(event.target.value);
    const form = event.target.form;

    if (event.target.value){
        form.querySelector(".tweet_image").classList.remove("hide");
        form.querySelector(".tweet_image").src = URL.createObjectURL(event.target.files[0]);
    } else {
        form.querySelector(".tweet_image").classList.add("hide");
        form.querySelector(".tweet_image").src = "";
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

async function createTweet(){
    console.log("Tweet");
    const form = event.target.parentElement;
    console.log(form);
    console.log(new FormData(form));

    const conneciton = await fetch("/create-tweet", {
        method: "POST",
        body: new FormData(form)
    });

    console.log(conneciton);
    if (!conneciton.ok) {
        alert("There was an issue with your tweet")
    return;
    }

    let response = await conneciton.json()
    console.log(response);

    let tweet = `
    <div class="tweet">
                            
        <img src="profile_images/${response.user_image}" alt="" class="user_image">
        <form onsubmit="return false" action="">
        <input class="tweet_id" type="hidden" value="${response.tweet_id}">
            <div class="tweet_info">
                <a href="" class="tweet_user_name">${response.user_first_name}</a href="">
                <p class="tweet_user_tag">${response.user_tag}</p>
                <p class="tweet_iat">${response.tweet_iat_date}</p>
            </div>
            
            <p class="tweet_text">${response.tweet_text}</p>

           ${response.tweet_image ? `<img src="tweet_images/${response.tweet_image}" alt="" class="tweet_image">` : ``}

            <div class="tweet_btns">

                <button onclick="handleLikeTweet()" class="own_tweet_like fa-solid fa-heart">
                    <span>0</span>
                </button>

                <button onclick="updateTweet()" class="tweet_update_btn fa-solid fa-pen-to-square"></button>
                <button onclick="deleteTweet()" class="tweet_delete_btn fa-solid fa-trash-can"></button>
            </div>
        </form>

    </div>
    `;

    document.querySelector("#main__tweets").insertAdjacentHTML("afterbegin", tweet)
    form.reset()
    form.querySelector(".tweet_image").src = "";
    form.querySelector(".tweet_image").classList.add("hide")
}

async function deleteTweet(){
    console.log("You deleted a tweet!");
    const tweet = event.target.form;
    console.log(tweet);

    let tweet_id = tweet.querySelector(".tweet_id").value;
    console.log(tweet_id);

    const connection = await fetch("/main/" + tweet_id, {
        method: "DELETE",
      });
    
    console.log(connection);
    if (!connection.ok) {
    alert("Could not delete tweet");
    return;
    }

    tweet.parentElement.remove()
}

async function updateTweet(){
    console.log("You updated a tweet!");
    const form = event.target.form;
    console.log(form);

    const tweet_id = form.parentElement.parentElement.querySelector(".tweet_id").value;
    console.log(tweet_id);

    const connection = await fetch("/main/" + tweet_id, {
        method: "PUT",
        body: new FormData(form),
    });
    
    console.log(connection);
    if (!connection.ok) {
        alert("Could not update tweet");
        return;
    }

    let response = await connection.json();
    console.log(response);

    form.parentElement.parentElement.querySelector(".tweet_text").textContent = response.tweet_text;
    if (response.tweet_image){
        console.log("Image is updated");
        form.parentElement.parentElement.querySelector(".tweet_image").src = "/tweet_images/" + response.tweet_image;
        form.parentElement.parentElement.querySelector(".tweet_image").classList.remove("hide");
    } else {
        console.log("Image is removed");
        form.parentElement.parentElement.querySelector(".tweet_image").src = "";
        form.parentElement.parentElement.querySelector(".tweet_image").classList.add("hide");
    }
    
    console.log(form.parentElement);
    form.parentElement.classList.remove("show_flex")
    form.reset()
    form.querySelector(".tweet_image").src = "";
    form.querySelector(".tweet_image").classList.add("hide");
}

async function handleLikeTweet(){
    console.log("You clicked a like button");
    let likeBtn = event.target;
    let tweet = event.target.form;
    console.log(likeBtn);
    console.log(tweet);

    likeBtn.classList.toggle("liked");
    let tweet_id = tweet.querySelector(".tweet_id").value;

    if(likeBtn.classList.contains("liked")){
        console.log(likeBtn);
        console.log("You liked a tweet!");
        likeBtn.dataset.liked = "true";
        
        console.log(likeBtn.querySelector("span").innerText)
        likeBtn.querySelector("span").innerText = parseInt(likeBtn.querySelector("span").innerText) + 1;
        
        console.log(tweet_id);
    
        const connection = await fetch("/likes/" + tweet_id, {
            method: "POST",
        });
        return
    } 

    if(!likeBtn.classList.contains("liked")){
        console.log("You disliked a tweet!");
        console.log(likeBtn);
        likeBtn.dataset.liked = "false";

        likeBtn.querySelector("span").innerText = parseInt(likeBtn.querySelector("span").innerText) - 1;
        console.log(tweet_id);

        const connection = await fetch("/likes/" + tweet_id, {
            method: "DELETE",
        });
        return

    }

}

