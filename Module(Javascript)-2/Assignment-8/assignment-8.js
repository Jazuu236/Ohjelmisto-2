function concat(stringsArray) {
    let result = "";

    for (let i =0; i < stringsArray.length; i++) {
        result += stringsArray[i]
    }
    return result;
}

const names = ["Johnny", "DeeDee", "Joey", "Marky"];
const concatenatedString = concat(names);

document.body.innerHTML = `<p>${concatenatedString}</p>`;
