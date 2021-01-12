import os
import time
import datetime
rootDir = "I:/1/"
dic={}
for dirName,subDirs,fileList in os.walk(rootDir):
  print(dirName)
  for fn in fileList:
    fnpath=dirName+fn
    st = os.stat(fnpath)
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
    # print mtime
    t=time.ctime(mtime)
    d_from_t = datetime.datetime.fromtimestamp(mtime)
    dic[fnpath]=d_from_t.strftime('%Y-%m-%d%H:%M:%S')
    # print fnpath+"- last modified:", d_from_t.strftime('%Y-%m-%d %H:%M:%S')
  pass

for x in dic:
  # p=os.path.splitext(x)[0]
  p=os.path.dirname(os.path.abspath(x))
  ext=os.path.splitext(x)[1]
  # tpath=p+"/"+dic[x]+ext
  # print tpath
  # print os.path.dirname(os.path.abspath(p))
  nname=os.path.join(rootDir,dic[x]+ext)
  # print p,ext
  print("os.rename('"+x+"','"+nname+"'')")
  os.rename(x,nname)
  pass