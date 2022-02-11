import random

n = random.random()

import sys
 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
    
file1 = open("myfile.txt", "a")  # append mode
file1.write(str((n)) + "\n")
file1.write("\n")
file1.close()

f = open("myfile.txt", "r")
print(f.read())
f.close()

print("current one is ", n)
print("Hello world ")
