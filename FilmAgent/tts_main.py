import os

# Define the ROOT variable dynamically
ROOT = os.path.abspath(os.path.dirname(__file__))

# Example usage of ROOT
if __name__ == "__main__":
    print(f"The ROOT path is set to: {ROOT}")
