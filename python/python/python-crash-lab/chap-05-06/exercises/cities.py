cities = {
    'Tokyo' : {'country':'japan',
               'population':37_400_000,
               'fact':'Tokyo is the most populous metropolitan area in the world'

    },

    'cairo':{'country':'egypt',
             'population':10_100_000,
             'fact':'Cairo is home to the only surviving ancient wonder, the pyramid if Giza.'

    },

    'sydney':{'country':'australia',
              'population':5_300_000,
              'fact':'Sydney Opera House is one of the most famous architectural landmarks in the world.'
        
    }
}

for name, infos in cities.items():
    print(f"\nCity's Name: {name}")
    for key, info in infos.items():
        print(f"\t{key}:{info}")