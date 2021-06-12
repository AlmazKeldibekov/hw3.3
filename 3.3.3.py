# def decorator(func):
#     procent = 0
#     if isinstance(str1,str) and len(str1) == 10 and isinstance(str2,str) and len(str2) == 10:

def func(str1,str2):
    procent = 0
    for i in range(10):
        if str1[i] == str2[i]:
            procent += 1
    return procent * 100 / 10

print(func('qwertyuiop','qwertyuikl'))