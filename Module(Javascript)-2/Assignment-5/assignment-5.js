function numbers() {
    var numbersArray = [];
    var number;

    do {
        number = prompt("Enter a number:");

        number = parseInt(number);

        if (numbersArray.includes(number)) {
            alert(`The number ${number} has already been entered.`);
            break;
        } else if (!isNaN(number) && number !== 0) {
            numbersArray.push(number);
        }

    } while (true);

    if (numbersArray.length > 0) {
        numbersArray.sort((a, b) => a - b);

        console.log("Numbers in ascending order:");
        numbersArray.forEach(num => {
            console.log(num);
        });

        let ul = document.createElement('ul');

        numbersArray.forEach(num => {
            let li = document.createElement('li');
            li.textContent = num;
            ul.appendChild(li);
        });

        document.body.appendChild(ul);

    } else {
        alert("No valid numbers were entered.");
    }
}

numbers();
