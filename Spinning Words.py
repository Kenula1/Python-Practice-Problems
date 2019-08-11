def spin_words(sentence):
    word_list = sentence.split()
    for word in range(len(word_list)):
        if len(word_list[word]) >= 5:
            word_list[word] = word_list[word][::-1]
    return ' '.join(word_list)

print(spin_words("Welcome"))