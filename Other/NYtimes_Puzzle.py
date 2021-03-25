#Open the word list file (stored in a different folder) and read it line by line
words_file = open("../Needed_Modules/Word_List.txt", "r")
english_words = words_file.read().splitlines()

for i in english_words:
    if len(i)==4 and i[-1] == 'b':
        test = True
        for j in ['o','u','r','s','g','f','m','j','p']:
            if j in i:
                test = False
                break
        if test:
            print(i)

"""
bibb
blab
bleb
"""