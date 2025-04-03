function rollDice() {
    return Math.floor(Math.random() * 6) + 1;
}

function main() {
    let roll;
    let rollList = document.createElement("ul");
    document.body.appendChild(rollList);

    do {
        roll = rollDice();
        let listItem = document.createElement("li");
        listItem.textContent = `Rolled: ${roll}`;
        rollList.appendChild(listItem);
    } while (roll !== 6);
}

document.addEventListener("DOMContentLoaded", main);
