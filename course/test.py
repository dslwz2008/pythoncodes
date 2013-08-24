#def naive(a, b):
#    x = a
#    y = b
#    z = 0
#    while x > 0:
#        z = z + y
#        x = x - 1
#    return z
#    
#print naive(3, 5)
#print naive(3, 6)
#print naive(2, 10)
#print range(3, 6)
#args=[3, 6]
#print range(*args)
#
#def test1(*args):
#    for item in args:
#        print item
#        
#def test(**args):
#    for item in args:
#        print item
#        
#print test1('1', '2', '3')
#voltage= "four million"
#state= "bleedin' demised"
#action= "VOOM"
##print test(voltage="four million",  action:"VOOM", state:"bleedin' demised")
#
#def parrot(voltage, state='a stiff', action='voom'):
#     print "-- This parrot wouldn't", action,
#     print "if you put", voltage, "volts through it.",
#     print "E's", state, "!"
#
#d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
#parrot(**d)
#test(**d)
#test(color="red", bold=False)
import subprocess

p = subprocess.Popen('adb help', shell=True,
    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(w,r,e) = (p.stdin, p.stdout, p.stderr)

ret = ''
while 1:
    line = r.readline()
    if not line:
        break
    ret += line

print ret
r.close()
w.close()
e.close()
