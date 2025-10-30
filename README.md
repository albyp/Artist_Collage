# Artist Collage

Create a simple 2x2 collage with 3 images and a text file.
Useful for cataloging artists, movies etc.

## Features

- Automatically resizes images to 540x540 while maintaining aspect ratio
- Create a plain background image with text from the description file
- Simple inputs and config

## Usage

1. Create a folder for the artist "artist-name"
2. Input 3 images and a text file containing the description of the artist
3. Open `main.py` with a text editor of choice
4. Edit line 4 `ARTIST = "YOUR-ARTIST-HERE"` (should be the same name as the folder from step 1)
5. Run `main.py`

**Note:** Ensure the images and text file are stored with the correct naming convention for the script to work.

- artist-name_pfp.jpg
- artist-name_id1.jpg
- artist-name_id2.jpg
- artist-name.txt

## Dependencies

Ensure Python is installed (version 3.9+).
Install the required dependencies using: `pip install -r requirements.txt`
