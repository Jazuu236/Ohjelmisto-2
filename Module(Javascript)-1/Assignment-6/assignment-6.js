const answer = confirm("Should I calculate the square root?");

if (answer) {
    let number = parseFloat(prompt("Enter number:"));

    if (number < 0) {
        document.body.innerHTML = "The square root of a negative number is not defined.";
    } else {
        let squareroot = Math.sqrt(number);
        document.body.innerHTML = `The square root of ${number} is ${squareroot}`;
    }
} else {
    document.body.innerHTML = "You chose not to calculate the square root!";
}
