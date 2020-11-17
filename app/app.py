from flask import Flask, render_template, request
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
import requests
import json
import time
import random

# method that helps us simulate cpu load
def get_shell_script_output_using_check_output(cpu, cpuLoad, io, mem, memSize, timeout):
    stress_ng = "stress-ng"
    if cpu != None:
        stress_ng = stress_ng + " --cpu {cpu}"
    if cpuLoad != None:
        stress_ng = stress_ng + " --cpu-load {cpuLoad}"
    if io != None:
        stress_ng = stress_ng + " --io {io}"
    if mem != None:
        stress_ng = stress_ng + " --vm {mem}"
    if memSize != None:
        stress_ng = stress_ng + " --vm-bytes {memSize}"
    if timeout != None:
        stress_ng = stress_ng + " --timeout {timeout}"
    stress_ng = stress_ng + " --metrics-brief"

    stdout = check_output(
        stress_ng.format(cpu=cpu, cpuLoad=cpuLoad, io=io, mem=mem, memSize=memSize, timeout=timeout), stderr=subprocess.STDOUT, shell=True).decode('utf-8')
    return stdout


app = Flask(__name__)


@app.route('/')
def index():

    return "New Demo"


@app.route('/test')
def test():
    return "This is the test!!!!"

@app.route('/db')
def dbWork():
    return "This is where we could call a database"

# canary?cpu=2&cpuLoad=25&io=4&memSize=10m&timeout=30s
@app.route('/canary')
def canary():
    cpu = request.args.get('cpu')
    cpuLoad = request.args.get('cpuLoad')
    io = request.args.get('io')
    mem = request.args.get('mem')
    memSize = request.args.get('memSize')
    timeout = request.args.get('timeout')
    return '<pre>'+get_shell_script_output_using_check_output(cpu, cpuLoad, io, mem, memSize, timeout)+'</pre>'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
