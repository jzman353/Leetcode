class Solution:
    def floodFill(image, sr, sc, newColor):
        changed = 1
        stack = []
        checked = []
        init_color = image[sr][sc]
        tempr = sr
        tempc = sc
        image[tempr][tempc] = newColor

        while changed == 1:
            changed = 0
            try:  # Check Up
                while True:
                    if (tempr-1)>=0 and image[tempr - 1][tempc] == init_color and [tempr - 1, tempc] not in checked:
                        checked.append([tempr - 1, tempc])
                        stack.append([tempr - 1, tempc])
                        changed = 1
                    elif image[tempr - 1][tempc] != init_color and [tempr - 1, tempc] not in checked:
                        checked.append([tempr - 1, tempc])
                        break
                    else:
                        break
            except:
                pass
            try:  # Check Down
                while True:
                    if image[tempr + 1][tempc] == init_color and [tempr + 1, tempc] not in checked:
                        checked.append([tempr + 1, tempc])
                        stack.append([tempr + 1, tempc])
                        changed = 1
                    elif image[tempr + 1][tempc] != init_color and [tempr + 1, tempc] not in checked:
                        checked.append([tempr + 1, tempc])
                        break
                    else:
                        break
            except:
                pass
            try:  # Check Left
                while True:
                    if (tempc-1)>=0 and image[tempr][tempc - 1] == init_color and [tempr, tempc - 1] not in checked:
                        checked.append([tempr, tempc - 1])
                        stack.append([tempr, tempc - 1])
                        changed = 1
                    elif image[tempr][tempc - 1] != init_color and [tempr, tempc - 1] not in checked:
                        checked.append([tempr, tempc - 1])
                        break
                    else:
                        break
            except:
                pass
            try:  # Check Right
                while True:
                    if image[tempr][tempc + 1] == init_color and [tempr, tempc + 1] not in checked:
                        checked.append([tempr, tempc + 1])
                        stack.append([tempr, tempc + 1])
                        changed = 1
                    elif image[tempr][tempc + 1] != init_color and [tempr, tempc + 1] not in checked:
                        checked.append([tempr, tempc + 1])
                        break
                    else:
                        break
            except:
                pass

            if stack and changed == 0:  # Check if stack isn't empty
                temp = stack.pop()
                tempr = temp[0]
                tempc = temp[1]
                image[tempr][tempc] = newColor
                changed = 1

            if not stack and changed == 0:  # Check if stack is empty
                break

        return image

    #print(floodFill([[1,1,1],[1,1,0],[1,0,1]], sr=1, sc = 1, newColor = 2))
    print(floodFill([[0,0,0],[0,1,0]], sr=1, sc=1, newColor=2))