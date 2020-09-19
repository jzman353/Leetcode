'''
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
Write a recursive function that paints the pixel if it's the correct color, then recurses on neighboring pixels.

Runtime: 100 ms Beats 18%
Memory Usage: 14 MB
'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        changed = 1
        stack = []
        checked = []
        init_color = image[sr][sc]
        tempr = sr
        tempc = sc
        image[tempr][tempc] = newColor
        
        while changed == 1:
            changed = 0
            try: # Check left
                while True:
                    if tempr-1>=0 and image[tempr-1][tempc] == init_color and [tempr-1,tempc] not in checked:
                        checked.append([tempr-1,tempc])
                        stack.append([tempr-1,tempc])
                        changed = 1  
                    elif image[tempr-1][tempc] != init_color and [tempr-1,tempc] not in checked:
                        checked.append([tempr-1,tempc])
                        break
                    else:
                        break
            except:
                pass
            try: # Check Right
                while True:
                    if image[tempr+1][tempc] == init_color and [tempr+1,tempc] not in checked:
                        checked.append([tempr+1,tempc])
                        stack.append([tempr+1,tempc])
                        changed = 1
                    elif image[tempr+1][tempc] != init_color and [tempr+1,tempc] not in checked:
                        checked.append([tempr+1,tempc])
                        break  
                    else:
                        break
            except:
                pass
            try: # Check Down
                while True:
                    if tempc-1>=0 and image[tempr][tempc-1] == init_color and [tempr,tempc-1] not in checked:
                        checked.append([tempr,tempc-1])
                        stack.append([tempr,tempc-1])
                        changed = 1
                    elif image[tempr][tempc-1] != init_color and [tempr,tempc-1] not in checked:
                        checked.append([tempr,tempc-1])
                        break  
                    else:
                        break
            except:
                pass
            try: # Check Up
                while True:
                    if image[tempr][tempc+1] == init_color and [tempr,tempc+1] not in checked:
                        checked.append([tempr,tempc+1])
                        stack.append([tempr,tempc+1])
                        changed = 1
                    elif image[tempr][tempc+1] != init_color and [tempr,tempc+1] not in checked:
                        checked.append([tempr,tempc+1])
                        break 
                    else:
                        break
            except:
                pass
            
            if stack and changed == 0: #Check if stack isn't empty
                temp = stack.pop()
                tempr = temp[0]
                tempc = temp[1]
                image[tempr][tempc] = newColor
                changed = 1
                
            
            if not stack and changed == 0: #Check if stack is empty
                break
                
        return image
                
                
'''
Runtime: 64 ms

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        r, c = len(image), len(image[0])
        color = image[sr][sc]
        def dfs(i, j):
            if i < 0 or i>=r or j < 0 or j >= c: #out of bounds
                return
            if image[i][j] == newColor or image[i][j] != color: #if coloured or does not have simialr colour as source do nothing
                return
            image[i][j] = newColor
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i,j+1)
            dfs(i, j-1)
        dfs(sr, sc)
        return image
'''
