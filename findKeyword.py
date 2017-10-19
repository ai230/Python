import os


def rename_files():
    # 1) get file name from a folder
    file_list = os.listdir(r"C:\Users\ai\Desktop\prank")
    print(file_list)
    save_path = os.getcwd()
    print("this is current path ", save_path)
    os.chdir(r"C:\Users\ai\Desktop\Python\prank")
    
    # 2) for each file rename the filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(file_name.maketrans('','','0123456789')))

    os.chdir(save_path)


rename_files()
