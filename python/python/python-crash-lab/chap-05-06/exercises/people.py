id_1 = {

    'first_name':'zamy',
    'last_name':'okonkwo',
    'state':'anambra',
    'town':'ekwulimili',
    'lga':'nnewi north',
    
}
print('==================')
id_2 = {

    'first_name':'ngozi',
    'last_name':'mbamara',
    'state':'anambra',
    'town':'ogidi',
    'lga':'idemilii south',


}




id_3  = {

        'first_name':'tochukwu',
        'last_name' : 'elebeke',
        'state':'anambra',
        'town' : 'nnewi',
        'lga' : 'orumba south',
        

}




peoples = [id_1, id_2, id_3]

for profile in peoples:
    print(f"first_name: {profile['first_name']}")
    print(f"last_name: {profile['last_name']}")
    print(f"state: {profile['state']}")
    print(f"town: {profile['town']}")
    print(f"lga: {profile['lga']}")
    print('-' * 20)
                
        
