# Course: CS361 - Software Engineering 1
# Author: Jana Dalyn Boyd
# Assignment: Microservice
# Description: Writes the URL of a random image to a text file.

import random

# repeat while site is live
while True:
    
    # look for run command
    instruct_file = open("instructions.txt", "r")
    if instruct_file.readline() == 'run':
        instruct_file.close()
        instruct_file = open("instructions.txt", "w")
        instruct_file.write("")
        instruct_file.close()
        
        # generate random number
        random.seed(a=None, version=2)
        ran_num = random.randint(1, 7)

        # open file & write URL
        img_url = open("img_url.txt", "w")
        img_url.write("microservice/" + str(ran_num) + ".jpg")
        img_url.close()