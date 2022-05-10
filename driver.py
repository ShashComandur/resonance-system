# This program is the driver for the truchet tile generation.
# It will run through all five albums, and generate the appropriate files for each. 

# imports
import generateImage
import os

# variable declarations
genericFilepath = "..\..\Everything\Art\Posters\~resonance_system\Files\\"
albumNames = ["A$AP Rocky - Testing", "Camo & Krooked - Mosaik", "Flume - Skin", "Lido - Everything", "Noisia - Outer Edges"]
truchetTypes = ["Test", "Triangles", "Circles"]

# create the picture using every mp3 in every album folder
for album in albumNames:
    currentFilepath = genericFilepath + album
    outputFilepath = currentFilepath + "\img\\"
    for filename in os.listdir(currentFilepath):
        f = os.path.join(currentFilepath, filename)
        if os.path.isfile(f):
            # string concatenation nonsense to put all the pictures in the appropriate folders
            beginningSubstring = currentFilepath + "\\"
            newImageFilename = f.replace(currentFilepath+album, "")[:-4] +".png"
            newImageFilename = newImageFilename[len(beginningSubstring):]
            generateImage.truchetGenerator(f, currentFilepath + "\\img\\" + newImageFilename, truchetTypes[2])


