window.addEventListener("load", init)

function init(){
    console.log("Page and script loaded");

    if(document.querySelectorAll(".followed")){
        document.querySelectorAll(".followed").forEach(btn => {
            btn.addEventListener("mouseover", () => {
                btn.textContent = "Unfollow"
            })
            btn.addEventListener("mouseout", () => {
                btn.textContent = "Following"
            })
        })
    }
    
}