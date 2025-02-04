let selection_link = document.getElementsByClassName("selection_link");
for(let i = 0; i < selection_link.length; i++){
    let selection = selection_link[i].parentElement;
    selection.addEventListener("click", function(){
        selection_link[i].click();
    })

}

