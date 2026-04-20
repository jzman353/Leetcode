"""
71. Simplify Path
Medium
Topics
premium lock icon
Companies
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.

Example 1:

Input: path = "/home/"

Output: "/home"

Explanation:

The trailing slash should be removed.

Example 2:

Input: path = "/home//foo/"

Output: "/home/foo"

Explanation:

Multiple consecutive slashes are replaced by a single one.

Example 3:

Input: path = "/home/user/Documents/../Pictures"

Output: "/home/user/Pictures"

Explanation:

A double period ".." refers to the directory up a level (the parent directory).

Example 4:

Input: path = "/../"

Output: "/"

Explanation:

Going one level up from the root directory is not possible.

Example 5:

Input: path = "/.../a/../b/c/../d/./"

Output: "/.../b/d"

Explanation:

"..." is a valid name for a directory in this problem.

Constraints:

1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.

100%
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        l = []
        for i in range(len(s)):
            if s[i] and s[i] != '.':
                if s[i] == '..':
                    if l:
                        l.pop()
                    continue
                else:
                    l.append(s[i])

        return '/'+'/'.join(l)

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.simplifyPath(input1)
        print(ans)
        return ans

    # --- Provided examples ---
    assert test("/home/") == "/home"                            # trailing slash removed
    assert test("/home//foo/") == "/home/foo"                   # multiple slashes collapsed
    assert test("/home/user/Documents/../Pictures") == "/home/user/Pictures"  # '..' goes up one
    assert test("/../") == "/"                                  # can't go above root
    assert test("/.../a/../b/c/../d/./") == "/.../b/d"          # '...' is a valid dir name

    # --- Single period '.' (current directory) ---
    assert test("/./") == "/"                                   # '.' at root
    assert test("/home/./foo") == "/home/foo"                   # '.' in middle
    assert test("/a/./b/./c") == "/a/b/c"                       # multiple '.'s
    assert test("/./././.") == "/"                              # only dots

    # --- Double period '..' (parent directory) ---
    assert test("/a/b/c/..") == "/a/b"                          # '..' at end
    assert test("/a/b/c/../..") == "/a"                         # two '..'s
    assert test("/a/../../..") == "/"                           # '..' beyond root clamps to '/'
    assert test("/a/../b/../c") == "/c"                         # alternating '..'
    assert test("/a/b/c/../../d") == "/a/d"                     # alternating '..'

    # --- Multiple slashes ---
    assert test("///") == "/"                                   # only slashes → root
    assert test("/a///b////c") == "/a/b/c"                      # many consecutive slashes
    assert test("//home//user//") == "/home/user"               # leading double slash

    # --- Valid multi-period names ('...', '....', etc.) ---
    assert test("/....") == "/...."                             # four dots = valid name
    assert test("/.../...") == "/.../..."                       # chain of triple dots
    assert test("/a/.../b") == "/a/.../b"                       # triple dot in middle

    # --- Root path ---
    assert test("/") == "/"                                     # already root
    assert test("//") == "/"                                    # double slash root

    # --- Underscores, digits, mixed names ---
    assert test("/my_folder/sub_dir") == "/my_folder/sub_dir"   # underscores
    assert test("/abc123/def456") == "/abc123/def456"           # digits in name
    assert test("/a1_b2/.../c3") == "/a1_b2/.../c3"             # mixed

    # --- Long chains ---
    assert test("/a/b/c/d/e/f/g") == "/a/b/c/d/e/f/g"           # deep path
    assert test("/a/b/c/../../..") == "/"                       # unwind full path
    assert test("/a/b/../c/d/../e") == "/a/c/e"                 # interleaved '..'

    # --- '..' that exceeds root depth ---
    assert test("/a/../../b/../c//.//") == "/c"  # your failing case
    assert test("/a/b/../../..") == "/"  # 3 levels up from depth 2
    assert test("/a/../../../b") == "/b"  # multiple excess '..' then continue
    assert test("/a/b/../../../c") == "/c"  # unwind past root then descend
    assert test("/../../a") == "/a"  # leading excess '..'
    assert test("/../../../") == "/"  # all excess '..' → root

    # --- '..' + trailing slashes + '.' mixed ---
    assert test("/a/b/.//..//") == "/a"  # '.', '..', '//' at end
    assert test("/a//./b/..//") == "/a"  # mixed slashes and '..'
    assert test("/a/./b/./c/..//./") == "/a/b"  # long chain of mixed
    assert test("//a//b//..//.//") == "/a"  # double slashes everywhere
    assert test("/a/b/c/./../..//.//") == "/a"  # deep then unwind with noise

    # --- '..' + valid multi-period names ---
    assert test("/.../..") == "/"  # '...' then '..' goes up
    assert test("/a/.../..") == "/a"  # '..' after valid '...'
    assert test("/.../a/../../b") == "/b"  # excess '..' after '...' dir
    assert test("/..../..") == "/"  # '..' after '....'

    # --- Trailing and leading noise ---
    assert test("/a//") == "/a"  # trailing double slash
    assert test("/a/b///") == "/a/b"  # trailing triple slash
    assert test("//a") == "/a"  # leading double slash + name
    assert test("///a///b///") == "/a/b"  # slashes everywhere

    # --- Single character names ---
    assert test("/a/b/c") == "/a/b/c"
    assert test("/a/../b/../c/../d") == "/d"  # every dir immediately undone
    assert test("/a/b/c/../../../d/e/f") == "/d/e/f"  # full unwind then descend

    print("All tests completed successfully.")