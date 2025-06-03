#!/usr/bin/env python3

import numpy as np
import cgi
import os
import cgitb
import csv

cgitb.enable()

form = cgi.FieldStorage()
dataString = form.getvalue('data')

print("Content-Type: text/plain")
print()

dataArray = dataString.split(',')
movieIndex = 0
unratedMoviesIndex = 0
genresSortedIndex = 0
genresSorted = np.array([])
unratedMovies = np.empty((0,))
for i in range(len(dataArray)):
	if dataArray[i] != '':
		dataArray[i] = int(dataArray[i])

def show_recommendations():
	movieIndex = 0
	ratingRowIndex = 0
	with open('movie_data.txt', 'r') as file:
		while True:
			storedMovieData = file.readline()
			if not storedMovieData:
				break
			currentDataArrayStrings = [int(x) for x in next(csv.reader([storedMovieData]))]
			currentDataArrayInts = np.array(currentDataArrayStrings, dtype=int)

			if movieIndex == 0:
				numberOfGenres = currentDataArrayInts.size
				movieGenrePreference = np.zeros((len(unratedMovies), numberOfGenres), dtype=int)

			matchUnratedMovies = np.any(unratedMovies == movieIndex)
			if matchUnratedMovies:
				movieGenrePreference[ratingRowIndex, :] = currentDataArrayInts
				ratingRowIndex += 1
			movieIndex += 1

	sortedMoviePreference = np.empty_like(movieGenrePreference)
	genresSorted = np.argsort(genrePoints)[::-1]
	for row in range(movieGenrePreference.shape[0]):
		for i in range(movieGenrePreference.shape[1]):
			sortedMoviePreference[row][i] = movieGenrePreference[row][genresSorted[i]]

	topThreeSorted = []
	for col in range(sortedMoviePreference.shape[1]):
		topThree = np.argsort(sortedMoviePreference[:, col])[-3:][::-1]
		topThreeSorted.append(topThree)
	topThreeRecommended = np.array(topThreeSorted)

	topTenSorted = np.empty(10, dtype='int')
	topTenCounter = 0
	for row in range(topThreeRecommended.shape[0]):
		for i in range(topThreeRecommended.shape[1]):
			if topTenCounter >= (len(topTenSorted)):
				break
			duplicateFinder = topThreeRecommended[row][i]
			if i == 0 and row == 0:
				topTenSorted[topTenCounter] = duplicateFinder
				topTenCounter += 1
			else:
				duplicateFound = np.any(topTenSorted == duplicateFinder)
				if not duplicateFound and ((i != 0) or (row != 0)):
					topTenSorted[topTenCounter] = duplicateFinder
					topTenCounter += 1

	topTenRecommended = np.empty(10,)
	topTenSortedIndex = 0
	for i in topTenSorted:
		topTenRecommended[topTenSortedIndex] = unratedMovies[i]
		topTenSortedIndex += 1

	print(','.join(map(str, topTenRecommended)))

with open('movie_data.txt', 'r') as file:
	while True:
		storedMovieData = file.readline()
		if not storedMovieData:
			break
		currentDataArrayStrings = [int(x) for x in next(csv.reader([storedMovieData]))]
		currentDataArrayInts = np.array(currentDataArrayStrings, dtype=int)
		if movieIndex == 0:
			genrePoints = np.zeros(currentDataArrayInts.shape, dtype=int)
		if dataArray[movieIndex] == 1:
			for i in range(len(currentDataArrayInts)):
				genrePoints[i] += currentDataArrayInts[i]
		elif dataArray[movieIndex] == 0:
			for i in range(len(currentDataArrayInts)):
				genrePoints[i] -= currentDataArrayInts[i]
		elif dataArray[movieIndex] == '':
			unratedMovies.resize((unratedMoviesIndex + 1,))
			unratedMovies[unratedMoviesIndex] = movieIndex
			unratedMoviesIndex += 1
		movieIndex += 1

show_recommendations()
