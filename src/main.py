from textnode import *
from text_to_html import *
from split_nodes_delimiter import *
from markdown_to_blocks import *
import os
import shutil

def main():
    if os.path.exists("/home/jschasse/workspace/github.com/jschasse/site_generator/public"):
        shutil.rmtree("/home/jschasse/workspace/github.com/jschasse/site_generator/public", ignore_errors=True)
    copy_directory("/home/jschasse/workspace/github.com/jschasse/site_generator/static", "/home/jschasse/workspace/github.com/jschasse/site_generator/public")



def copy_directory(source_path, dest_path):
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    for directories in os.listdir(source_path):
        from_path = os.path.join(source_path, directories)
        to_path = os.path.join(dest_path, directories)
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            os.mkdir(os.path.join(from_path, to_path))
            copy_directory(from_path, to_path)

   

if __name__ == "__main__":
    main()