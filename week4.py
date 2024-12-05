

def read_file():
    
    # Prompts the user for a filename, reads the file content, 
    # and handles errors if the file doesn't exist or can't be read.
   
    filename = input("Enter the filename to read: ")

    try:
        # Attempt to open and read the file
        file = open(filename, 'r') 
        content = file.read()
        # print("\nFile Content:")
        print(content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist. Please check the filename and try again.")
    except PermissionError:
        print(f"Error: Permission denied. You do not have access to read the file '{filename}'.")
    finally:
        print("Thank you for your time.")

# Run the program
if __name__ == "__main__":
    read_file()
