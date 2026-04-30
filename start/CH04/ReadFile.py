#!/usr/bin/env python3
# Sample script that reads from a file
# By Jordan Peetz
'''
This is a piece of code to read the file i created from the script writefile.ph
'''

#Created loop to openfile and read it contents
with open("hackme.txt", "r") as file:
    contents = file.read()
print("here is someone to hack - info dump")
print(contents)