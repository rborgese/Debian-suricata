import subprocess
import errno



def call_start():
    tmp_file = open("Outputs/Start.txt", "w")
    subprocess.call(["./Shell/Start.sh"], stdout=tmp_file)

def call_deps():
    tmp_file = open("Outputs/deps.txt", "w")
    subprocess.call(["./Shell/deps_suricata.sh"])

def call_install():
    tmp_file= open("Outputs/install.txt", "w")
    subprocess.call(["./Shell/installSuricata.sh"], stdout=tmp_file)
    tmp_file.close()



call_install()
