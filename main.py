"""
Sony RAW Star Selector

This Python script is designed for Sony photographers who shoot in RAW + JPEG formats.
It helps you easily find and transfer all 5-star rated RAW images from your camera to a designated folder.

Author: @dariocodes
GitHub: https://github.com/dariocodes/rate-finder

This script is released under the MIT License. See the bottom of this file for full details.

Usage:
1. Run the script using `python3 main.py`.
2. Enter the pathname of the source directory.
3. Enter the pathname of the destination directory.

For more information and FAQs, refer to the README.md file in the repository.
"""

from PIL import Image
import os
import shutil
from datetime import datetime

extensions: list[str] = ['.JPEG', '.jpeg', '.jpg', '.JPG']
target_extension: list[str] = ['.ARW', '.arw']

def check_rating(filepath: str):
    img = Image.open(filepath) 
    xml_object = img.getxmp()
    rating = xml_object['xmpmeta']['RDF']['Description']['Rating']
    if rating:
        return rating
    return None

def check_date(filepath: str, input_date: str)-> bool:
    img = Image.open(filepath) 
    xml_object = img.getxmp()
    creation_date_and_time = xml_object['xmpmeta']['RDF']['Description']['CreateDate']
    creation_date = creation_date_and_time[:10]
    if input_date == creation_date:
        return True
    else:
        return False


def find_equivalent_file(input_dir, filename, new_extensions):
    base_name, _ = os.path.splitext(filename)
    for ext in new_extensions:
        new_filename = base_name + ext
        new_filepath = os.path.join(input_dir, new_filename)
        if os.path.isfile(new_filepath):
            return new_filepath
    return None

if __name__ == '__main__':
    # assign directory
    input_directory = input(str('Path of input directory: '))
    output_directory = input(str('Path of output directory: '))

    date_process = False
    confirmation = {'yes', 'y', 'ye'}
    date_choice = (str(input('Would you like to pick a specific date?[Y/N]: '))).lower()
    if date_choice in confirmation:
        date_process = True
        date = str(input('What date would you like to process?\nPlease write it like year-month-day eg. 2023-05-02: '))

     #index how many items to process
    total_items = 0
    checked_items = 1

    for photo in os.scandir(input_directory):
        if photo.is_file() and photo.name.endswith(tuple(extensions)):
            total_items += 1

    for photo in os.scandir(input_directory):

        if photo.is_file() and photo.name.endswith(tuple(extensions)):
            print(f'\r{checked_items}/{total_items} processed', end='', flush=True)
            checked_items += 1
            full_path = os.path.join(input_directory, photo.name)
            try:
                rating = check_rating(full_path)
                if date_process == True:
                    photo_date = check_date(full_path, date)
                else:
                    photo_date = True
            except:
                print(f'Error on file {full_path}')

            if rating == '5' and photo_date:
                print(f'\n Item found {photo.name}')
                equivalent_photo_path = find_equivalent_file(input_directory, photo.name, target_extension)

                if equivalent_photo_path:
                    shutil.copy(equivalent_photo_path, output_directory)
                else:
                    print(f'the RAW equivalent of {photo.name} could not be found')
                    continue
"""
MIT License

Copyright (c) [2023] [@dariocodes]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""