def extract_words_from_file(file_path):
    words = []
    with open(file_path, 'r') as file:
        for line in file:
            # Split each line into words using whitespace as the delimiter
            line_words = line.strip().split()
            words.extend(line_words)
    return words

# Provide the path to your text file
file_path = 'path/to/your/file.txt'
word_list = extract_words_from_file(file_path)

# Print all the words
for word in word_list:
    print(word)
