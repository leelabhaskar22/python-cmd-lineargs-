import sys

def add(x , y):
    return int(x) + int(y)

result = add(sys.argv[1] , sys.argv[2])
print(result)