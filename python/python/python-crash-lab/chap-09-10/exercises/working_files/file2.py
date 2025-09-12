file_name = 'chap09&10/working_files/learning_python.txt'

with open(file_name) as file:
    content = file.read()


content = content.replace('python', 'c')
print(content)
