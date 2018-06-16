from bottle import route, run, static_file
from Shell import shell_calls

# Reading html files
def read_file(theFile):
    file = open(theFile, "r")
    html = file.read()
    file.close()
    return html


# Serve static Js and Css files
@route("/Web/CSS/Bootstrap/<filename>")
def serve_bootstrap(filename):
    return static_file(filename, root="Web/CSS/Bootstrap/")

@route("/Web/Jquery/<filename>")
def serve_jquery(filename):
    return static_file(filename, root="Web/Jquery/")

@route("/Web/Js/<filename>")
def serve_js(filename):
    return static_file(filename, root="Web/Js/")

# Iframe for logs
@route("/Web/html/outputs/<filename>")
def serve_iframe(filename):
    shell_out = read_file("Web/html/outputs/{}".format(filename))
    return shell_out

# Shell calls
@route("/Shell/clean")
def clean_iframe():
    shell_calls.reset_soup()

@route("/Shell/scripts/Start.sh")
def start_install():
    shell_calls.call_start()
    #shell_calls.call_deps()
    #shell_calls.call_install()

# Shell Tests
@route("/Shell/tests/ls.sh")
def test_ls():
    shell_calls.call_ls()

@route("/Shell/tests/cd.sh")
def test_cd():
    shell_calls.call_cd()
    shell_calls.call_bad_cd()




# User Interface
@route('/')
@route('/home')
def hello():
    index = read_file("Web/index.html")
    return index

run(host='localhost', port=8080, debug=True)
