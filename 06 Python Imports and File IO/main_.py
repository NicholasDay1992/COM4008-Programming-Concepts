import sys  # For handling command-line arguments
import argparse  # For more advanced argument parsing
import logging  # For logging purposes

def main():
    print("Hello from main.py!")
    nick_obj = Student("Nick", 12345678)
    nick_obj.print()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)  # Exit with a non-zero status to indicate an error
        
