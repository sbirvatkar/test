import random

n = random.random()

file1 = open("myfile.txt", "a")  # append mode
file1.write(str((n)) + "\n")
file1.write("\n")
file1.close()

f = open("myfile.txt", "r")
print(f.read())
f.close()

print("current one is ", n)
print("Hello world ")
