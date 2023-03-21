def word_replace(): 
    str = "Some commun string to replace"
    word_to_replace = input("Type a word to replace: ")
    word_replacement = input("Type a word to replacement: ")
    return str.replace(word_to_replace, word_replacement)

print(word_replace())