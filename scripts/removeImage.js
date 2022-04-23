function removeImage(){
    console.log("Removing image");
    const image = event.target.parentElement;
    console.log(image);

    const image_input = event.target.parentElement.parentElement.parentElement.querySelector("input[type=file]");
    console.log(image_input);

    image.classList.add("hide");
    image_input.value = "";
}