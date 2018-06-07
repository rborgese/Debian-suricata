import subprocess
import errno
from bs4 import BeautifulSoup


def call_start():
    tmp_stdout = ""
    subprocess.call(["./Shell/Start.sh"], stdout=tmp_stdout)

def call_deps():
    tmp_stdout = ""
    subprocess.call(["./Shell/deps_suricata.sh"])

def call_install():
    tmp_stdout = ""
    subprocess.call(["./Shell/installSuricata.sh"], stdout=tmp_stdout)

def call_test():
    tmp_stdout = ""
    subprocess.call(["./Shell/ls_test.sh"], stdout=tmp_stdout)


call_test()
