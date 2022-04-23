async function handleFollow(){
    console.log("You followed someone!");
    const user = event.target.parentElement;
    console.log(user);

    const followBtn = event.target;

    const user_id = user.querySelector("input").value;
    console.log(user_id);

    if(!followBtn.classList.contains("followed")){
        console.log("You followed this user");
        followBtn.classList.toggle("followed");
        followBtn.textContent = "Following";
        init()

        const connection = await fetch("/follows/" + user_id, {
            method: "POST",
        });
        return

    } else{
        console.log("You unfollowed this user");
        followBtn.classList.toggle("followed");
        followBtn.addEventListener("mouseover", () => {
            followBtn.textContent = "Follow";
        })
        followBtn.addEventListener("mouseout", () => {
            followBtn.textContent = "Follow";
        })
        followBtn.textContent = "Follow";

        const connection = await fetch("/unfollows/" + user_id, {
            method: "DELETE",
        });
        return
    }

}