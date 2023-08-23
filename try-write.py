# Safely open the file
file = open("hello.txt", "w")

try:
    file.write("Hello, World!")
except:
    print("the file was not able to write")
finally:
    # Make sure to close the file after using it
    file.close()
