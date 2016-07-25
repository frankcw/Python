    #function and dictionaries, with and optional argument

def make_album(artist,album,tracks=''):
    """we are creating the album dictionary"""
    album_dic = {'artist_name':artist, 'album_name':album}
    #if statement for the optional argument
    if tracks:
        album_dic['num_tracks'] = tracks
    return album_dic


while True:
	print('Please enter "q" at any moment to quit\n')
	artist = input('Artist:')
	if artist == 'q':
		break
	album = input('Album:')
	if artist == 'q':
		break
	tracks = input('Tracks:')
	if artist == 'q':
		break

	artist_information = make_album(artist,album,tracks)
	print(artist_information)
