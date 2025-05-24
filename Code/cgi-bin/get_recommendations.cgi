#!/usr/bin/env python3

import numpy as np
import cgi
import os
import cgitb
import csv

cgitb.enable()

form = cgi.FieldStorage()
dataString = form.getvalue('data')

print("Content-Type: text/html")
print()
print("<html><body>")
print("<h1>Data Received</h1>")
print(f"<p>Data: {dataString}</p>")

dataString = "1,1,1,0,,,,,," 
dataArray = dataString.split(',')
print(f"<p>Data: {dataArray}</p>")
movieIndex = 0
unratedMovies = [] *len(dataArray)
for i in range(len(dataArray)):
	if dataArray[i] != '':
		dataArray[i] = int(dataArray[i])
recommendedMovies = []
#print(f"<p>Data: {dataArray}</p>")

def genres_ranked():
	genresSorted = np.argsort(genrePoints)[::-1]
	print(f"<p>Sorted Genres: {genresSorted}</p>")

def show_recommended_movies():
	with open('../cgi-bin/movie_data.txt', 'r') as file:
		while True:
			storedMovieData = file.readline()
			if not storedMovieData:
				break


	print(f"<p>Recommended Movies: {recommendedMovies}</p>")


with open('../cgi-bin/movie_data.txt', 'r') as file:
	while True:
		storedMovieData = file.readline()
		if not storedMovieData:
			break
		currentDataArrayStrings = [int(x) for x in next(csv.reader([storedMovieData]))]
		currentDataArrayInts = np.array(currentDataArrayStrings, dtype=int)
		#print(f"<p>currentDataArrayInts: {currentDataArrayInts}</p>")
		if movieIndex == 0:
			genrePoints = np.zeros(currentDataArrayInts.shape, dtype=int)
		#print(f"<p>genrePoints: {genrePoints}, {movieIndex}</p>")
		if dataArray[movieIndex] == 1:
			for i in range(len(currentDataArrayInts)):
				genrePoints[i] += currentDataArrayInts[i]
		elif dataArray[movieIndex] == 0:
			for i in range(len(currentDataArrayInts)):
				genrePoints[i] -= currentDataArrayInts[i]
		elif dataArray[movieIndex] == '':
			unratedMovies.append(movieIndex)
		#print(f"<p>genre points total: {genrePoints}, {movieIndex}</p>")
		movieIndex += 1

print(f"<p>Genre Points: {genrePoints}</p>")
print(f"<p>Unrated Movies: {unratedMovies}</p>")

genres_ranked()

print("</body></html>")
print("Status: 302 Found")
print("Location: ../html/recommendations.html")
print()
