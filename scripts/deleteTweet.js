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
    alert("Could not delete tweet, try again later");
    return;
    }

    if(document.querySelector(".tweet_amount span")){
      console.log(document.querySelector(".tweet_amount span").textContent);
      let valueStr = document.querySelector(".tweet_amount span").textContent;
      let valueInt = parseInt(valueStr);
      document.querySelector(".tweet_amount span").textContent = valueInt - 1;
  }

    tweet.parentElement.remove()
}