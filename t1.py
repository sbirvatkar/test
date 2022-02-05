import random

n = random.random()

file1 = open("myfile.txt", "a")  # append mode
file1.write(str((n)) + "\n")
file1.write("\n")
file1.close()

print(n)
print("Hello world ")
