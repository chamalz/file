"""
A first simple Cloud Foundry Flask app

Author: Ian Huston
License: See LICENSE.txt

"""
from flask import Flask, request, render_template
import os
from flask import send_file
from flask import request, redirect
from flask import request
import multiprocessing
import threading
import time
import subprocess
from flask import Flask, render_template



app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":
        req = request.form
        fname =str(req.get("fname"))
        f = os.popen("python createReq.py "+fname)
        now = f.read()  
        #return redirect(request.url)
    return render_template("b.html",fname=fname)


@app.route("/dl", methods=["GET", "POST"])
def dl():
  #path = "file.txt"
  req = request.form
  fname =str(req.get("fname"))
  return send_file(fname, as_attachment=True)











@app.route('/')
def hello_world():
    #aa=request.args.get("n")
    #c=int(aa)
    return render_template("a.html")

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
