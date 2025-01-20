# main.py
from modules.extraction import ExtractionHandler, DiskSpaceChecker
from modules.command_handler import CommandExecutor
import sys

def main():
    # Example usage
    file_path = "example.7z"
    output_dir = "./extracted"

    print("Checking disk space...")
    if not DiskSpaceChecker.sufficient_disk_space(file_path):
        print("Not enough disk space.")
        sys.exit(1)

    print("Extracting archive...")
    if ExtractionHandler.extract_archive(file_path, output_dir):
        print(f"Extraction complete. Files are in {output_dir}")
    else:
        print("Extraction failed.")

    # Secure eval example
    expression = "2 + 2 * 3"
    print(f"Evaluating expression: {expression}")
    result = CommandExecutor.evaluate_expression(expression)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
