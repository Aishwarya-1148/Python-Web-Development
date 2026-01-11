# Program: Binary File Handling in Python
# Includes: Write and Read (separate try–except blocks)
# Comments include function/mode explanations + why we use 'with' keyword

# ----------------------------------------------------
# Why we use 'with':
# ----------------------------------------------------
# The 'with' keyword automatically closes the file
# after the block is finished, even if an error occurs.
# This prevents resource leaks and avoids using file.close().
# It's the safest and recommended way to handle files in Python.
# ----------------------------------------------------


# ----------------------------------------
# 1️⃣ WRITE to a Binary File
# ----------------------------------------
try:
    # Bytes data to write (b'' means binary literal)
    data = b"Hello Students! This is binary data."

    # open("file", "wb")
    # "wb" → write binary (creates or overwrites a file)
    with open("sample.bin", "wb") as file:
        file.write(data)       # write() → writes bytes to file
        print("Step 1: Binary file written successfully!\n")

except Exception as e:
    print("Error in Writing File:", e)


# ----------------------------------------
# 2️⃣ READ from a Binary File
# ----------------------------------------
try:
    # open("file", "rb")
    # "rb" → read binary (reads file as bytes)
    with open("sample.bin", "rb") as file:
        content = file.read()  # read() → reads entire file as bytes

        print("Step 2: Binary file read successfully!")
        print("Content in bytes:", content)

except Exception as e:
    print("Error in Reading File:", e)


# ------------------------------------------
# Copy an Image File in Python (Binary Mode)
try:
    # Open the original image in READ BINARY mode
    with open("luffy.jpeg", "rb") as original:
        image_data = original.read()   # Read entire image as bytes

    # Open a new file in WRITE BINARY mode
    with open("copied_image.jpeg", "wb") as copy_file:
        copy_file.write(image_data)    # Write the bytes into new file

    print("Image copied successfully!")

except Exception as e:
    print("Error:", e)
