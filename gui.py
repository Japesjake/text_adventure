import os, random

# for subdirs, dirs, files in os.walk(r'.\data'):
#     print(file)

b = [1,2,3]
a = b
random.shuffle(b)
print(a)
print(b)
