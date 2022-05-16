# Python program to take in a file, find its SHA512 hash, and turn it into a 2000x2000 truchet tile png
# Hash function sourced from: https://www.programiz.com/python-programming/examples/hash-file

# imports
import hashlib
from PIL import Image

# takes in an mp3, returns its SHA512 hash
def hashFile(filename):
   # make a hash object
   h = hashlib.sha512()
   # open file for reading in binary mode
   with open(filename,'rb') as file:
       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read  1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)
   # return the hex representation of digest
   return hextobin(h.hexdigest())

# helper function - takes in a hex string, returns it in binary
def hextobin(h):
  return bin(int(h, 16))[2:].zfill(len(h) * 4)

# takes in the SHA512 hash string in binary, returns it in an double array, with each space containing two bits
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

# takes in the hash array, generates the image, writes it to the input filepath
# truchetType is also an input, to specify the set of images to use
def generateImage(arr, imageFilepath, truchetType):
    # initialize canvas, with full transparency
    img = Image.new('RGBA', (2000, 2000), color = 'red')
    img.putalpha(0)

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
    hash = hashFile(songFilepath)
    arr = generateArray(hash)
    generateImage(arr, imageFilepath, truchetType)
