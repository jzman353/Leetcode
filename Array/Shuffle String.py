#9.8%

def restoreString(s: str, indices) -> str:
    dict1 = {}
    length = len(s)
    for i in range(length):
        dict1[indices[i]] = s[i]
    ans = ""
    for i in range(length):
        ans = ans + dict1[i]
    return ans

print(restoreString("codeleet",[4,5,6,7,0,2,1,3]))
print(restoreString("abc",[0,1,2]))
print(restoreString("aiohn",[3,1,4,2,0]))
print(restoreString("aaiougrt",[4,0,2,6,7,3,1,5]))
print(restoreString("art",[1,0,2]))

"""def restoreString(s: str, indices) -> str:
    ans=[""]*len(s)
    for i in range(0,len(s)):
        ans[indices[i]]=s[i]
    return "".join(ans)"""