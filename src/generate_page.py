from markdown_to_html_node import *
from extract_title import *
import os
import shutil

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        from_path_file = f.read()
    with open(template_path, "r") as t:
        template_path_file = t.read()
    from_path_Node = markdown_to_html_node(from_path_file)
    from_path_tohtml = from_path_Node.to_html()
    title = extract_title(from_path_file)
    text = template_path_file.replace("{{ Title }}", title).replace("{{ Content }}", from_path_tohtml)
    with open(dest_path, "w") as dest_path_file:
        dest_path_file.write(text)
        
def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for directories in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, directories)
        to_path = os.path.join(dest_dir_path, directories)
        if os.path.isfile(from_path):
            with open(from_path, "r") as f:
                from_path_file = f.read()
            with open(template_path, "r") as t:
                template_path_file = t.read()
            from_path_Node = markdown_to_html_node(from_path_file)
            from_path_tohtml = from_path_Node.to_html()
            title = extract_title(from_path_file)
            text = template_path_file.replace("{{ Title }}", title).replace("{{ Content }}", from_path_tohtml)
            with open(to_path.replace(".md", ".html"), "w") as dest_path_file:
                dest_path_file.write(text)
        else:
            os.mkdir(os.path.join(from_path, to_path))
            generate_page_recursive(from_path, template_path, to_path)

