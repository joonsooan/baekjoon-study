num_test_case = int(input())

for i in range(num_test_case):
    sentence = input()
    words = sentence.split()
    reversed_words = []

    for word in words:
        reversed_word = ""
        for char in word:
            reversed_word = char + reversed_word
        reversed_words.append(reversed_word)

    for word in reversed_words:
        print(word, end=" ")