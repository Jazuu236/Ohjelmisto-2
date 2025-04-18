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

      console.log("Search Results:");
      data.forEach(item => {
          const show = item.show;
          console.log(`Name: ${show.name}`);
          console.log(`Genres: ${show.genres.join(", ") || "N/A"}`);
          console.log(`Summary: ${show.summary ? show.summary.replace(/<[^>]*>/g, '') : "No summary available."}`);
          console.log('----------------------');
      });

  } catch (error) {
      console.error('Fetch error:', error);
  }
});
