#Open the word list file (stored in a different folder) and read it line by line
words_file = open("../Needed_Modules/Word_List.txt", "r")
english_words = words_file.read().splitlines()

for i in english_words:

    #if len(i)==5 and i[0] == 'e' and i[1] == 'e' and i[2] == 't' and i[3] == 'i' and i[4] == 't':
    #if len(i) == 5 and i[3] == 'e' and (i[0] == 'a' or i[4] == 'a') and 'c' not in i and 'p' not in i and 'x' not in i and 'h' not in i and 't' not in i and 's' not in i and 'l' not in i and 'r' not in i and 'd' not in i:
    if len(i) == 5 and i[3] == 'i' and i[4] == 'e' and 't' not in i and "u" not in i and "n" not in i:
        print(i)