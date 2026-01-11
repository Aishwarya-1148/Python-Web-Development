# --------------------------------------
# FILE HANDLING IN PYTHON
# Modes of File Handling
"""
1] r : Read Mode
        - Only reading is allowed.
        - File MUST already exist.

2] w : Write Mode
        - Used for writing data.
        - Creates file if it does not exist.
        - Clears old data if file already exists.

3] a : Append Mode
        - Adds new data at the end of file.
        - Creates file if it doesn't exist.
"""
# --------------------------------------


# ---------- WRITE OPERATION ----------
# Writing data into the file using write() method
writeMode = open("data.txt", "w")
writeMode.write("This is the file handling example.\nPython is writing this line.\n")
writeMode.close()
print("Data written successfully in file.\n")


# ---------- READ OPERATION WITH EXCEPTION HANDLING ----------
# Using try-except to handle FileNotFoundError

# Using read() → Reads entire file content as a single string
try:
    readMode = open("data.txt", "r")
    print("Reading using read():")
    print(readMode.read())
    readMode.close()
except FileNotFoundError:
    print("Error: The file 'data.txt' does not exist!")
print("--------------------------------------------------\n")


# ---------- readLine() ----------
# Using readline() → Reads one line at a time
try:
    readMode = open("data.txt", "r")
    print("Reading using readline():")
    print(readMode.readline())  # Reads first line
    print(readMode.readline())  # Reads second line
    readMode.close()
except FileNotFoundError:
    print("Error: The file 'data.txt' does not exist!")
print("--------------------------------------------------\n")


# ---------- readLines() + for loop ----------
# Using readlines() → Returns list of lines, then we loop through it
try:
    readMode = open("data.txt", "r")
    print("Reading using readlines() with for loop:")
    lines = readMode.readlines()

    for line in lines:
        print(line, end="")  # end="" prevents extra blank line

    readMode.close()
except FileNotFoundError:
    print("Error: The file 'data.txt' does not exist!")
print("\n--------------------------------------------------")
