# ----- We use json file (films.json) 

import json

with open('films.json') as f:
    filmsContent = json.load(f)
    for film in filmsContent['films']:
        # print(film) - If we want to se each object of the filmsContent
        print('{} directed by {}'.format(film['Title'], film['Director'])) # for each print title and director
        
# ----- We write in the file ("a" - Append - will append to the end of the file)
        
with open("testFile.txt", "a") as f:
    f.write("Hello! :)")
    f.close()

# ----- We read the file ("r" - Read)

with open("testFile.txt", "r") as f:
    print(f.read())

# ----- We overwrite any existing content ("w" - Write - will overwrite any existing content)

with open("testFile.txt", "w") as f:
    f.write("We deleted all the content! :(")
    f.close()

# ----- We read again after overwriting

with open("testFile.txt", "r") as f:
    print(f.read())
    
# ----- We create new file ("x" - Create - will create a file, returns an error if the file exist)
# ----- Also here we use the try except :) 

try:
    with open("testNewFile.txt", "x") as f:
        f.close()
except IOError:
    print("File exists (Maybe)")

# ----- We read and write a Binary file
# ----- 'rb' for reading binary files
# ----- 'wb' for writing binary files

# ----- Initialize binaryData to None
binaryData = None

# ----- We use the try except/because if the 'binary_file.bin' doesn't exist

try:
    with open('binaryFile.bin', 'rb') as f:
        binaryData = f.read()
except FileNotFoundError:
    print("The file 'binaryFile.bin' does not exist.")

# ----- Check if binaryData is not None before proceeding
if binaryData is not None:
    # ----- Open 'newBinaryFile.bin' for writing (create it if it doesn't exist)
    try:
        with open('newBinaryFile.bin', 'wb') as f:
            f.write(binaryData)
    except FileNotFoundError:
        print("The file 'newBinaryFile.bin' does not exist.")


