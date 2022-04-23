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

    } else if(modal == "close"){
        console.log(event.target)
        event.target.parentElement.classList.remove("show_flex");
        event.target.parentElement.classList.remove("show");

    } else if(modal == "closeButton"){
        console.log(event.target)
        event.target.parentElement.parentElement.classList.remove("show_flex");
        event.target.parentElement.parentElement.classList.remove("show");
    }
}