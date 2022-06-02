# Course: CS361 - Software Engineering 1
# Author: Jana Dalyn Boyd
# Assignment: Microservice
# Description: Writes the URL of a random image to a text file.

Files Included (place in the same directory as your main project)

micro.py
    looks for the word 'run in a file named 'instructions.txt,'
    generated a random number, uses that number to choose a random image,
    writes the url of that image to a file named 'img_url.txt'

instructions.txt
    your main project file should write the word 'run' to this file when it needs an image url
    'micro.py' will read the word 'run' and do the above actions

img_url.txt
    'micro.py' will write the url of the image to be displayed to this file
    your main project file should read this url

racquet_image.txt
    list of racquet urls