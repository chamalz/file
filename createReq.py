import sys
f1=open("file.txt","a")
f1.write(str(sys.argv[1])+"\n")
f1.close()
