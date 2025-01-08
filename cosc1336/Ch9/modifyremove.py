# The change function changes an existing
# entry in the albums dictionary.
def change(albums):
    # Get an artist to look up.
    artist = input('Enter a artist: ')

    if artist in albums:
        # Get a new album.
        album = input('Enter the new album: ')

        # Update the entry.
        albums[artist] = album
    else:
        print('That artist is not found.')

# The delete function deletes an entry from the
# albums dictionary.
def delete(albums):
    # Get a artist to look up.
    artist = input('Enter an artist: ')

    # If the artist is found, delete the entry.
    if artist in albums:
        del albums[artist]
    else:
        print('That artist is not found.')