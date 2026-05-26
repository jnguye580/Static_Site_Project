import os
import shutil

# Recursive function that will copy all contents from staic to public
# Call function with static as source and public as the destination
# For each item, two cases:
# 1. files -> copy over to destination
# 2. folder/directory -> create that directory in destination and recursion to copy its files

def recursion_copy(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    source_items = os.listdir(source)
    for item in source_items:
        item_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, dest_path)
        else:
            recursion_copy(item_path, dest_path)

def copy_static(source , destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    recursion_copy(source, destination)