#Open the word list file (stored in a different folder) and read it line by line
#words_file = open("Needed_Modules/Word_List.txt", "r")
words_file = open("/Users/jzalmano/PycharmProjects/Leetcode/Needed_Modules/Word_List.txt", "r")
english_words = words_file.read().splitlines()

#green = "?????"
#yellow = ""
#yellow2 = {'a':[0,3],'o':[0,1,2],'n':[0,3], 'g':[0,3]}
#gray = ""

green = "s??n?"
yellow1 = ''
yellow2 = {}
gray = "etyiopak"
"""

"""

for i in english_words:
    if len(i) == 5:
        ruled_out = False
        for ind, val in enumerate(green):
            if val != "?":
                if i[ind] != val:
                    ruled_out = True
        for val in yellow1+''.join(yellow2.keys()):
            if val not in i:
                ruled_out = True
        for letter,places in yellow2.items():
            for ind in places:
                if i[ind] == letter:
                    ruled_out = True
        for val in gray:
            if val in i:
                ruled_out = True
        if not ruled_out:
            print(i)

#minty
#tinny
