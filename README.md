# Resonance System
This is repository houses the code I used to finish my new art series, Resonance System.

### Author
Shash Comandur
shashcomandur.com
Email: shashank.comandur@gmail.com

# About
I wanted to create an series of pieces to commemorate my five favorite albums of all time. These albums, in ranked
order, are as follows:

1. [Noisia - Outer Edges](https://open.spotify.com/album/73TmwDD6mBOZh6sF9sKXZo?si=sEck0GHTSfG60NGug_0tPQ)
2. [Lido - Everything](https://open.spotify.com/album/78VgrlxNqlGg3ApYVdQHyM?si=DFmoTUNWQbKUVpOIbenrTw)
3. [Camo & Krooked - Mosaik](https://open.spotify.com/album/1miPtr5WVeMoYFvu0RZ6Mc?si=NzHVu0XLQw2Ve0TaSzHJQQ)
4. [Flume - Skin](https://open.spotify.com/album/4NZWRpoMuXaHU7csTjWdB5?si=RbSVDggmTqOstWr7P6dJng)
5. [A$AP Rocky - Testing](https://open.spotify.com/album/3MATDdrpHmQCmuOcozZjDa?si=8YCnrzwuRB2YDpLL-721AA)

I thought that a fun way to execute this idea would be to write a program to do something to visualize the music itself.
I found that the [truchet tiles](https://en.wikipedia.org/wiki/Truchet_tiles) were a promising route to accomplish this, as a
seemingly random arrangement of the tiles can almost always produce an interesting pattern. 


# Programs
The main program, generateImage, takes in an mp3 file, runs it through the SHA512 hash. This produces 
a 128 character hexadecimal string. The string is then converted to binary, yielding 512 bits. 

Then, a 16x16 2D array is initialized. Each array entry gets two of the bits from the hash result.
Knowing that two bits allows us to count to 4 (00, 01, 10, 11), we can design sets of truchet tiles,
with four in a set, and assign each number a truchet tile. 

The sets of tiles I designed are contained in the folder Truchet Tiles. 

The program uses Pillow, the Python imaging library, to place the tiles in images and write them to files. 
The files are all 2000x2000 .pngs, and because I decided to use a 16x16 array, 2000/16 = 125 px for the width
and height of each tile. 

I then ran this program on every song from every album (the music was sourced from the Google Play Music Store, as 320 kbps mp3s).

# Results
The raw images produced by the code are not what I ended up using in the series – I instead opted to composite all the results from
each album into a single piece, one poster and one gif per. The results will be posted in my [portfolio](http://shashcomandur.com/pages/portfolio.html) when they are finished!
 
