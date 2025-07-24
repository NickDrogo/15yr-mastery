guess_list = ['Zammy', 'Mum', 'Dad']

zammy = f"Hello {guess_list[0]}👋, here is an invitation to my birthday party,pls be there!\n"
mum = f"\tHello {guess_list[1]}👋,here is an invitation to my birthday party,pls be there!\n"
dad = f"Hello {guess_list[2]}👋, here is an invitation to my birthday party,wish you will be there!"

print(zammy)
print(mum)
print(dad)
print()

print(f"Ouch!😞 {guess_list[2]} ain't gonna make it to the party sadly") 
print()

guess_list[2] = "gifty"

gifty= f"Hello {guess_list[2]}👋, here is an invitation to my birthday party,pls be there!"
print("=====================================================================================")

print(zammy)
print(mum)
print(gifty)
print()
print("======================================================================================")

print(f"Hello {guess_list[0]}👋, i found a bigger dinner table,which means there is a detour of plans")
print(f"Hello {guess_list[1]}👋, i found a bigger dinner table,which means there is a detour of plans")
print(f"Hello {guess_list[2]}👋, i found a bigger dinner table,which means there is a detour of plans")
print()

guess_list.insert(0, "kelvin")
guess_list.insert(1, "Apostle")
guess_list.append("Favour")

print("===================================================================================")
""
print(f"Hello {guess_list[0]}👋, here is an invitation to my birthday party,pls be there!\n")
print(f"Hello {guess_list[1]}👋, here is an invitation to my birthday party,pls be there!\n")
print(f"Hello {guess_list[2]}👋, here is an invitation to my birthday party,pls be there!\n")
print(f"Hello {guess_list[3]}👋, here is an invitation to my birthday party,pls be there!\n")
print(f"Hello {guess_list[4]}👋, here is an invitation to my birthday party,pls be there!\n")
print(f"Hello {guess_list[5]}👋, here is an invitation to my birthday party,pls be there!")
print()

print("=========================================================================")
print("Sadly! there is a change of plans, i can only invite two people to my dinner party\n")
print(f"I'm sorry {guess_list.pop(0)}🙏, i can't invite you anymore")
print(f"I'm sorry {guess_list.pop(0)}🙏, i can't invite you anymore")
print(f"I'm sorry {guess_list.pop(0)}🙏, i can't invite you anymore")
print(f"I'm sorry {guess_list.pop(0)}🙏, i can't invite you anymore")

print("=========================================================================")
print(f"Hello {guess_list[0]}, you are still invited to my party😇")
print(f"Hello {guess_list[1]}, you are still invited to my party😇\n")
print(f"The number of people i am inviting to the dinner is {len(guess_list)}\n")

del guess_list[0]
del guess_list[0]

print(guess_list)

