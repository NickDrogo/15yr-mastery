from pathlib import Path
file_name = 'chap09&10/working_files/files/guest.txt'

first_name = input("Enter your first name:\n")
last_name = input("Enter your last name:\n")
    

path = Path(file_name)
contents = path.write_text(f"{first_name} {last_name}")
