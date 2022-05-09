# Python program to take in a file, find its SHA512 hash, and turn it into a 2000x2000 truchet tile png
# Hash function sourced from: https://www.programiz.com/python-programming/examples/hash-file

# imports
import hashlib
from PIL import Image

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

# generate the image from the hash
def generateImage(arr, imageFilepath, truchetType):
    # initialize canvas
    img = Image.new('RGBA', (2000, 2000), color = 'red')

    # loop through array, set color and write to image based on value
    for i in range(16):
        for j in range(16):
            if (arr[j][i] == "00"):
                cell = Image.open("Truchet Tiles/" + truchetType + "/1.png")
            elif (arr[j][i] == "01"):
                cell = Image.open("Truchet Tiles/" + truchetType + "/2.png")
            elif (arr[j][i] == "10"):
                cell = Image.open("Truchet Tiles/" + truchetType + "/3.png")
            elif (arr[j][i] == "11"):
                cell = Image.open("Truchet Tiles/" + truchetType + "/4.png")

            # paste the cell in to the proper coordinates
            img.paste(cell, (i*125, j*125), cell)
    
    # write to file
    img.save(imageFilepath)
    return

# put it all together!
def truchetGenerator(songFilepath, imageFilepath, truchetType):
    hash = hash_file(songFilepath)
    arr = generateArray(hash)
    print(arr)
    generateImage(arr, imageFilepath, truchetType)

# ------------------------------------------------ testing - move to another file soon 
# hash = hash_file("../../Everything/Art/Posters/~resonance_system/Music Files/Noisia - Outer Edges/02 - Anomaly.mp3")
# print(hash)

# arr = generateArray(hash)
# print(arr)

# generateImage(arr)

truchetGenerator("../../Everything/Art/Posters/~resonance_system/Music Files/Noisia - Outer Edges/03 - Collider.mp3", "collider.png", "Test")