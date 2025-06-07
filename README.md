# Welcome to my Cloud Server Project #

My name is Jack Pember and my student number is 34394543<br /><br />
[nextwatch.site](https://nextwatch.site/) is the link to my server<br /><br />
*placholder* is the link to my video explainer.

## Documentation ##

The below links will walk you through the creation of my Project.

1.  [Server Creation](/Documentation/ServerCreation.md)<br /><br />
2.  [Website Configuration](/Documentation/WebsiteConfiguration.md)<br /><br />
3.  [Scripting](/Documentation/Scripting.md)<br />

## Script Verifiable Output ##

You will see my server's Script Verifiable Output whenever the following happens:

#### Movie Posters are displayed ####
* When the webpage first loads, a script tag fetches links to movie posters using a bash file that reads from a text file.<br />Both are stored on the server and visible in this repository as the following:<br />  [get_poster.sh](Code/cgi-bin/get_poster.sh)<br />[movie_posters.txt](Code/cgi-bin/movie_posters.txt)

#### Next or Previous buttons are pressed ####
*  Whenever either button is pressed, a script tag will either load the next 3 movie posters or the previous 3 (this works before and after the submit button is pressed)

#### "thumb up" button is pressed ####
*  Whenever any "thumb up" button is pressed, a script tag store a 1 to an array in the same index as which ever movie poster is above the pressed "thumb up" button. Then the button will change colour to green and turn it's corresponding "thumb down" button back to white if it is not already

#### "thumb down" button is pressed ####
*  Exact same as "thumb up" except "thumb down" will store a 0 instead of 1 and will become red if pressed instead of green

#### "Submit Ratings" button is pressed ####
*  Whenever Submit ratings is pressed, a script tag will send an array of 1's, 0's and null's to a CGI script which will process the data. The CGI script will return a string of 10 integers, each integer represents an entry in the array containing movie poster links, the returned string is displayed where the "Submit Ratings" button was. The array of stored poster links will also be updated to only include entries found in the returned string of 10 integers, and the order of the array will be the same as the returned string of 10 integers. Lastly, all "thumb up" and "thumb down" buttons will be hidden.<br />The CGI script and the text file utilized are stored on the server and visible in this repository as the following:<br />  [get_recommendations.cgi](Code/cgi-bin/get_recommendations.cgi)<br />[movie_data.txt](Code/cgi-bin/movie_data.txt)
