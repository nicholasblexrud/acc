# The look_up function looks up a artist in the
# albums dictionary.
def look_up(albums):
    # Get a artist to look up.
    artist = input('Enter an artist: ')

    # Look it up in the dictionary.
    print(albums.get(artist, 'Not found.'))