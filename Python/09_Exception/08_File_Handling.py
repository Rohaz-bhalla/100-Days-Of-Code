# file = open("File.txt", "w")
# try:
#     file.write("Hey there, this is a file generated via python")
# finally:
#     file.close()

with open("file_2.txt", "w") as file:
    file.write("Just another file generated via python")