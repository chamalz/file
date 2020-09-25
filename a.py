import json
import requests
import httplib2
from oauth2client import GOOGLE_REVOKE_URI, GOOGLE_TOKEN_URI, client
def reftok():
 CLIENT_ID = '1038873846148-3e516ng6c2pe688d7j638nl2r7i3ov0e.apps.googleusercontent.com'
 CLIENT_SECRET = 'Z1zSjFPZahG08qqtZUITpBrm'
 REFRESH_TOKEN = '1//0fbJ411lVJxLKCgYIARAAGA8SNwF-L9IrmJC9uXkBMOGEZNH-Kc7oO6DB25YETvF0ai-YXkrPVcSyk3EkPCMqA8cvuKQqczg78k0'
 credentials = client.OAuth2Credentials(
 access_token=None,  # set access_token to None since we use a refresh token
 client_id=CLIENT_ID,
 client_secret=CLIENT_SECRET,
 refresh_token=REFRESH_TOKEN,
 token_expiry=None,
 token_uri=GOOGLE_TOKEN_URI,
 user_agent=None,
 revoke_uri=GOOGLE_REVOKE_URI)
 credentials.refresh(httplib2.Http())  # refresh the access token (optional)
 tok=credentials.to_json()
 http = credentials.authorize(httplib2.Http())  # apply the credentials
 idx=tok.index(', "client_id":')
 tok[18:idx-1]
 return tok[18:idx-1]
def up(fname,fdata,tokk):
 metadata = {
    "name": fname
    #,"parents": ['1S23Yth0LSFchI7y2mbYuBQXdDuqi5L2o']
    ,"mimeType": "application/vnd.google-apps.document"
     
 }
 files = {
    'data': ('metadata', json.dumps(metadata), 'application/json')
     ,'file': ('text', open(fdata, "rb").read())
      # or  open(filedirectory, "rb")
 }
 r = requests.post(
 "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart&&supportsAllDrives=true",
 headers={"Authorization": "Bearer " + tokk},
 files=files
 )
 return r.text
from coincurve import PublicKey
from sha3 import keccak_256
import os
import time
start_time = time.time()
ff="rnddd"
file1=open(ff,"w")
mytok=reftok()
cont=0
xx=0
while True:
  a=(time.time() - start_time)
  a=int(a)
  if a>3500:
    mytok=reftok()
    start_time = time.time()
  cont=cont+1
  private_key = os.urandom(32)
  public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
  addr = keccak_256(public_key).digest()[-20:]
  addr=addr.hex()
  private_key=private_key.hex()
  s=str(addr)+" "+str(private_key)+" "
  file1.write(s)
  if cont>9887:
    file1.close()
    bl=0
    slp=5
    while bl==0:
      s=up(ff,ff,mytok)
      if '"mimeType": "application/vnd.google-apps.document"' in s:
       bl=1
       xx=xx+1
       fc1=open("contt.txt","w")
       fc1.write("number files: "+str(xx))
       fc1.close()
      else:
       fc1=open("DriveErorr.txt","a")
       fc1.write("contt: "+str(xx)+"\n"+str(s)+"\n")
       fc1.close()
       time.sleep(slp)
       slp=slp+2
    os.remove(ff)
    ff=str(private_key)+"RND"
    file1=open(ff,"w")
    cont=0
