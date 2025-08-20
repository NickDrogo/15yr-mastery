def make_album(artist_name, album):
    result = {'artist_name':artist_name, 'album':album}
    return result


while True:
    print("\nEnter an album's artist and title or 'q' to quit")
    user = input("Enter artist's name: ")
    

    if user == 'q':
        break

    user2 = input("Enter the album's title: ")
    if user2 == 'q':
        break

    result1 = make_album(user, user2)
    print(result1)

    
    
    