const header = document.getElementById("header");
const footer = document.getElementById("footer");

const id_number = document.getElementById("id_number");
  id_number.textContent = id_number.textContent.trim().padStart(6, "0"); 



function disappear_header(){
    header.style.visibility = "hidden";
    console.log(header.style);
}

function disappear_footer(){
    footer.style.visibility = "hidden";
    console.log(footer.style);
}



function reappear(){
    header.style.visibility = "visible";
    footer.style.visibility = "visible";
}

document.addEventListener("keydown", function(event){
    if(event.key == "p"){
        disappear_header();
        disappear_footer();
        print();
        reappear();
    }
})

window.alert("Press P to Print Document");

