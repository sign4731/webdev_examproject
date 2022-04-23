async function createTweet(){
    console.log("Tweet");
    const form = event.target.parentElement;
    console.log(form);
    console.log(new FormData(form));

    const connection = await fetch("/create-tweet", {
        method: "POST",
        body: new FormData(form)
    });

    console.log(connection);
    if (!connection.ok) {
        alert("There was an issue tweeting, try again later")
    return;
    }

    let response = await connection.json()
    console.log(response);

    let randomNumber = Math.random();
    let tweet = `
    <div class="tweet">
                            
        <img src="../${response.path}profile_images/${response.tweet_and_user.user_image}" alt="" class="user_image">
        <form onsubmit="return false" autocomplete="off" >
        <input class="tweet_id" type="hidden" value="${response.tweet_and_user.tweet_id}">
            <div class="tweet_info">
                <a href="" class="tweet_user_name">${response.tweet_and_user.user_first_name}</a href="">
                <p class="tweet_user_tag">${response.tweet_and_user.user_tag}</p>
                <p class="tweet_iat">${response.tweet_and_user.tweet_iat_date}</p>
            </div>
            
            <p class="tweet_text">${response.tweet_and_user.tweet_text}</p>

           ${response.tweet_and_user.tweet_image ? `<img src="../${response.path}tweet_images/${response.tweet_and_user.tweet_image}" alt="" class="tweet_image">` : `<img src="" alt="" class="tweet_image">`}

            <div class="tweet_btns">

                <button onclick="handleLikeTweet()" class="own_tweet_like fa-solid fa-heart">
                    <span>0</span>
                </button>

                <button onclick="toggleModal('update')" class="tweet_update_btn fa-solid fa-pen-to-square"></button>
                <button onclick="deleteTweet()" class="tweet_delete_btn fa-solid fa-trash-can"></button>
            </div>
        </form>

        <section class="tweet_modal tweet_update">
            <div class="tweet_modal__modal" onclick="toggleModal('close')"></div>
    
                <form onsubmit="return false" class="tweet_modal__form" autocomplete="off">
                <i class="back fa-solid fa-xmark" onclick="toggleModal('closeButton')"></i>
                <img src="../${response.path}profile_images/${response.tweet_and_user.user_image}" alt="user image" class="user_image">
                <div>
                    <div class="input_content">
                        <input name="tweet_text" type="text" value="${response.tweet_and_user.tweet_text}" data-validate="str" data-min="1" data-max="200">
                        <div class="tweet_image_container hide">
                            <div onclick="removeImage()" class="remove_tweet_image fa-solid fa-xmark"></div>
                            <img alt="tweet image"  class="tweet_image">
                        </div>
                    </div>
                    
                    <div class="image_upload">
                        <label for="tweet_update_image_upload_${randomNumber}">
                            <i class="fa-solid fa-image"></i>
                        </label>
                        <input id="tweet_update_image_upload_${randomNumber}" name="tweet_image" type="file" accept="image/png, image/jpeg, image/jpg" onchange="handleFileInput()">
                    </div>

                    <button onclick="validate(updateTweet)" class="tweet_btn">Update my tweet!</button>
                </div>
                
                </form>
    
        </section>

    </div>
    `;
    console.log(response.tweet_and_user.user_id);
    const url = window.location.href;
    if(url.includes("main") || url.includes(response.tweet_and_user.user_id)){
        console.log("User on main or own page");
        document.querySelector(".main__tweets").insertAdjacentHTML("afterbegin", tweet)
        if(document.querySelector(".tweet_amount span")){
            console.log(document.querySelector(".tweet_amount span").textContent);
            let valueStr = document.querySelector(".tweet_amount span").textContent;
            let valueInt = parseInt(valueStr);
            document.querySelector(".tweet_amount span").textContent = valueInt + 1;
        }
    }

    form.reset()
    form.querySelector(".tweet_image").src = "";
    form.querySelector(".tweet_image_container").classList.add("hide")

    if(form.classList.contains("tweet_header")){
        form.parentElement.parentElement.classList.remove("show");
    }
}