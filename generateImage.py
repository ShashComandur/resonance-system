# Python program to take in a file, find its SHA512 hash, and turn it into a 2000x2000 truchet tile png
# Hash function sourced from: https://www.programiz.com/python-programming/examples/hash-file

# imports
import hashlib
import pygame

# takes in an mp3, returns its SHA512 hash
def hash_file(filename):
   # make a hash object
   h = hashlib.sha512()

   # open file for reading in binary mode
   with open(filename,'rb') as file:
       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)
   # return the hex representation of digest
   #return bin(int(h.hexdigest(), 16))
   return hextobin(h.hexdigest())

# helper function to convert the hex string to a bin string
def hextobin(h):
  return bin(int(h, 16))[2:].zfill(len(h) * 4)

# generate the 16x16 array to hold the bin substrings
def generateArray(hash):
    # initialize 16x16 double array to hold data for each tile
    arr = [[""]*16 for i in range(16)]
    stringIndex = 0

    # populate array using the hash
    for i in range(16):
        for j in range(16):
            arr[i][j] = hash[stringIndex: stringIndex+2]
            stringIndex += 2
    return arr

def generateImage(arr):

    return

# ------------------------------------------------ testing - move to another file soon 
message = hash_file("../../Everything/Art/Posters/~resonance_system/Music Files/Noisia - Outer Edges/01 - The Approach.mp3")
print("\nThe Approach: " + message + "\n")

arr = generateArray(message)
print(arr)