import os
from mutagen.easyid3 import EasyID3

# || DESCRIPTION || 
# In some cases (such as with the music albums for The Long Dark), the audio file is named, but the 'title' metadata tag has no value.
# Place the script in the album's folder/directory. The script will scan the directory and update the 'title' tag for each audio file accordingly.

print(f"Script started")

folderpath = os.getcwd() # Get the script's working directory
mp3FileExtensionString = ".mp3"

def set_title_to_filename(folderpath):
    print(f"For loop started")
    # Loop through all files in the folder
    for filename in os.listdir(folderpath):
        # Check if the file is an mp3
        if check_file_is_mp3(filename):
            # Get the audio file's full path
            filepath = os.path.join(folderpath, filename)

            edit_mp3_metadata(filename, filepath)


def check_file_is_mp3(filename):
        print(f"Checking file is an mp3")
        if filename.endswith(mp3FileExtensionString):
            return True
        
def check_title_tag_is_not_set(audioFile, songTitleString):
    print(f"Checking audio file Title attribute is NOT set")
    if 'title' not in audioFile or audioFile['title'] != [songTitleString]:
          return True
     # the variable `songTitleString` is enclosed in square brackets because audio['title'] is a list. Mutagen library classifies each tag (eg. 'title') as a list of strings. Metadata tags like 'title' can potentially hold multiple values.
     # eg. audio['title'] = ['Song Title 1', 'Song Title 2']

def edit_mp3_metadata(filename, filepath):
    try:
        # Load the MP3 file's metadata
        audioFile = EasyID3(filepath)
    except Exception:
        # If the file doesn't have ID3 tags, create new ones
        audioFile = EasyID3()

    # Extract the file name without the ".mp3" extension
    # os.path.splitext() method splits a file name into two parts: the "root" ('songname') and the "extension" ('.mp3'), returns a tuple with two elements with index [0] and index [1]
    songTitleString = os.path.splitext(filename)[0]

    # Check if the Title tag is not already set
    if check_title_tag_is_not_set(audioFile, songTitleString):
        # Set the Title to the file name (without the extension)
        audioFile['title'] = songTitleString
        
        # Save the updated metadata
        audioFile.save(filepath)
        print(f"Updated title for: {filename}")

    else:
        print(f"Title already set for: {filename}")


set_title_to_filename(folderpath)
print(f"Audio file tag editing script completed")
