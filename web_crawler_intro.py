import os

#function to create a directory
def create_dir(directory):
    if not os.path.exists(directory):
        print ("Creating the {} directory".format(directory))
        os.makedirs(directory)

create_dir('Hello')