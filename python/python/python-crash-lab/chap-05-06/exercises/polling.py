favourie_languages = {

    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

poll_members = ['sarah', 'jenny', 'caleb','edward', 'phil']

for poll_member in poll_members:

    if poll_member in favourie_languages.keys():
        print(f"Hi {poll_member.title()}, thank you for responding")
        
    else:
        print(f"Hi {poll_member.title()}, you are invited to take a poll")

