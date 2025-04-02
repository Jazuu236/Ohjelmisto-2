function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}
let hn =getRandomInt(4);

let name = prompt("What is your name?");

switch (hn) {
    case 0:
        house = "Gryffindor";
        break;
    case 1:
        house = "Slytherin";
        break;
    case 2:
        house = "Hufflepuff";
        break;
    case 3:
        house = "Ravenclaw";
        break;

}
document.body.innerHTML += `<h1>${name}, you are in ${house}!</h1>`;