def decryption(sentence, n):
    sentence = list(sentence.strip(" "))
    for i in range(len(sentence)):
        alphabet_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        alphabet_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        for j in range(len(alphabet_upper)):
            if sentence[i] == alphabet_upper[j]:
                sentence[i] = alphabet_upper[j - n]
                break
            elif sentence[i] == alphabet_lower[j]:
                sentence[i] = alphabet_lower[j - n]
                break
    sentence = "".join(sentence)
    return sentence
print(decryption("Aopz pz h zljyla", 7))