from pathlib import Path
path = Path('chap09&10/working_files/files/common_words.txt')



contents = path.read_text(encoding='utf-8')

lower = contents.lower()

counts = lower.split()
num_rep = lower.count('the')

print(contents.lower().split().count('the '))

print(contents.lower().count('the '))

print(contents.lower().split().count('the'))

print(contents.lower().count('the'))
