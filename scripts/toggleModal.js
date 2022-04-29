function toggleModal(modal){
    console.log("Modal");
    if (modal == "signup"){
        document.querySelector("#sign_up").classList.add("show_flex");

    } else if(modal == "login"){
        document.querySelector("#sign_up").classList.remove("show_flex");
        document.querySelector("#log_in").classList.add("show_flex");

    } else if(modal == "update"){
        console.log(event.target.form.parentElement.querySelector(".tweet_update"));
        event.target.form.parentElement.querySelector(".tweet_update").classList.add("show_flex");

    } else if(modal == "tweet"){
        console.log(event.target.parentElement.parentElement.querySelector(".tweet_header"));
        event.target.parentElement.parentElement.querySelector(".tweet_header").classList.add("show");

    }  else if(modal == "menu"){
        document.querySelector(".header_menu_modal").classList.add("show");

    } else if(modal == "search"){
        document.querySelector(".search_box").classList.add("show");
        document.addEventListener('mousedown', function(e) {
            const container = document.querySelector('.search_box');
            if (!container.contains(e.target)) {
                container.classList.remove("show")
            }
        });

    } else if(modal == "followers"){
        document.querySelector(".followers_box").classList.add("show");
        document.querySelector(".followers_box+svg").classList.add("show");
        document.addEventListener('mousedown', function(e) {
            const container = document.querySelector('.followers_box');
            if (!container.contains(e.target)) {
                container.classList.remove("show");
                document.querySelector(".followers_box+svg").classList.remove("show");
            }
        });

    } else if(modal == "following"){
        document.querySelector(".following_box").classList.add("show");
        document.querySelector(".following_box+svg").classList.add("show");
        document.addEventListener('mousedown', function(e) {
            const container = document.querySelector('.following_box');
            if (!container.contains(e.target)) {
                container.classList.remove("show");
                document.querySelector(".following_box+svg").classList.remove("show");
            }
        });

    }else if(modal == "close"){
        console.log(event.target)
        event.target.parentElement.classList.remove("show_flex");
        event.target.parentElement.classList.remove("show");

    } else if(modal == "closeButton"){
        console.log(event.target)
        event.target.parentElement.parentElement.classList.remove("show_flex");
        event.target.parentElement.parentElement.classList.remove("show");
    }
}