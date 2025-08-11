player1 = {

    'name':'messi',
    'position':'forward',
    'goals':810
    
}

player2 = {

    'name':'maldini',
    'position':'cb',
    'goals': 10
}


player3 = {

    'name':'neymar',
    'position':'forward',
    'goals': 520,
}


player4 = {

    'name':'ramos',
    'position':'cb',
    'goals':150
}


player5 = {

    'name':'cr7',
    'position':'forward',
    'goals':1017

}



players = [player1, player2, player3, player4, player5]


for player in players:
    if player['goals'] > 600:
        print(f"\n{player['name'].title()} has more than 600 goals")

    if player['position'] == 'cb' and player['goals'] > 10:
        print(f"\n{player['name'].title()} is a CB with more than 10 goals.")
        

star_player = max(players, key=lambda p: p['goals'])
print(f"\nStar player: {star_player['name'].title()} with {star_player['goals']} goals.")