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
        alert("Could not update tweet, try again later");
        return;
    }

    let response = await connection.json();
    console.log(response);

    form.parentElement.parentElement.querySelector(".tweet_text").textContent = response.tweet_text;
    if (response.tweet_image){
        console.log("Image is updated");
        form.parentElement.parentElement.querySelector(".tweet_image").src = `/tweet_images/` + response.tweet_image;
        form.parentElement.parentElement.querySelector(".tweet_image").classList.remove("hide");
    } else {
        console.log("Image is removed");
        form.parentElement.parentElement.querySelector(".tweet_image").src = "";
        form.parentElement.parentElement.querySelector(".tweet_image").classList.add("hide");
    }
    
    console.log(form.parentElement);
    form.parentElement.classList.remove("show_flex")
    form.reset()
    form.querySelector(".tweet_update_image").src = "";
    form.querySelector(".tweet_update_image").classList.add("hide");
}