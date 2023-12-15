from PIL import Image
import os
import shutil

extensions = ['.JPEG', '.jpeg', '.jpg', '.JPG']
target_extension = ['.ARW', '.arw']

def check_rating(filepath):
    img = Image.open(filepath) 
    xml_object = img.getxmp()
    return xml_object['xmpmeta']['RDF']['Description']['Rating']

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

     #index how many items to process]
    total_items = 0
    checked_items = 1

    for photo in os.scandir(input_directory):
        if photo.is_file() and photo.name.endswith(tuple(extensions)):
            total_items += 1

    for photo in os.scandir(input_directory):
        if photo.is_file() and photo.name.endswith(tuple(extensions)):
            print(f'\r{checked_items}/{total_items} processed', end='')

            full_path = os.path.join(input_directory, photo.name)
            rating = check_rating(full_path)

            if rating == '5':
                print(f'\n Item found {photo.name}')
                equivalent_photo_path = find_equivalent_file(input_directory, photo.name, target_extension)
                
                if equivalent_photo_path:
                    shutil.copy(equivalent_photo_path, output_directory)
                else:
                    print(f'the RAW equivalent of {photo.name} could not be found')
                    continue
