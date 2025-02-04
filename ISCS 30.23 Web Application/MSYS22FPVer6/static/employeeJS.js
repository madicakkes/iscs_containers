const employees = document.getElementsByClassName("employee_data");
console.log(employees);
for(let i = 1; i < employees.length; i+=2){
  employees[i].style.backgroundColor = "rgb(220, 220, 220)";
  employees[i].addEventListener("mouseover", ()=> {employees[i].style.backgroundColor = "rgb(200, 200, 200)";})
  employees[i].addEventListener("mouseout", ()=> {employees[i].style.backgroundColor = "rgb(220, 220, 220)";})
}

for(let i = 2; i < employees.length; i+=2){
  employees[i].style.backgroundColor = "rgb(260, 260, 260)";
  employees[i].addEventListener("mouseover", ()=> {employees[i].style.backgroundColor = "rgb(245, 245, 245)";})
  employees[i].addEventListener("mouseout", ()=> {employees[i].style.backgroundColor = "rgb(260, 260, 260)";})
}

const all_ids = document.getElementsByClassName("employee_idNumber");
console.log(all_ids);
console.log("updated");
for(i = 0; i < all_ids.length; i++){
  let text = all_ids[i].textContent.trim();
  let pad = text.padStart(6, "0");
  all_ids[i].textContent = pad;
  console.log(`all_ids ${i} incremented`);
}
