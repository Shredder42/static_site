import os
import shutil

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)



'''
Alex written functions

def copy_directory(source, destination, initial_call=True):
    if initial_call:
        shutil.rmtree(destination)
        os.mkdir(destination)

    file_list = []
    source_dir_items = os.listdir(source)
    for item in source_dir_items:
        item_path = os.path.join(source, item)
        if os.path.isfile(item_path):
            file_list.append(item_path)
            shutil.copy(item_path, destination)
        else:
            new_dest = os.path.join(destination, item)
            os.mkdir(new_dest)                   
            file_list.extend(copy_directory(item_path, new_dest, False))

    return file_list

'''