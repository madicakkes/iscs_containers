document.addEventListener("keydown", function(event){
  if(event.key == "Enter"){
    const form_Submit_Button = document.getElementById("submit");
    const all = document.querySelector("*");
    all.style.cursor = "wait";
    setTimeout(()=>{form_Submit_Button.click()}, 2000);
  }
})
