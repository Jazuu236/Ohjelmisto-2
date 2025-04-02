let num1 = parseInt(prompt("Enter first number:"));
let num2 = parseInt(prompt("Enter second number:"));
let num3 = parseInt(prompt("Enter third number:"));

let sum = num1 + num2 + num3;
let product = num1 * num2 * num3;
let average = sum / 3;

document.body.innerHTML += `<h1>Sum: ${sum}</h1>`;
document.body.innerHTML += `<h1>Product: ${product}</h1>`;
document.body.innerHTML += `<h1>Average: ${average}</h1>`;
