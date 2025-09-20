from pathlib import Path
file_name = "chap09&10/working_files/files/guest_book.txt"
path = Path(file_name)

while True:
    user = input("Enter your usernam: \n")
    if user.lower() == 'q':
        break

    with path.open('a') as f:
        f.write(f"{user}\n")