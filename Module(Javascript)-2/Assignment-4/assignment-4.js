function numbers() {
    var numbersArray = [];
    var number;

    do {
        number = prompt("Enter a number or 0 to stop:");

        number = parseInt(number);

        if (number !== 0 && !isNaN(number)) {
            numbersArray.push(number);
        }

    } while (number !== 0);

    if (numbersArray.length > 0) {
        numbersArray.sort((a, b) => b - a);

        console.log("Numbers from largest to smallest:");
        numbersArray.forEach(num => {
            console.log(num);
        });

        document.body.innerHTML += "<p>Numbers from largest to smallest: </p><ul>";
        numbersArray.forEach(num => {
            document.body.innerHTML += "<li>" + num + "</li>";
        });
        document.body.innerHTML += "</ul>";
    } else {
        alert("No valid numbers were entered.");
        document.body.innerHTML += "<p>No valid numbers were entered.</p>";
    }
}

numbers();
