import os
from mutagen.easyid3 import EasyID3

# || DESCRIPTION || 
# This script is meant to update the albums corresponding metadata to highlight the different "discs" and each song's corresponding artists as well as giving each album the corrected album name/title

# BEFORE RUNNING THE SCRIPT
# Update the list at the bottom of the script labeled 'metadata'.


def set_itunes_metadata(metadata):
    # Access values from the dictionary
    album_folder_path = metadata['album_folder_path']

    # Iterate through all tracks in the folder
    for filename in os.listdir(album_folder_path):
        # Check if the filename ends with a '.mp3' extension
        if check_file_is_mp3(filename):
            # Get the audio file's full path
            filepath = compose_filepath(album_folder_path, filename)
            edit_mp3_metadata(filename, filepath, metadata)

def compose_filepath(album_folder_path, filename):
    return os.path.join(album_folder_path, filename)

def check_file_is_mp3(filename):
    print(f"Checking file is an mp3")
    mp3_file_ext_string = ".mp3"
    if filename.endswith(mp3_file_ext_string):
        return True

def edit_mp3_metadata(filename, filepath, metadata):
    try:
        audioFile = EasyID3(filepath)
    except Exception:
        # If the file doesn't have ID3 tags, create new ones
        audioFile = EasyID3()

    # Values from the metadata dictionary
    album_name = metadata['album_name']
    grouping_subtitle = metadata['grouping_subtitle']
    main_artist_name = metadata['main_artist_name']
    contri_artist_name = metadata['contri_artist_name']
    disc_number = metadata['disc_number']
    total_discs = metadata['total_discs']

    # Set metadata
    audioFile['album'] = album_name
    audioFile['grouping'] = grouping_subtitle
    audioFile['albumartist'] = main_artist_name
    audioFile['artist'] = contri_artist_name
    audioFile['discnumber'] = f"{disc_number}/{total_discs}"
    audioFile.save(filepath)
    print(f"Updated metadata for {filename}")

# Metadata to update the audio files with. Edit these according to your preferences.
album_metadata = {
    "album_folder_path" : r"{Copy-paste the path to the folder}",
    "album_name" : "{Album name}",
    "grouping_subtitle" : "{Give each 'disc' a label/title}",
    "main_artist_name" : "{Main artist's name}",
    "contri_artist_name" : "{Contributing artist's name. Eg. a second composer, guest singer, etc.}",
    "disc_number" : {eg. 1},
    "total_discs" : {eg. 4}
}

set_itunes_metadata(album_metadata)