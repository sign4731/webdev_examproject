function handleFileInput(){
    console.log("Getting image");
    console.log(event.target.value);
    console.log(event.target.parentElement);
    
    const form = event.target.form;
    console.log(form);

    if (event.target.value){
        form.querySelector(".tweet_image_container").classList.remove("hide");
        form.querySelector(".tweet_image").src = URL.createObjectURL(event.target.files[0]);
    } else {
        form.querySelector(".tweet_image_container").classList.add("hide");
        form.querySelector(".tweet_image").src = "";
    }
}