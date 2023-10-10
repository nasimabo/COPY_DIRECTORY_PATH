import shutil

source_directory = "F:/Work"
destination_directory = "F:/Work/back_work"

try:
    shutil.copytree(source_directory,destination_directory)
except FileExistsError as err:
    print(err)
except:
    print("Unknown error - terminating program!")
    raise
