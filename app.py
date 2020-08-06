import os
import shutil
import os.path
from os import path
import time

def main():
    print("Text to be printed when program starts")

    src_folder = os.getcwd()
    order_num = input("Skriv inn gjennomgangsnummer: ")
    license_num = input("Skriv inn bilnummer: ")
    
    target = r"target_path"
    target = target + "\\" + license_num
    target_order_num = target + "\\" + order_num

    if path.exists(target_order_num):
        print("Benytter samme mappe")
    elif path.exists(target):
        os.mkdir(target_order_num)
    else:
        os.mkdir(target)
        os.mkdir(target_order_num)

    for count, filename in enumerate(os.listdir(src_folder + "\\")):
        if filename.endswith(('.jpg', '.png', '.jpeg', '.bmp')):
            dst = order_num + "-" + str(count + 1) + ".jpg"
            src = src_folder + "\\" + filenametarget_order_num 

            os.rename(src, dst)
            print(f"Fra: {filename} til: {dst} ")

            shutil.move(dst, target_order_num)

            os.startfile(target_order_num)
        

if _name_ == '_main_':
    main()
