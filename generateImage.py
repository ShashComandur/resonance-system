# Python program to take in a file, find its SHA256 hash, and turn it into a 2000x2000 truchet pattern png
# Hashing function sourced from https://www.programiz.com/python-programming/examples/hash-file

# imports
import hashlib

# takes in an mp3, returns its SHA256
def hash_file(filename):

   # make a hash object
   h = hashlib.sha256()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

def truchet(hash):

    return

# testing - move to another file soon
message = hash_file("../../Everything/Art/Posters/~resonance_system/Music Files/Noisia - Outer Edges/01 - The Approach.mp3")
print("\nThe Approach: " + message + "\n")