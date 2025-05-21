#!/bin/bash

# Read the input from the form
read username
read password

# Store the credentials in a file
echo "Username: $username" >> credentials.txt
echo "Password: $password" >> credentials.txt

# Provide feedback
echo "Credentials stored successfully."