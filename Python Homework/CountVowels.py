print("This program will count the amount of vowels in a single word and list them out.")
def vowels():
    user_word = input("What is the word of choice?: ")

    a_vowel = user_word.count("a")
    e_vowel = user_word.count("e")
    i_vowel = user_word.count("i")
    o_vowel = user_word.count("o")
    u_vowel = user_word.count("u")

print(vowels)

