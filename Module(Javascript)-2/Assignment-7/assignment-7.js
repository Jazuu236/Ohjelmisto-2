function rollDice(sides) {
    return Math.floor(Math.random() * sides) + 1;
}

function main() {
    let sides = parseInt(prompt("Give number of sides:"));

    if (isNaN(sides) || sides <2){
        alert("Invalide input.")
        return;
    }

    let roll;
    let rollList = document.createElement("ul");
    document.body.appendChild(rollList);

    do {
        roll = rollDice(sides);
        let listItem = document.createElement("li");
        listItem.textContent = `Rolled: ${roll}`;
        rollList.appendChild(listItem);
    } while (roll !== sides);
}

document.addEventListener("DOMContentLoaded", main);
