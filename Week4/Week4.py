def read_and_modify_file():
    try:
        filename = input("Enter the filename: ")
        with open(filename, 'r') as file:
            content = file.readlines()
        
        # Modify content: Add line numbers and exclamation marks
        modified_content = []
        for i, line in enumerate(content):
            modified_line = f"{i+1}: {line.strip().replace('.', '!')}\n"
            modified_content.append(modified_line)
        
        # Write to a new file
        new_filename = "Modified_" + filename
        with open(new_filename, 'w') as file:
            file.writelines(modified_content)
        
        print(f"File successfully modified and saved as {new_filename}")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: Permission denied. Cannot read or write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_modify_file()
