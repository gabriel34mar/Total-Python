def alphabet(word):
    reduction_word=set(word.lower())
    ordered= sorted(reduction_word)
    return ordered

print(alphabet("entertaining"))
