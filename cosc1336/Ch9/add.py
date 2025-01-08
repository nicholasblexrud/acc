# The add function adds a new entry into the
# albums dictionary.
def add(albums):
    # Get a artist and album.
    artist = input('Enter a artist: ')
    album = input('Enter a album: ')

    # If the artist does not exist, add it.
    if artist not in albums:
        albums[artist] = album
    else:
        print('That entry already exists.')