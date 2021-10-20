def pig_it(text):
    words = text.split()
    new_sentence = ""
    for word in words:
        if word == "!" or word == "?":
            new_sentence += word
        else:
            new_word = word[1:]+word[0] + "ay"
            new_sentence += new_word + " "
    if new_sentence[-1] == " ":
        new_sentence = new_sentence.rstrip(new_sentence[-1])
        
    return new_sentence