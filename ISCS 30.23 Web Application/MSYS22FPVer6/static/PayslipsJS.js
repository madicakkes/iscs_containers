console.log("JS LOADED");
const payslips = document.getElementsByClassName("payslip_data");
for(let i = 1; i < payslips.length; i+=2){
  payslips[i].style.backgroundColor = "rgb(220, 220, 220)";
  payslips[i].addEventListener("mouseover", ()=> {payslips[i].style.backgroundColor = "rgb(200, 200, 200)";})
  payslips[i].addEventListener("mouseout", ()=> {payslips[i].style.backgroundColor = "rgb(220, 220, 220)";})
}

for(let i = 2; i < payslips.length; i+=2){
  payslips[i].style.backgroundColor = "rgb(260, 260, 260)";
  payslips[i].addEventListener("mouseover", ()=> {payslips[i].style.backgroundColor = "rgb(245, 245, 245)";})
  payslips[i].addEventListener("mouseout", ()=> {payslips[i].style.backgroundColor = "rgb(260, 260, 260)";})
}

const all_ids = document.getElementsByClassName("payslip_idNumber");
for(i = 0; i < all_ids.length; i++){
  let text = all_ids[i].textContent;
  let pad = text.padStart(6, "0");
  all_ids[i].textContent = pad;
}
