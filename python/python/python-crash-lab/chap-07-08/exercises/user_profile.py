def user_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_id = user_profile('Nick', 'Elebeke', location='Nigeria', field='problem solving', fav_colour='black')
print(user_id)