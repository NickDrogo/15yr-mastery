def make_album(artist_name, album, no_songs=None):
    result = {'artist_name':artist_name, 'album':album, 'no_songs':no_songs}
    return result



result = make_album('kenny', 'atilogwu')
result1 = make_album('psquare', 'game over')
result2 = make_album('flavor', 'reloaded')
result3 = make_album('Nick', 'consistency', 200)

print(result)
print(result1)
print(result2)
print(result3)