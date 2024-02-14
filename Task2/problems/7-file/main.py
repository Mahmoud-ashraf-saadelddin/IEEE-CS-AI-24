import string


def count_words(file_path):
    word_count = {}

    with open(file_path, 'r') as file:
        for line in file:
            # Removing punctuation and converting to lowercase
            cleaned_line = ''.join(char for char in line if char.isalnum() or char.isspace()).lower()

            # Splitting the cleaned line into words
            words = cleaned_line.split()

            # Counting occurrences of each word
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    # Printing the results
    for word, count in word_count.items():
        print(f"{word}: {count}")


file_path = 'Sample.txt'
count_words(file_path)
