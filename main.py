def spin_words(sentence):
    return ' '.join([word if len(word) < 5 else word[::-1] for word in sentence.split()])


print(spin_words('Hey fellow warriors'))
