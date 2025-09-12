file_name = 'chap09&10/working_files/common_words.txt'

with open(file_name) as file_object:
    contents = file_object.read()
    lower = contents.lower()
    counts = lower.split()
    num_rep = counts.count('the')
    print(num_rep)
