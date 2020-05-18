from os import listdir
from os.path import isfile, join
files_dir = "."
script_name = "link_script.bash"
this_file_name = "create_link_script.py"
files_to_filter = [this_file_name, script_name, "README.md"]

all_files = listdir(files_dir)
relevant_files = [x for x in all_files if not x.startswith(".") and x not in files_to_filter]

cd_cmd = "cd ~"
link_cmds = ["ln -nsf dotfiles/{0} .{0}".format(x) for x in relevant_files]
script_str = "\n".join([cd_cmd] + link_cmds)
with open(script_name, "w") as text_file:
    text_file.write(script_str)
