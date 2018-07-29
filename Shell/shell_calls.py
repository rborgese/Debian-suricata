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
        new_file = open(path, "w")
        new_file.close()



# Template function for outputing logs to txt file
def output_log(log, path):
        file_open = open(path, "a")
        file_open.write(log)
        file_open.close()



## Shell calls

# Function that calls shell script to add execute permissions to scripts
def call_start():
    out_path = "Outputs/Start.log"
    clean_log(out_path)
    output = subprocess.run(["./Shell/scripts/Start.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    yield "Adding execute permissions"
    if not output.stderr:
        yield "Success"
    if output.stderr:
        for line in output.stderr.splitlines():
            new_line_txt = line + "\n"
            yield "Error: " + line
            output_log(new_line_txt, out_path)

# Function that calls shell script to install all necessary dependencies
def call_deps(passwd):
    out_path = "Outputs/deps.log"
    clean_log(out_path)
    yield "Installing all necessary dependencies, creating log file at: {}".format(out_path)
    yield "This might take a while"
    if str(type(passwd)) == "<class 'str'>":
        passwd = str.encode(passwd)
    try:
        subprocess.run(["sudo", "whoami"], stderr=subprocess.STDOUT,input=passwd, timeout=3)
    except subprocess.TimeoutExpired as e:
        yield e
        return
    output = subprocess.run(["./Shell/scripts/deps_suricata.sh"], stderr=subprocess.STDOUT, timeout=3, input=passwd)
    if not output.stderr:
        yield "All requirements met"
        for line in output.stdout.splitlines():
            new_line_txt = line + "\n"
            output_log(new_line_txt, out_path)
    if output.stderr:
        print("the output ", output.stderr)
        yield "An error ocurred, please check the log file at {}, the error will also be displayed below".format(out_path)
        for line in output.stderr.splitlines():
            new_line_txt = line + "\n"
            yield "Error: " + line
            output_log(new_line_txt, out_path)



# Function that calls shell script to make and install suricata
def call_install():
    out_path = "Outputs/install.log"
    clean_log(out_path)
    yield "Making and installing, creating log file at: {}".format(out_path)
    yield "This might also take a while"
    output = subprocess.run(["./Shell/scripts/installSuricata.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not output.stderr:
        yield "It seems everything went ok, however it is recommended to run Simple Test"
        for line in output.stdout.splitlines():
            new_line_txt = line + "\n"
            output_log(new_line_txt, out_path)
    if output.stderr:
        for line in output.stderr.splitlines():
            new_line_txt = line + "\n"
            yield "Error: " + line
            output_log(new_line_txt, out_path)


## Shell tests

# Calls ls, outputs stdout to log file
def call_ls():
    out_path = "Outputs/ls.log"
    clean_log(out_path)
    output = subprocess.run(["./Shell/tests/ls.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not output.stderr:
        yield "No error"
        for line in output.stdout.splitlines():
            new_line_txt = line + "\n"
            output_log(new_line_txt, out_path)
    if output.stderr:
        for line in output.stderr.splitlines():
            new_line_txt = line + "\n"
            yield "Error: " + line + ", Check log file at {}".format(out_path)
            output_log(new_line_txt, out_path)

# Calls cd into a directory outputs stdout to log file
def call_cd():
    out_path = "Outputs/cd.log"
    clean_log(out_path)
    output = subprocess.run(["./Shell/tests/cd.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not output.stderr:
        yield "No error"
        for line in output.stdout.splitlines():
            new_line_txt = line + "\n"
            output_log(new_line_txt, out_path)
    if output.stderr:
        for line in output.stderr.splitlines():
            new_line_txt = line + "\n"
            yield "Error: " + line + ", Check log file at {}".format(out_path)
            output_log(new_line_txt, out_path)

# Calls cd into fake directories to output stderr to html and log file
def call_bad_cd():
    out_path = "Outputs/cd.log"
    clean_log(out_path)
    output = subprocess.run(["./Shell/tests/bad_cd.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not output.stderr:
        yield "No error"
        for line in output.stdout.splitlines():
            new_line_txt = line + "\n"
            output_log(new_line_txt, out_path)
    if output.stderr:
        for line in output.stderr.splitlines():
            new_line_txt = line + "\n"
            yield "Error: " + line + ", Check log file at {}".format(out_path)
            output_log(new_line_txt, out_path)

# Gets the password from websocket runs sudo whoami if password is incorrect yields timeout exception
def call_sudo_try(passwd):
    out_path = "Outputs/sudo_try.log"
    clean_log(out_path)
    if str(type(passwd)) == "<class 'str'>":
        passwd = str.encode(passwd)
    try:
        output = subprocess.run(["sudo", "whoami"], input=passwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        if not output.stderr:
            yield "Password accepted"
            for line in output.stdout.splitlines():
                line = line.decode()
                yield line
                new_line_txt = line + "\n"
                output_log(new_line_txt, out_path)
        if output.stderr:
            yield "An error ocurred, please check the log file at {}, the error will also be displayed below".format(out_path)
            for line in output.stderr.splitlines():
                line = line.decode()
                new_line_txt = line + "\n"
                yield "Error: " + line
                output_log(new_line_txt, out_path)
    except subprocess.TimeoutExpired as e:
        yield str(e) + ", Your password might be incorrect"
        return
