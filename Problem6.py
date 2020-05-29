from pip._vendor.distlib.compat import raw_input

for i in range(int(raw_input('Enter Input'))): #More than 4 lines will result in 0 score. Blank lines won't be counted.
    a = int(raw_input('Enter Input')); A = set(raw_input().split());b = int(raw_input()); B = set(raw_input().split())
    if A.issubset(B) : print ('True')
    else : print ('False')