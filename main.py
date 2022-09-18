# directories controller
import os
# files controller
import shutil

path = f"C://Users//{os.getlogin()}//Downloads"
dir_list = os.listdir(path)

for item in dir_list:
    # get file extension
    fileExtension = os.path.splitext(item)[1]
    print(len(fileExtension))
    if len(fileExtension) == 0:
        continue
    fileTypes = open(".//data//typeDirect.txt", "r")
    for line in fileTypes.readlines():
        extension, directory = line.split(":")
        directory = directory.strip()
        print(f'{fileExtension} == {extension}')
        if fileExtension == extension:
            print('here')
            if os.path.exists(f'C://Users//jlva_//Downloads//{directory}'):
                print('directory exist')
                shutil.move(f'C://Users//jlva_//Downloads//{item}', f'C://Users//jlva_//Downloads//{directory}')
            else:
                print(f'C://Users//jlva_//Downloads//{directory}')
                os.makedirs(f'C://Users//jlva_//Downloads//{directory}')
                shutil.move(f'C://Users//jlva_//Downloads//{item}',
                            f'C://Users//jlva_//Downloads//{directory}')
    fileTypes.close()
