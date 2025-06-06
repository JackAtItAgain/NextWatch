# Scripting #

### In this walkthrough we will: ###
1. Install python3 and numpy for scripts
2. Html creation
3. Cgi creation
4. Set file permissions

## Install python3 and numpy for scripts ##

1.	Use command “sudo apt install python3-numpy”

## Html creation ##

1.	Create a custom html index file, include a basic layout and design.
2.	Make 2 buttons, position them side by side and in the centre of the page, one to scroll left and one right.
3.	Make 3 image tags, position them side by side and in between the scroll buttons.
4.	Make 2 buttons for each image tag, the thumbsUp and thumbsDown buttons, position each pair shoulder to shoulder just beneath the corresponding image tag.
5.	Make 1 button, this will be our submit button, position it below thumbsUp and Down buttons in the centre of the page.
6.	 Fetch the movie poster links with a simple bash file.
 
7.	Read the movie poster links into an array.
8.	Set the 3 image tags to the first 3 movies.
9.	Whenever scroll button is pressed display next 3 movies, I use an index to keep track of which movie’s we are displaying.
 
10.	Whenever a thumbsUp or thumbsDown button is pressed store 1 (thumbsUp) or 0 (thumbsDown) to an array with the same index as current displayed movies.
11.	Whenever submit button is pressed send the array of user movie ratings to cgi file via post and await response.
12.	Response will be a string of integers with each integer representing the index of the array of movie poster links.
13.	Convert the response string into an array and overwrite the existing array of movie poster links with each movie poster link in accordance with the response array.
 
(Here recommendedMovies is the response array and images is the array of movie poster links)
14.	Then hide the thumbsUp, thumbsDown and submit buttons and refresh the displayed posters.

## Cgi creation ##

CGI CREATION
The goal of the cgi script (get_recommendations.cgi) is to take a string of 1’s, 0’s and null’s and calculate the user’s favourite genres and to order genres by user’s favourites preference. Then find the movie that scores the highest on the user’s favourite genres and store the index of that movie into the first index of the result array. Then find the second highest movie and store that movie into the second index of the result array. Continue this process while ignoring duplicate movies until the result array has 10 movie indexes. Then return the result array.
1.	Read received string and put it into an array (This will be our dataArray)
2.	Open movie_data.txt (the file containing each movie’s genre scores) and read the first line into an array. (Each line is a list of integers between 0 and 9 corresponding to how much the specific movie is considered that genre)
3.	If the line read index of dataArray has a rating, 1 or 0, either, add or subtract the line array from another array called genrePoints 
4.	If the line read index of dataArray has no rating add that index to an array called unratedMovies
5.	Loop through all lines of movie_data.txt
6.	genrePoints should now according to this method be an array of points, each index represents how much a user like a genre. unratedMovies should now be an array of all movies the user has not rated
7.	Make a new array movieGenrePreference and write the index of the highest scoring genre in genrePoints to the first index of movieGenrePreference, then the second highest scoring genre to the second index and so on until genres are sorted by the user’s preference.
8.	Read movie_data.txt into a 2d array and then use unratedMovies and movieGenrePreference to find the top 3 unrated movies with the highest score in the user’s favourite genre. Write the top 3 of each genre into a 2d array
9.	Loop through the top 3 of each genre and write the first entry into a 1d array called topTenSorted, then the second, until there are 10 entries, make sure to ignore any duplicates
10.	Turn topTenSorted into a string and return the string

## Set file permissions ##

1.	Make sure to set get_poster.sh and get_recommendations.cgi so they are executable, use “sudo chmod 755 ‘path_to_file’”

## Summary ##
