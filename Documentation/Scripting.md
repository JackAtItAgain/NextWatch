# Scripting #

### In this walkthrough we will: ###
1. Install Python3 and Numpy for Scripts
2. HTML Creation
3. CGI Creation
4. Setting File Permissions

It's important to note that while a walkthrough, this section conceptualises the scripting components as oppose to serving as a guide for exactly what to write. 
If this were a guide for exactly what to write, it would serve no purpose since the code files are located in this repository and can be simply copied onto a server without the need for explaination.
Therefore, the sections [HTML Creation](#html-creation) and [CGI Creation](#cgi-creation) attempt to explain the approach the scripts take in delivering content.

## Install Python3 and Numpy for Scripts ##
Later we will create a CGI file that will run on Python and will also need the Numpy library installed

1.	In the terminal of your Cloud Server use the command:

    ```
      sudo apt install python3-numpy
    ```
## HTML Creation ##
The html will be a single index.html file with javascript being utilized. The goal is to display images of movie posters, provided via a bash file that reads the links from a .txt file. The html will temporarily store the user’s ratings whenever a thumbs up or thumbs down button is pressed. When the user wants to submit ratings, the html should send the user’s rating to a .cgi file that will return a string of indexes. That returned string of indexes can be used to display movie posters of unwatched movies, ordered by the likelihood the user will enjoy, which is determined by the .cgi file.

1.	Create a new HTML file called index.html, include a basic layout and design (my chosen layout is outlined in steps 2-5)
2.	Make 2 buttons, position them side by side and in the centre of the page, one to see next and one to see previous
3.	Make 3 image tags, position them side by side and in between the next and previous buttons
4.	Make 2 buttons for each image tag, the thumbsUp and thumbsDown buttons, position each pair shoulder to shoulder just beneath the corresponding image tag
5.	Make 1 button, this will be our submit button, position it below thumbsUp and Down buttons in the centre of the page
6.	Fetch the movie poster links with a simple bash file (see image below), store bash file in var/www/cgi-bin<br /><br /><img src="https://github.com/JackAtItAgain/NextWatch/blob/main/Documentation/VisualAids/PosterDisplay1.png?raw=true" width="300">
7.	Read the movie poster links into an array
8.	Set the 3 image tag's source to the first 3 movies
9.	Whenever the next button is pressed display the next 3 movies and the previous 3 movies for previous, I use an index to keep track of which movies are currently displayed<br /><br /><img src="https://github.com/JackAtItAgain/NextWatch/blob/main/Documentation/VisualAids/PosterDisplay2.png?raw=true" width="500">
10.	Whenever a thumbsUp or thumbsDown button is pressed, store (1 for thumbsUp or 0 for thumbsDown) to an array with the same index as current displayed movies
11.	Whenever the submit button is pressed, send the array that is storing (thumbsUp or thumbsDown) to each movie to a CGI file via post and await response (we will create the CGI file in the next section)
12.	The response from the CGI file will be a string of 10 integers seperated by commas. If you use the first integer to index the array containing movie poster links, that movie is what the highest recommended by the CGI file. The second integer in the response string will give the 2nd highest recommended movie and so on until you have 10 movies ordered
13.	Convert the response string into an array and overwrite the existing array of movie poster links with the 10 ordered movie poster links that is described in the previous step (this my method)<br /><br /><img src="https://github.com/JackAtItAgain/NextWatch/blob/main/Documentation/VisualAids/PosterDisplay3.png?raw=true" width="400"><br />(In the example above, "recommendedMovies" is the response string converted to an array and "images" is the array of movie poster links)
14.	Then hide the thumbsUp, thumbsDown and submit buttons and refresh the displayed posters

## CGI Creation ##

The goal of the CGI script (get_recommendations.cgi) is to take a string of 1’s, 0’s and null’s and calculate the user’s favourite genres and to order genres by the user’s preference (which is determined by the method in this section). Then find the movie that scores the highest on the user’s favourite genres and store the index of that movie into the first index of the result array. Then find the second highest movie and store that movie into the second index of the result array. Continue this process while ignoring duplicate movies until the result array has 10 movie indexes, then convert the result array into a string seperated by commas and return the string.

I have used Python as my coding language of choice in my CGI script since I am more familair with it. Therefore, just a reminder that the exact approach taken below will need adapting for use in another language.

1.	Read received string and put it into an array (this will be our dataArray)
2.	Open movie_data.txt (the file containing each movie’s genre scores) and read the first line into an array (each line is a list of integers between 0 and 9 corresponding to how much the specific movie is considered that genre)<br /><br />(Referenced below is movie_data.txt displayed as an excel file but the first column (titles) and row (genres) are only for visual aid and are excluded from the .txt file)<br /><br /><img src="https://github.com/JackAtItAgain/NextWatch/blob/main/Documentation/VisualAids/MovieData.png?raw=true" width="900">
3. Create 2 arrays, first called genrePoints which is filled with zeros and has the same size as the array containing the current line. The second array is called unratedMovies with no size specified (we will append this size of unratedMovies as needed)
5.	If the entry of dataArray that corresponds to the current line (dataArray[0] corresponds to first line, dataArray[1] corresponds to second line, and so on) has a value of 1 (add each entry of the current line to genrePoints). If the value is 0 (subtract each entry of the current line from the array genrePoints)
6.	But if the entry of dataArray is null append an additional entry to unratedMovies with the value of the current movie index
7.	Loop through all lines of movie_data.txt
8.	After there are no more lines of movie_data.txt, genrePoints should now be an array of total points for each genre, the higher the points in an entry the more we assume the user likes that genre. unratedMovies should now be an array containing all movies the user has not rated
9.	Make a new array movieGenrePreference and store the index of the highest scoring genre in genrePoints to the first index of movieGenrePreference, then the second highest scoring genre to the second index and so on until genres are sorted by the user’s preference in movieGenrePreference
10.	Read movie_data.txt into a 2d array and then use unratedMovies and movieGenrePreference to find the top 3 unrated movies with the highest score in the user’s favourite genre. Write the top 3 of each genre into a 2d array
11.	Loop through the top 3 of each genre and store each entry as they appear into a 1d array called topTenSorted, until there are 10 entries, make sure to ignore any duplicate entries
12.	Convert topTenSorted into a string with values seperated by commas and return the string to HTML

## Setting File Permissions ##

1.	Make sure to set the created bash and cgi files so they are executable, use the command:

    ```
      sudo chmod 755 "path_to_file"
    ```

## Summary ##

After you have completed this and the previous walkthroughs you should have a working Website that sends user input to the server to determine which unrated movies they are most likely to enjoy.
