#!/bin/bash

echo "Content-type: text/plain"
echo ""

while IFS= read -r line; do
  echo "$line"
done < movie_posters.txt
