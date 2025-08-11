current_users = ['zammy', 'prince', 'kelvin', 'mathew', 'apostle', 'sparkle']

new_users = ['zammy', 'phill foden', 'simon', 'guardiola', 'APOSTLE', 'SPARKLE']

for user_name in new_users:
    if user_name.lower() in current_users:
        print(f"the name '{user_name}' is not available")
    else:
        print(f"the name '{user_name}' is available")

