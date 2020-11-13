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
from flask import Flask, request, jsonify
import os.path
from os import path

app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":
        req = request.form
        fname =str(req.get("fname"))
        if path.exists('file.txt')==True :
          return "<xmp>" +str("  فایل دیگری در حال دانلود است لطفا منتطر بمانید ")+"  "+"</xmp>"



        f = os.popen("python createReq.py "+fname)
        now = f.read()  
        #return redirect(request.url)
    return render_template("b.html",fname=fname)


@app.route("/dl", methods=["GET", "POST"])
def dl():
  #path = "file.txt"
  req = request.form
  fname =str(req.get("fname"))
  err=0
  ln=0
  try:
   file1 = open("fsize.txt","r")  
   ln=file1.read() 
   file1.close()
  except FileNotFoundError:
   return "<xmp>" +str("  1فایل پیدا نشد  ")+"  "+"</xmp>"
  ln=int(ln)
  length = os.path.getsize(fname)
  length=int(length)
  if ln<length:
    return "<xmp>" +str(" فایل در حال آپلود میباشد لطفا منتظر بمانید")+"  "+"</xmp>"






  try:
   return send_file(fname, as_attachment=True)
  except:
   err=1 
   return "<xmp>" +str("  2فایل پیدا نشد  ")+"  "+"</xmp>"
  finally:
   if err==0: 
    os.remove(fname)










@app.route('/', methods=["GET", "POST"])
def hello_world():
    cmd=str(request.args.get("cmd"))
    if cmd=="u":
      fname=str(request.args.get("fname"))
      if path.exists(fname)==True :
        return
      fsize=str(request.args.get("fsize"))
      data=request.get_data()
      f=open(fname, 'ab')
      f.write(data)
      f.close
      f=open("fsize.txt", 'w')
      f.write(fsize)
      f.close
      return "<xmp>" +str(len(data))+"  "+"</xmp>"
    else if cmd=="checkjob":
      try:
       file1 = open("file.txt","r")  
       fn=file1.read() 
       file1.close()
      except FileNotFoundError:
       return
      return  str(fn)
    else:
     return render_template("a.html")

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
