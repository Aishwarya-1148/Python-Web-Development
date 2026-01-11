# -------------------------------
# File Handling in Python
# Modes of File Handling
"""
1] r : Read mode
        - Only reading is allowed.
        - The file MUST already exist, otherwise it will throw an error.

2] w : Write mode
        - Used to write data into the file.
        - If the file does NOT exist, Python creates it.
        - If the file exists, previous data will be removed (file opens as blank).

3] a : Append mode
        - Used to add new data at the end of the file.
        - File will be created if it doesn’t exist.
        - Previous data remains safe; new data is added at bottom.
"""
# -------------------------------


# ---------- WRITE OPERATION ----------
# Open file in write mode and insert data
writeMode = open("data.txt", "w")
writeMode.write("This is the file handling example.\nPython is writing this line.\n")
writeMode.close()  # Always close file after writing
print("Data written successfully in file.\n")


# ---------- READ OPERATION USING read() ----------
# read() → Reads entire file content as one single string
readMode = open("data.txt", "r")
print("Reading using read():")
print(readMode.read())
readMode.close()
print("----------------------------------------------\n")


# ---------- READ OPERATION USING readline() ----------
# readline() → Reads only one line at a time
readMode = open("data.txt", "r")
print("Reading using readline():")
print(readMode.readline())  # Reads 1st line
print(readMode.readline())  # Reads 2nd line
readMode.close()
print("----------------------------------------------\n")


# ---------- READ OPERATION USING readlines() + for loop ----------
# readlines() → Returns a list of all lines
readMode = open("data.txt", "r")
print("Reading using readlines() with for loop:")
lines = readMode.readlines()

for line in lines:
    print(line, end="")  # end="" removes extra new line

readMode.close()
print("\n----------------------------------------------")
