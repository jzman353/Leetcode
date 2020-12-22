#Open the word list file (stored in a different folder) and read it line by line
words_file = open("../../Needed_Modules/Word_List.txt", "r")
english_words = words_file.read().splitlines()

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'}

#This function will translate every word into morse code and store it in a new text document named Word_List_In_Morse_Code.txt
def translate(word_list):
    Word_List_In_Morse_Code = open("Word_List_In_Morse_Code.txt", "w+")
    for word in word_list:
        morse_word = ""
        for letter in word.upper():
            morse_word = morse_word + MORSE_CODE_DICT[letter]
        Word_List_In_Morse_Code.write(str(morse_word)+"\n")
#translate(english_words)

#After translating all the words once, you can just get all the morse code words from the document
#Open the morse code list file and read it line by line
morse_file = open("Word_List_In_Morse_Code.txt", "r")
morse_words = morse_file.read().splitlines()

#Exersize 1
#The sequence -...-....-.--. is the code for four different words (needing, nervate, niding, tiling). Task 1: Find the only sequence that's the code for 13 different words.
#This function uses a Counter from the collections package (included with python3)
def same_morse_13_words(morse_words):
    import collections
    cnt = collections.Counter()
    for word in morse_words:
        cnt[word] += 1
    print(cnt.most_common(10))
#print(same_morse_13_words(morse_words))
#Exersize 1 answer: '-....--....'

#Exersize 2
#autotomous encodes to .-..--------------..-..., which has 14 dashes in a row. Task 2: Find the only word that has 15 dashes in a row.
def fifteen_dashes(english_words, morse_words):
    for i, word in enumerate(morse_words):
        counter = 0
        maxx = 0
        for letter in word:
            if letter == '-':
                counter += 1
                maxx = max(maxx, counter)
            else:
                counter = 0
        if maxx == 15:
            return english_words[i]
#print(fifteen_dashes(english_words, morse_words))
#Exersize 2 answer: bottommost

#Exersize 3
#Call a word perfectly balanced if its code has the same number of dots as dashes. counterdemonstrations is one of two 21-letter words that's perfectly balanced. Task 3: Find the other one.
def perfectly_balanced(english_words, morse_words):
    for i, word in enumerate(morse_words):
        if len(english_words[i])==21 and word.count('-') == word.count('.') and english_words[i] != 'counterdemonstrations':
            return english_words[i]
#print(perfectly_balanced(english_words, morse_words))
#Exersize 3 answer: overcommercialization

#Exersize 4
#protectorate is 12 letters long and encodes to .--..-.----.-.-.----.-..--., which is a palindrome (i.e. the string is the same when reversed). Task 4: Find the only 13-letter word that encodes to a palindrome.
def palindrome(english_words, morse_words):
    for i, word in enumerate(morse_words):
        if len(english_words[i]) == 13:
            reverse_word = list(reversed(word))
            if list(word) == reverse_word:
                return english_words[i]
#print(palindrome(english_words, morse_words))
#Exersize 4 answer: intransigence

#Exersize 5
#--.---.---.-- is one of five 13-character sequences that does not appear in the encoding of any word. Task 5: Find the other four.
#This function gives every possible 13 char combination # Thirteen_Char_Morse_Permutations.txt
def generate_permutations_symbols():
    import itertools
    x = ['.','-']
    permutations_list = [p for p in itertools.product(x, repeat=13)]
    for i in range(len(permutations_list)):
        permutations_list[i] = "".join(list(permutations_list[i]))
    Permutations_file = open("Thirteen_Char_Morse_Permutations2.txt", "w+")
    for permutation in permutations_list:
        Permutations_file.write(str(permutation) + "\n")
#generate_permutations_symbols()

def morse_does_not_appear(morse_words):
    Permutations_file = open("Thirteen_Char_Morse_Permutations2.txt", "r")
    permutations = Permutations_file.read().splitlines()
    permutations.remove('--.---.---.--')
    for i in morse_words:
        if len(i) == 13:
            if i in permutations:
                permutations.remove(i)
        elif len(i) > 13:
            for j in range(len(i)-13):
                if i[j:j+13] in permutations:
                    permutations.remove(i[j:j+13])
        print(len(permutations))
    return permutations
#print(morse_does_not_appear(morse_words))
#Exersize 5 answer: ['---.----.----', '---.---.-----', '---.---.---.-', '--.---.------']

