#Create and write to the source file
src = open("source.txt", "w")
src.write("This is the original file.\nIt will be copied to another file.")
src.close()

#Read from source file
src = open("source.txt", "r")
data = src.read()
src.close()

#Write data to destination file
dest = open("copy.txt", "w")
dest.write(data)
dest.close()

print("File copied successfully!")
