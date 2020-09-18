#Solved brute force method but not enough

'''
Image Overlap

Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.

Notes:

    1 <= A.length = A[0].length = B.length = B[0].length <= 30
    0 <= A[i][j], B[i][j] <= 1
'''
import copy
def largestOverlap(A, B) -> int:
    def count_sum(A,B,size):
        sum = 0
        for i in range(size):
            for j in range(size):
                sum += A[i][j]*B[i][j]
        return sum

    origional = copy.deepcopy(A)
    reset = copy.deepcopy(origional)
    size = len(A)
    sum1 = max(0,count_sum(A, B, size))
    #Right Shift
    for i in range(size):
        # Down Shift
        for j in range(size-1):
            A.insert(0, [0] * size)
            A.pop()
            sum1 = max(sum1, count_sum(A, B, size))
        A = copy.deepcopy(reset)
        # Up Shift
        for j in range(size-1):
            A.append([0] * size)
            A.pop(0)
            sum1 = max(sum1, count_sum(A, B, size))
        A = copy.deepcopy(reset)
        for j in range(size):
            A[j].insert(0,0)
            reset = copy.deepcopy(A)
        sum1 = max(sum1, count_sum(A, B, size))

    A = copy.deepcopy(origional)
    # Left Shift
    for i in range(size-1):
        for j in range(size):
            A[j].pop(0)
            A[j].append(0)
        sum1 = max(sum1, count_sum(A, B, size))
        reset = copy.deepcopy(A)
        # Down Shift
        for j in range(size-1):
            A.insert(0, [0] * size)
            sum1 = max(sum1, count_sum(A, B, size))
        A = copy.deepcopy(reset)
        # Up Shift
        for j in range(size-1):
            A.append([0] * size)
            A.pop(0)
            sum1 = max(sum1, count_sum(A, B, size))
    return sum1

"""
#1/49
A = [[1, 1, 0],
     [0, 1, 0],
     [0, 1, 0]]
B = [[0, 0, 0],
     [0, 1, 1],
     [0, 0, 1]]
#Answer: 3
#15/49
A = [[1]]
B = [[1]]
#Answer: 1

"""
#40/49
A = [[0,0,0],[1,0,0],[1,0,0]]
B = [[1,0,0],[1,1,1],[0,0,1]]
#Answer: 2


print(largestOverlap(A, B))

"""
Overview

First of all, this is a really fun problem to solve, as one would discover later. In addition, it could be a practical problem in real world. For instance, if one can find the maximal overlapping zone between two images, one could clip the images to make them smaller and more focused.

In this article, we will cover three approaches as follows:

    We could solve the problem intuitively by enumerating all the possible overlapping zones.

    Or more efficiently, we can apply some knowledge of linear algebra (or geometry), as we will present another solution in the second approach.

    Finally, we could even solve it with the conception of convolution, as in Convolution Neural Network (a.k.a. CNN), which is the backbone operation for the image recognition models nowadays.

Approach 1: Shift and Count

Intuition

As stated in the problem description, in order to calculate the number of ones in the overlapping zone, we should first shift one of the images. Once the image is shifted, it is intuitive to count the numbers.

    Therefore, a simple idea is that one could come up all possible overlapping zones, by shifting the image matrix, and then simply count within each overlapping zone.

The image matrix could be shifted in four directions, i.e. left, right, up and down.

We could represent the shifting with a 2-axis coordinate as follows, where the X-axis indicates the shifting on the directions of left and right and the Y-axis indicates the shifting of up and down.

Image Shift

For instance, the coordinate of (1, 1) represents that we shift the matrix to the right by one and to the up side by one as well.

    One important insight is that shifting one matrix to a direction is equivalent to shifting the other matrix to the opposite direction, in the sense that we would have the same overlapping zone at the end.

Image Shift

For example, by shifting the matrix A to one step on the right, is same as shifting the matrix B to the left by one step.

Algorithm

Based on the above intuition, we could implement the solution step by step. First we define the function shift_and_count(x_shift, y_shift, M, R) where we shift the matrix M with reference to the matrix R with the shifting coordinate (x_shift, y_shift) and then we count the overlapping ones in the overlapping zone.

    The algorithm is organized as a loop over all possible combinations of shifting coordinates (x_shift, y_shift).

    More specifically, the ranges of x_shift and y_shift are both [0, N-1] where NNN is the width of the matrix.

    At each iteration, we invoke the function shift_and_count() twice to shift and count the overlapping zone, first with the matrix B as the reference and vice versa.

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        dim = len(A)

        def shift_and_count(x_shift, y_shift, M, R):
            '''
            Shift the matrix M, and count the ones in the overlapping zone.
            M: matrix to be moved
            R: matrix for reference

            moving one matrix up and left is equivalent to
            moving the other matrix down and right
            '''
            count = 0
            for r_row, m_row in enumerate(range(y_shift, dim)):
                for r_col, m_col in enumerate(range(x_shift, dim)):
                    if M[m_row][m_col] == 1 and M[m_row][m_col] == R[r_row][r_col]:
                        count += 1
            return count

        max_overlaps = 0
        # move one of the matrice up and left and vice versa.
        # (equivalent to move the other matrix down and right)
        for y_shift in range(0, dim):
            for x_shift in range(0, dim):
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, A, B))
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, B, A))

        return max_overlaps
        
Complexity Analysis

Let NNN be the width of the matrix.

First of all, let us calculate the number of all possible shiftings, (i.e. the number of overlapping zones).

For a matrix of length NNN, we have 2(N−1)2(N-1)2(N−1) possible offsets along each axis to shift the matrix. Therefore, there are in total 2(N−1)⋅2(N−1)=4(N−1)22(N-1) \cdot 2(N-1) = 4(N-1)^22(N−1)⋅2(N−1)=4(N−1)2 possible overlapping zones to calculate.

    Time Complexity: O(N4)\mathcal{O}(N^4)O(N4)

        As discussed before, we have in total 4(N−1)24(N-1)^24(N−1)2 possible overlapping zones.

        The size of the overlapping zone is bounded by O(N2)\mathcal{O}(N^2)O(N2).

        Since we iterate through each overlapping zone to find out the overlapping ones, the overall time complexity of the algorithm would be 4(N−1)2⋅O(N2)=O(N4)4(N-1)^2 \cdot \mathcal{O}(N^2) = \mathcal{O}(N^4)4(N−1)2⋅O(N2)=O(N4).

    Space Complexity: O(1)\mathcal{O}(1)O(1)
        As one can see, a constant space is used in the above algorithm.

Approach 2: Linear Transformation

Intuition

One drawback of the above algorithm is that we would scan through those zones that are filled with zeros over and over, even though these zones are not of our interests.

Because for those cells filled with zero, no matter how we shift, they would not add up to the final solutions. As a follow-up question, we could ask ourselves that, can we focus on those cells with ones?

    The answer is yes. The idea is that we filter out those cells with ones in both matrices, and then we apply the linear transformation to align the cells.

First of all, we define a 2-dimension coordinate, via which we could assign a unique coordinate to each cell in the matrix, e.g. a cell can be indexed as I=(Xi,Yi)I = (X_i, Y_i)I=(Xi​,Yi​).

Then to shift a cell, we can obtain the new position of the cell by applying a linear transformation. For example, to shift the cell to the right by one and to the up side by one is to apply the linear transformation vector of V=(1,1)V = (1, 1)V=(1,1). The new index of the cell can be obtained by I+V=(Xi+1,Yi+1)I + V = (X_i + 1, Y_i + 1)I+V=(Xi​+1,Yi​+1).

linear transformation

Furthermore, given two matrices, we have two non-zero cells respectively in the matrices as Pa=(Xa,Ya)P_a =(X_a, Y_a)Pa​=(Xa​,Ya​) and Pb=(Xb,Yb)P_b = (X_b, Y_b)Pb​=(Xb​,Yb​). To align these cells together, we would need a transformation vector as Vab=(Xb−Xa,Yb−Ya)V_{ab} = (X_b - X_a, Y_b - Y_a)Vab​=(Xb​−Xa​,Yb​−Ya​), so that Pa+Vab=PbP_a + V_{ab} = P_bPa​+Vab​=Pb​.

    Now, the key insight is that all the cells in the same overlapping zone would share the same linear transformation vector.

Based on the above insight, we can then use the transformation vector VabV_{ab}Vab​ as a key to group all the non-zero cells alignments between two matrices. Each group represents an overlapping zone. Naturally, the size of the overlapping zone would be the size of the group as well.

Algorithm

The algorithm can be implemented in two overall steps.

    First, we filter out those non-zero cells in each matrix respectively.

    Second, we do a cartesian product on the non-zero cells. For each pair of the products, we calculate the corresponding linear transformation vector as Vab=(Xb−Xa,Yb−Ya)V_{ab} = (X_b - X_a, Y_b - Y_a)Vab​=(Xb​−Xa​,Yb​−Ya​). Then, we count the number of the pairs that have the same transformation vector, which is also the number of ones in the overlapping zone.


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        dim = len(A)

        def non_zero_cells(M):
            ret = []
            for x in range(dim):
                for y in range(dim):
                    if M[x][y] == 1:
                        ret.append((x, y))
            return ret

        transformation_count = defaultdict(int)
        max_overlaps = 0

        A_ones = non_zero_cells(A)
        B_ones = non_zero_cells(B)

        for (x_a, y_a) in A_ones:
            for (x_b, y_b) in B_ones:
                vec = (x_b - x_a, y_b - y_a)
                transformation_count[vec] += 1
                max_overlaps = max(max_overlaps, transformation_count[vec])

        return max_overlaps
        
Complexity Analysis

Let Ma,MbM_a, M_bMa​,Mb​ be the number of non-zero cells in the matrix A and B respectively. Let NNN be the width of the matrix.

    Time Complexity: O(N4)\mathcal{O}(N^4)O(N4).

        In the first step, we filter out the non-zero cells in each matrix, which would take O(N2)\mathcal{O}(N^2)O(N2) time.

        In the second step, we enumerate the cartesian product of non-zero cells between the two matrices, which would take O(Ma⋅Mb)\mathcal{O}(M_a \cdot M_b)O(Ma​⋅Mb​) time. In the worst case, both MaM_aMa​ and MbM_bMb​ would be up to N2N^2N2, i.e. matrix filled with ones.

        To sum up, the overall time complexity of the algorithm would be O(N2)+O(N2⋅N2)=O(N4)\mathcal{O}(N^2) + \mathcal{O}(N^2 \cdot N^2) = \mathcal{O}(N^4)O(N2)+O(N2⋅N2)=O(N4).

        Although this approach has the same time complexity as the previous approach, it should run faster in practice, since we ignore those zero cells.

    Space Complexity: O(N2)\mathcal{O}(N^2)O(N2)
        We kept the indices of non-zero cells in both matrices. In the worst case, we would need the O(N2)\mathcal{O}(N^2)O(N2) space for the matrices filled with ones.

Approach 3: Imagine Convolution

Intuition

As it turns out, the number of overlapped ones in an overlapping zone is equal to the result of performing a convolution operation between two matrices.

image convolution

To put it simple, the convolution between two matrices is to perform a dot product between them, i.e. ∑xN∑yN(Vxy(A)⋅Vxy(B))\sum_{x}^{N}\sum_{y}^{N}\big(V_{xy}(A) \cdot V_{xy}(B)\big)∑xN​∑yN​(Vxy​(A)⋅Vxy​(B)) where Vxy(A)V_{xy}(A)Vxy​(A) and is the value of the cell in the matrix A at the position of (x,y)(x, y)(x,y).

From the above formulas, one can clearly see why the result of convolution is the number of overlapping ones.

Usually, the image convolution is performed between an image and a specific kernel matrix, in order to obtain certain effects such as blurring or sharpening. In our case, we would perform the convolution between the matrix A and the shifted matrix B which serves as a kernel.

More importantly, we should shift the matrix with truncation and zero padding, in order to obtain a proper kernel for convolution.

shift with padding

    As a result, rather than manually counting the number of overlapping ones, we could perform the convolution operation instead.

Algorithm

Overall, we enumerate all possible kernels (by shifting the matrix B), and then perform the convolution operation to count the overlapping ones. The algorithm can be broke down into the following steps:

    First of all, we extend both the width and height of the matrix B to N+2(N−1)=3N−2N + 2(N-1) = 3N-2N+2(N−1)=3N−2, and pad the extended cells with zeros, as follows:

kernels

    From the extended and padded matrix B, we then can extract the kernel one by one.

    For each kernel, we perform the convolution operation with the matrix A to count the number of overlapping ones.

    At the end, we return the maximal value of overlapping ones.

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        import numpy as np
        A = np.array(A)
        B = np.array(B)

        dim = len(A)
        # extend the matrix to a wider range for the later kernel extraction.
        B_padded = np.pad(B, dim-1, mode='constant', constant_values=(0, 0))

        max_overlaps = 0
        for x_shift in range(dim*2 - 1):
            for y_shift in range(dim* 2 - 1):
                # extract a kernel from the padded matrix
                kernel = B_padded[x_shift:x_shift+dim, y_shift:y_shift+dim]
                # convolution between A and kernel
                non_zeros = np.sum(A * kernel)
                max_overlaps = max(max_overlaps, non_zeros)

        return max_overlaps

Note that, in the Python solution, we utilise the numpy package, which is a well-known library in the tasks of data processing and machine learning.

The numpy library is highly optimized for the matrix operations, which is why it runs faster than the Approach #1, although they have the same time complexity.

Complexity Analysis

Let NNN be the width of the matrix.

    Time Complexity: O(N4)\mathcal{O}(N^4)O(N4)

        We iterate through (2N−1)⋅(2N−1)(2N-1) \cdot (2N-1)(2N−1)⋅(2N−1) number of kernels.

        For each kernel, we perform a convolution operation, which takes O(N2)\mathcal{O}(N^2)O(N2) time.

        To sum up, the overall time complexity of the algorithm would be (2N−1)⋅(2N−1)⋅O(N2)=O(N4)(2N-1) \cdot (2N-1) \cdot \mathcal{O}(N^2) = \mathcal{O}(N^4)(2N−1)⋅(2N−1)⋅O(N2)=O(N4).

    Space Complexity: O(N2)\mathcal{O}(N^2)O(N2)
        We extend the matrix B to the size of (3N−2)⋅(3N−2)(3N-2) \cdot (3N-2)(3N−2)⋅(3N−2), which would require the space of O(N2)\mathcal{O}(N^2)O(N2).

"""