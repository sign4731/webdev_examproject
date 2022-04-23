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