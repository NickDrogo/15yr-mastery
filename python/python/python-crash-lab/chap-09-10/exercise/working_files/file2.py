from pathlib import Path

file_name = 'chap09&10/working_files/learning_python.txt'

path = Path(file_name)
contents = path.read_text()

content = contents.replace('python', 'c')
print(content)
