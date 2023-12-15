# Sony RAW Star Selector

## Overview

This Python script is designed for Sony photographers who shoot in RAW + JPEG formats. It helps you easily find and transfer all 5-star rated RAW images from your camera to a designated folder. This tool is especially useful for streamlining your post-shoot workflow.

**Compatibility:** Tested on MacBook M2 and MacBook Intel.

If you find this script useful, please consider starring this repository and sharing it with your community!

## Installation

1. **Download the Script**

   - Download `main.py` from this repository to your device.

2. **Prepare Your Environment**
   - Open the Terminal and navigate to the folder containing `main.py`:
     ```bash
     cd path/to/folder
     ```
   - If it's your first time running this script, install required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

## Usage

1. **Run the Script**

   - Execute `main.py` using the following command:
     ```bash
     python3 main.py
     ```

2. **Specify Directories**
   - Enter the pathname of the source directory (e.g., `/Volume/SD/DCIM/100MSDCF`).
   - Enter the pathname of the destination directory (e.g., `/Desktop/output`).

## FAQ

**Q: How do I find the pathname on MacOS?**
A: You can find instructions on how to locate a pathname on MacOS [here](https://apple.stackexchange.com/questions/317992/is-there-any-way-to-get-the-path-of-a-folder-in-macos).

## Script Details

**Dependencies:** `PIL` for image handling, `os` for file management, and `shutil` for file transfer.

**Functionality:**

- The script scans the specified folder for JPEG images.
- It checks each image's metadata for a 5-star rating.
- If a 5-star JPEG is found, the script locates its RAW counterpart.
- The RAW images are then copied to the designated output folder.
