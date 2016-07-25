    #function and dictionaries, with and optional argument

def make_album(artist,album,tracks=''):
    """we are creating the album dictionary"""
    album_dic = {'artist_name':artist, 'album_name':album}
    #if statement for the optional argument
    if tracks:
        album_dic['num_tracks'] = tracks
    return album_dic


album_info = make_album('Frank','red album')
print(album_info)
album_info = make_album('Claudia','blue album','32')
print(album_info)