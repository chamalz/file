import json
import requests
import httplib2
from oauth2client import GOOGLE_REVOKE_URI, GOOGLE_TOKEN_URI, client
def reftok():
 CLIENT_ID = '466949743446-a2vbpkaedt4u2l49g4m2ahj48opp3utf.apps.googleusercontent.com'
 CLIENT_SECRET = 'gPt2I0jMvbh-c-chJ7I1EoKC'
 
 REFRESH_TOKEN = '1//041KV8JoZmZryCgYIARAAGAQSNwF-L9IrwO1cOU8tGlgL8SRb10Vysh9PeXiKABWgEFm6iYIujlMFlKV_1K_2IGcF7Ij--ZQ-HMI'
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
    ,"parents": ['19VGDFwot2dDcFfAEVNzICrf1Uhw4bkj4']
    ,"mimeType": "application/vnd.google-apps.document"
    
    
 }
 files = {
    'data': ('metadata', json.dumps(metadata), 'application/json')
     ,'file': ('csv', open(fdata, "rb").read())
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
import binascii
start_time = time.time()
ff="rnddd"
file1=open(ff,"w")
mytok=reftok()
cont=0
xx=0
scont=0
s=""
while True:
  a=(time.time() - start_time)
  a=int(a)
  if a>3500:
    mytok=reftok()
    start_time = time.time()
  cont=cont+1
  y=int(binascii.hexlify(os.urandom(20)),16)
  private_key = y.to_bytes(32, 'big')
  public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
  addr = keccak_256(public_key).digest()[-20:]
  addr=addr.hex()
  private_key=private_key.hex()
  scont=scont+1 
  s=s+str(addr)+","+str(private_key)+","
  if scont>15:
    s=s[:-1]+'\n'
    file1.write(s)
    s=""
    scont=0
  if cont>9890:
    if s!="":
      file1.write(s[:-1])
      s=""
      scont=0
    file1.close()
    bl=0
    slp=5
    while bl==0:
      st=up(ff,ff,mytok)
      if '"mimeType": "application/vnd.google-apps.spreadsheet"' in st:
       bl=1
       xx=xx+1
       fc1=open("contt.txt","w")
       fc1.write("number files: "+str(xx))
       fc1.close()
      else:
       fc1=open("DriveErorr.txt","a")
       fc1.write("contt:"+str(xx)+"\n FileName:"+str(ff)+"\n"+str(s)+"\n")
       fc1.close()
       time.sleep(slp)
       slp=slp+2
    os.remove(ff)
    ff=str(private_key)+"RND"
    file1=open(ff,"w")
    cont=0
