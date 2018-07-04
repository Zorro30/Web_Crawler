import os

#function to create a directory
def create_dir(directory):
    if not os.path.exists(directory):
        print ("Creating the {} directory".format(directory))
        os.makedirs(directory)

#function to create files
def create_files(dir_name,base_url):
    queue = os.path.join(dir_name,'queue.txt')
    crawled = os.path.join(dir_name,'crawled.txt')
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

#function to wirte in file
def write_file(path,data):
    with open(path, 'w') as f:
        f.write(data)

#function to append in the same file
def append_to_file(path,data):
    with open(path, 'a') as f:
        f.write(data, "\n")

def delete_file_contents(path):
    open(path,'w').close()

#function to take contents of file and put them in sets
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))#replace newline with blankspace.
        return results

#function to copy back set contents to File  
def set_to_file(links,file_name):
    with open(file_name,'w') as f:
        for l in sorted(links):
            f.write(l+'\n')
