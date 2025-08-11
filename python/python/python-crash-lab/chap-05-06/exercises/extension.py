favourite_languages = {
    'jen':['python', 'ruby',],
    'sarah':['c'],
    'edward':['ruby', 'go'],
    'phil':['python', 'haskell']

}

for name, languages in favourite_languages.items():
    if  len(languages) > 1:
        print(f"\n{name}'s favourite language are: ")
        for language in languages:
            print(f"\t{language}")
    else:
        for language in languages:
            print(f"\n{name}'s favourite language is {language} ")