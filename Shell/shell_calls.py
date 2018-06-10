from subprocess import PIPE, run
import errno
from bs4 import BeautifulSoup

# Template function using BeautifulSoup to add to html
def generic_soup(text):
    html_file = open("Web/html/outputs/shell_out.html").read()
    soup = BeautifulSoup(html_file, "html.parser")
    tag = soup.find("div", {"id": "shellout"})
    newTag = soup.new_tag("p")
    newTag.append(text)
    tag.append(newTag)
    tag.append("\n")
    with open("Web/html/outputs/shell_out.html", "w") as shellout:
        shellout.write(str(soup))

def reset_soup():
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

# Shell calls

def call_start():
    output = "Adding execute permissions"
    run(["./Shell/scripts/Start.sh"])
    generic_soup(output)

def call_deps():
    output = run(["./Shell/scripts/deps_suricata.sh"], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    out_array = str(output.stdout).split()
    generic_soup("Installing all dependencies")

def call_install():
    output = run(["./Shell/scripts/installSuricata.sh"], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    out_array = str(output.stdout).split()
    generic_soup("Making and installing")

# Shell tests

def call_ls():
    output = run(["./Shell/scripts/ls.sh"], stdout=PIPE, universal_newlines=True)
    out_array = str(output.stdout).split()
    generic_soup("lil wayne")

reset_soup()
