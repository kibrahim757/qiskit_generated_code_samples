# If the file does not exist, return an empty dictionary
def read_account_file(file_path='account_info.conf', separator='='):
    """
    Reads a file containing key-value pairs separated by a specified separator.
    
    Args:
        file_path (str): Path to the file to read.
        separator (str): The character that separates keys and values in the file.
        
    Returns:
        dict: A dictionary containing the key-value pairs from the file.
    """
    keys = {}
    
    try:
        with open(file_path, 'r') as f:
            for line in f:
                if separator in line:
                    # Find the name and value by splitting the string
                    name, value = line.split(separator, 1)
                    # Assign key value pair to dict
                    keys[name.strip()] = value.strip()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    
    return keys