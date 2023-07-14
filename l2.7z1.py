
import os
def rename(name, digit, source, target, nrange=None):
    directory = os.getcwd() 

    files = os.listdir(directory) 
    files = [f for f in files if f.endswith(source)]  
    if nrange:
        start, end = nrange
    else:
        start, end = 0, len(files)
    counter = 1
    for i, filename in enumerate(files[start:end], start=1):
        name_part = filename[:digit]
        new_name = f"{name_part}{name}{str(counter).zfill(digit)}.{target}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        counter += 1
rename("newname", 3, ".txt", "pdf", nrange=(1, 10))
