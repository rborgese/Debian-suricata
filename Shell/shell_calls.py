import subprocess
from bs4 import BeautifulSoup
import os

# Template function to clean log files
def clean_log(path):
    if os.path.isfile(path):
        os.remove(path)
    else:
        print("File does not exist")



# Template function for outputing logs to txt file
def output_log(log, path):
        file_open = open(path, "a")
        file_open.write(log)

# Template function using BeautifulSoup to add to html
def generic_soup(text):
    html_file = open("Web/html/outputs/shell_out.html").read()
    soup = BeautifulSoup(html_file, "html.parser")
    tag = soup.find("div", {"id": "shellout"})
    newTag = soup.new_tag("p")
    newTag.append(text)
    tag.div.append(newTag)
    tag.div.append("\n")
    with open("Web/html/outputs/shell_out.html", "w") as shellout:
        shellout.write(str(soup))

# Function that cleans shell_out.html
def reset_soup():
    print("Reseting shell_out")
    html_file = open("Web/html/outputs/shell_out.html").read()
    soup = BeautifulSoup(html_file, "html.parser")
    tag = soup.find("div", {"id": "shellout"})
    newTag = soup.new_tag("div")
    tag.div.extract()
    newTag.append("\n")
    tag.append(newTag)
    tag.append("\n")
    with open("Web/html/outputs/shell_out.html", "w") as shellout:
        shellout.write(str(soup))
    print("Done")


# Shell calls
def call_start():
    out_path = "Outputs/Start.txt"
    clean_log(out_path)
    output = "Adding execute permissions"
    subprocess.run(["./Shell/scripts/Start.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    generic_soup("Adding execute permissions")
    if not output.stderr:
        for line in output.stdout.splitlines():
            new_line_txt = line + "\n"
            output_log(new_line_txt, out_path)
    if output.stderr:
        for line in output.stderr.splitlines():
            new_line_txt = line + "\n"
            generic_soup("Error: " + line)
            output_log(new_line_txt, out_path)

def call_deps():
    out_path = "Outputs/deps.txt"
    clean_log(out_path)
    output = subprocess.run(["./Shell/scripts/deps_suricata.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out_array = str(output.stdout).split()
    generic_soup("Installing all necessary dependencies, creating log file at: {}".format(out_path))
    if not output.stderr:
        for line in output.stdout.splitlines():
            new_line_txt = line + "\n"
            output_log(new_line_txt, out_path)
    if output.stderr:
        for line in output.stderr.splitlines():
            new_line_txt = line + "\n"
            generic_soup("Error: " + line)
            output_log(new_line_txt, out_path)

def call_install():
    out_path = "Outputs/install.txt"
    clean_log(out_path)
    output = suprocess.run(["./Shell/scripts/installSuricata.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out_array = str(output.stdout).split()
    generic_soup("Making and installing, creating log file at: {}".format(out_path))
    if not output.stderr:
        for line in output.stdout.splitlines():
            new_line_txt = line + "\n"
            output_log(new_line_txt, out_path)
    if output.stderr:
        for line in output.stderr.splitlines():
            new_line_txt = line + "\n"
            generic_soup("Error: " + line)
            output_log(new_line_txt, out_path)


# Shell tests
def call_ls():
    out_path = "Outputs/ls.txt"
    clean_log(out_path)
    output = subprocess.run(["./Shell/tests/ls.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not output.stderr:
        generic_soup("No error")
        for line in output.stdout.splitlines():
            new_line_txt = line + "\n"
            output_log(new_line_txt, out_path)
    if output.stderr:
        for line in output.stderr.splitlines():
            new_line_txt = line + "\n"
            generic_soup("Error: " + line)
            output_log(new_line_txt, out_path)

def call_cd():
    out_path = "Outputs/cd.txt"
    clean_log(out_path)
    output = subprocess.run(["./Shell/tests/cd.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not output.stderr:
        generic_soup("No error")
        for line in output.stdout.splitlines():
            new_line_txt = line + "\n"
            output_log(new_line_txt, out_path)
    if output.stderr:
        for line in output.stderr.splitlines():
            new_line_txt = line + "\n"
            generic_soup("Error: " + line)
            output_log(new_line_txt, out_path)

def call_bad_cd():
    out_path = "Outputs/cd.txt"
    clean_log(out_path)
    output = subprocess.run(["./Shell/tests/bad_cd.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not output.stderr:
        generic_soup("No error")
        for line in output.stdout.splitlines():
            new_line_txt = line + "\n"
            output_log(new_line_txt, out_path)
    if output.stderr:
        for line in output.stderr.splitlines():
            new_line_txt = line + "\n"
            generic_soup("Error: " + line)
            output_log(new_line_txt, out_path)


call_ls()
call_cd()
call_bad_cd()
