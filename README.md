# movie-rating
Tool that outputs a movie's RottenTomatoes and IMDb score by sifting through webpage HTMLs with regex.

This is a work in progress at the moment.

  Grabbing RottenTomatoes scores currently works for relatively unique movie titles (e.g Iron Man, Lady Bird, or Slumdog Millionaire). More "generic" movie titles (e.g Parasite) proves to be a little trickier due to multiple movies having the same title. Generally, RottenTomatoes differentiates between two or more identically-titled movies with the addition of its year of release. Beyond that, there are issues with URL nomenclature inconsistencies, so I'll have to closer look into it or try and utilize the website's search function.

  Scraping IMDb pages calls for a slightly different method. Due to the fact that each movie is indexed under its own 7 to 8-digit ID code on IMDb, my code currently utilizes IMDb's own search function to obtain those ID codes. However, relying on the website's search function presents the issue of identically-titled movies. The code currently extracts the ID of the first search result, which becomes a problem when your desired result is further down the list. An example of this is when inputting "The Lion King", the IMDb function pulls the ID of the first result, the movie released in 2019, but will not pull the ID of the older film released in 1994.
