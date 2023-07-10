import pydoc
import os
import sys

def is_documented(file_path):
    """Checks if the given Python file is documented.

    Args:
        file_path: A string that represents the path of the Python file.

    Returns:
        A boolean that indicates whether the file is documented or not.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"{file_path} does not exist.")
        return False

    # Check if the file is a Python file
    if not file_path.endswith(".py"):
        print(f"{file_path} is not a Python file.")
        return False

    # Get the module name from the file path
    module_name = os.path.splitext(os.path.basename(file_path))[0]

    # Get the documentation for the module
    try:
        module_doc = pydoc.render_doc(module_name)
    except:
        print(f"{module_name} is not documented(module documentation).")
        return False

    # Check if the documentation contains any text
    if not module_doc.strip():
        print(f"{module_name} has no documentation(module).")
        return False

    print(f"{module_name} is documented.")
    return True

if __name__ == "__main__":
    # Get the file path from the command line argument
    if len(sys.argv) < 2:
        print("Usage: python doc_check.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]

    is_documented(file_path)
