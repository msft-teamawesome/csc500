# Python code
filenames = ["file1.txt", "file2.txt", "file3.txt"]
for filename in filenames:
    if os.path.exists(filename):
        print(f"{filename} exists")
    else:
        print(f"{filename} does not exist")