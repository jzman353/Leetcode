#Open the word list file (stored in a different folder) and read it line by line
words_file = open("../Needed_Modules/Word_List.txt", "r")
english_words = words_file.read().splitlines()

for i in english_words:

    #if len(i)==5 and i[0] == 'e' and i[1] == 'e' and i[2] == 't' and i[3] == 'i' and i[4] == 't':
    if len(i) == 5 and i[1] == 'm' and i[4] == 'e':
        print(i)

