import glob,os,stat,time

def checkSum():
    val = 0
    for f in glob.glob ('*.py'):
        stats = os.stat (f)
        val += stats [stat.ST_SIZE] + stats [stat.ST_MTIME]
    return val

val=0
while (True):
    if checkSum() != val:
        val=checkSum()
        os.system ('clear')
        os.system ('nosetests')
    time.sleep(1)
