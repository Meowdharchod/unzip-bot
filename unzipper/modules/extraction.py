# modules/extraction.py
import os
import shutil
import subprocess
from pathlib import Path

class ExtractionHandler:
    """Handles archive extraction operations."""

    @staticmethod
    def extract_archive(file_path: str, output_dir: str) -> bool:
        """
        Extracts archive files to the output directory.
        Supports split archives and high compression ratios.
        """
        try:
            # Ensure output directory exists
            os.makedirs(output_dir, exist_ok=True)

            # Run extraction using 7z
            result = subprocess.run(
                ['7z', 'x', file_path, f'-o{output_dir}', '-y'],
                capture_output=True,
                text=True
            )

            # Check for errors
            if result.returncode != 0:
                print(f"Extraction failed: {result.stderr}")
                return False
            return True
        except Exception as e:
            print(f"An error occurred during extraction: {e}")
            return False


class DiskSpaceChecker:
    """Checks available disk space."""

    @staticmethod
    def sufficient_disk_space(file_path: str, buffer_ratio: float = 1.2) -> bool:
        """
        Checks if there is sufficient disk space for the extraction.

        Args:
            file_path (str): Path to the file being extracted.
            buffer_ratio (float): Safety buffer multiplier.

        Returns:
            bool: True if sufficient space is available, False otherwise.
        """
        try:
            stat = os.statvfs('/')
            free_space = stat.f_bavail * stat.f_frsize
            required_space = os.path.getsize(file_path) * buffer_ratio
            return free_space >= required_space
        except FileNotFoundError:
            print("File not found for disk space calculation.")
            return False
