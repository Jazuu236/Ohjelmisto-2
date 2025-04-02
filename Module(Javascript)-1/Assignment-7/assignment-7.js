let numdice = parseInt(prompt("How many dice rolls?"));
if (isNaN(numdice) || numdice <= 0) {
    alert("Please enter number over 0!");
} else {
    let sum = 0;
    for (let i = 0; i < numdice; i++) {
        let roll = Math.floor(Math.random()*6 + 1);
        sum += roll;
    }
    console.log("Total sum of dice rolls:", sum);
    document.body.innerHTML = `The total sum of ${numdice} dice rolls is: ${sum}`;
}