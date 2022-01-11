import pathlib
i=1
for path in pathlib.Path(r"directory_path_here").iterdir():
    if path.is_file():
        old_name = path.stem
        print(old_name)
        old_extension = path.suffix
        directory = path.parent
        new_name = "starting_name_of_file"+str(i)+ old_extension
        path.rename(pathlib.Path(directory, new_name))
        i=i+1
