import subprocess
from subprocess import check_output
from subprocess import Popen, PIPE
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'

@app.route('/greet')
def say_hello():
  return 'Hello from Server'

@app.route('/getemp')
def get_shell_script_output_using_communicate():
    session = Popen(['/home/opc/oci-apigw-atp/atpconnect.sh'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = session.communicate()
    if stderr:
        raise Exception("Error "+str(stderr))
    return stdout.decode('utf-8')