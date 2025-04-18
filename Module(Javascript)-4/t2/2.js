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

      console.log(data);
      
  } catch (error) {
      console.error('Fetch error:', error);
  }
});
