import subprocess
from bs4 import BeautifulSoup
import os

# Template function to clean log files
def clean_log(path):
    if os.path.isfile(path):
        os.remove(path)
        new_file = open(path, "w")
        new_file.close()
    else:
        print("File does not exist")
        new_file = open(path, "w")
        new_file.close()



# Template function for outputing logs to txt file
def output_log(log, path):
        file_open = open(path, "a")
        file_open.write(log)
        file_open.close()

# Template function using BeautifulSoup to add to html
def generic_soup(text):
    html_file = open("Web/html/outputs/shell_out.html")
    html_string = html_file.read()
    html_file.close()
    soup = BeautifulSoup(html_string, "html.parser")
    tag = soup.find("div", {"id": "shellout"})
    newTag = soup.new_tag("p")
    newTag.append(text)
    tag.div.append(newTag)
    tag.div.append("\n")
    with open("Web/html/outputs/shell_out.html", "w") as shellout:
        shellout.write(str(soup))
        shellout.close()


# Function that cleans shell_out.html
def reset_soup():
    print("Reseting shell_out")
    html_file = open("Web/html/outputs/shell_out.html")
    html_string = html_file.read()
    html_file.close()
    soup = BeautifulSoup(html_string, "html.parser")
    tag = soup.find("div", {"id": "shellout"})
    newTag = soup.new_tag("div")
    tag.div.extract()
    newTag.append("\n")
    tag.append(newTag)
    tag.append("\n")
    with open("Web/html/outputs/shell_out.html", "w") as shellout:
        shellout.write(str(soup))
        shellout.close()
    print("Done")


# Shell calls
def call_start():
    out_path = "Outputs/Start.txt"
    clean_log(out_path)
    output = subprocess.run(["./Shell/scripts/Start.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    generic_soup("Adding execute permissions")
    if not output.stderr:
        generic_soup("Success")
    if output.stderr:
        for line in output.stderr.splitlines():
            new_line_txt = line + "\n"
            generic_soup("Error: " + line)
            output_log(new_line_txt, out_path)

def call_deps():
    out_path = "Outputs/deps.txt"
    clean_log(out_path)
    generic_soup("Installing all necessary dependencies, creating log file at: {}".format(out_path))
    generic_soup("This might take a while")
    output = subprocess.run(["./Shell/scripts/deps_suricata.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not output.stderr:
        generic_soup("All requirements met")
        for line in output.stdout.splitlines():
            new_line_txt = line + "\n"
            output_log(new_line_txt, out_path)
    if output.stderr:
        generic_soup("An error ocurred, please check the log file at {}, the error will also be displayed below".format(out_path))
        for line in output.stderr.splitlines():
            new_line_txt = line + "\n"
            generic_soup("Error: " + line)
            output_log(new_line_txt, out_path)

def call_install():
    out_path = "Outputs/install.txt"
    clean_log(out_path)
    generic_soup("Making and installing, creating log file at: {}".format(out_path))
    generic_soup("This might also take a while")
    output = suprocess.run(["./Shell/scripts/installSuricata.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not output.stderr:
        generic_soup("It seems everything went ok, however it is recommended to run Simple Test")
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
