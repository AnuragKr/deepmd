import shutil
import os
import glob

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


#Creating directory
base_path = "../lw_pimd"
for i in range(0, 20):
    os.mkdir(f"{base_path}/data_{i}")

#Copying Type Map file
source_file_1 = glob.glob("../type_data/type_map.raw")
dest_directory = glob.glob(f"{base_path}/data_*")
for dest in dest_directory:
    shutil.copy(source_file_1[0],dest)

#Copying Type file
source_file_2 = glob.glob(f"{base_path}/type.raw")
for dest in dest_directory:
    shutil.copy(source_file_2[0],dest)

#Creating Set file and then copying
source_file_3 = glob.glob(f"{base_path}/set.*")
for set_file in source_file_3:
    num = int(set_file.split('.')[3])
    os.mkdir(f"{base_path}/data_{num}/set.000")
    copytree(set_file,f"{base_path}/data_{num}/set.000/")
