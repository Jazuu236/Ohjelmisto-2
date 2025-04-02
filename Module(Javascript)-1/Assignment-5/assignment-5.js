let year = parseInt(prompt("Give year"));

function leapyear(year) {
    if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
        return true;
    } else {
        return false;
    }
}

document.body.innerHTML += `<h1>${year} is a leap year: ${leapyear(year)}</h1>`;
