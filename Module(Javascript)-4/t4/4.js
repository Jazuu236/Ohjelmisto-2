document.querySelector("form").addEventListener("submit", async function(e) {
    e.preventDefault();

    const query = document.getElementById("query").value;
    if (!query) return;

    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`);
    
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();

        const results = document.getElementById("results");
        results.innerHTML = "";

        data.forEach(item => {
            const show = item.show;

            const article = document.createElement("article");

            const nameElement = document.createElement("h2");
            nameElement.textContent = show.name;
            article.appendChild(nameElement);

            const linkElement = document.createElement("a");
            linkElement.href = show.url;
            linkElement.target = "_blank";
            linkElement.textContent = "More details";
            article.appendChild(linkElement);

            const imageElement = document.createElement("img");
            imageElement.src = show.image ? show.image.medium : "https://via.placeholder.com/210x295?text=Not%20Found";
            imageElement.alt = show.name;
            article.appendChild(imageElement);

            const summaryElement = document.createElement("div");
            summaryElement.innerHTML = show.summary ? show.summary.replace(/<[^>]*>/g, '') : 'No summary available.';
            article.appendChild(summaryElement);

            results.appendChild(article);
        });

    } catch (error) {
        console.error('Fetch error:', error);
    }
});
