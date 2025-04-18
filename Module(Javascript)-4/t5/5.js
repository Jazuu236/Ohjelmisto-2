async function getJoke() {
    try {
        const response = await fetch("https://api.chucknorris.io/jokes/random");

        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        const data = await response.json();
        console.log(data.value);
    }   catch (error) {
        console.error("Fetch error", error);
    }
}
getJoke();