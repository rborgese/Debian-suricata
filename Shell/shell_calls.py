import subprocess
import errno
from bs4 import BeautifulSoup

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
    output = "Adding execute permissions"
    subprocess.run(["./Shell/scripts/Start.sh"])
    generic_soup(output)

def call_deps():
    output = subprocess.run(["./Shell/scripts/deps_suricata.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out_array = str(output.stdout).split()
    generic_soup("Installing all dependencies")

def call_install():
    output = suprocess.run(["./Shell/scripts/installSuricata.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out_array = str(output.stdout).split()
    generic_soup("Making and installing")


# Shell tests
def call_ls():
    output = subprocess.run(["./Shell/tests/ls.sh"], stdout=subprocess.PIPE, universal_newlines=True)
    out_array = str(output.stdout).split()
    for word in out_array:
        generic_soup(word)

def call_cd():
    output = subprocess.run(["./Shell/tests/cd.sh"], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    if not output.stderr:
        generic_soup("No error")
    if output.stderr:
        generic_soup("Error: " + str(output.stderr))

def call_bad_cd():
    output = subprocess.run(["./Shell/tests/bad_cd.sh"], stderr=subprocess.PIPE)
    if not output.stderr:
        generic_soup("No error")
    if output.stderr:
        generic_soup("Error: " + str(output.stderr))
