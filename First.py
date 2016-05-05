a = [0,0,0]
b = [0,0,0]
c = [0,0,0]
print a
print b
print c
win=0
i=1
while (win==0) and (i<10):
 movex=input()
 movey=input()
 print movex,movey
 if i%2==0:
  if movey==0:
    if a[movex]==0:
    	a[movex]=2
  if movey==1:
   if b[movex]==0:
    b[movex]=2
  if movey==2:
   if c[movex]==0:
    c[movex]=2
 else:
  if movey==0:
      if a[movex]==0:   
        a[movex]=1
  if movey==1:
   if b[movex]==0:
    b[movex]=1
  if movey==2:
   if c[movex]==0:
    c[movex]=1
 print c
 print b
 print a
 

 if a[0]*a[1]*a[2]==1:
  win=1
 if a[0]*b[0]*c[0]==1:
  win=1
 if b[0]*b[1]*b[2]==1:
  win=1
 if a[1]*b[1]*c[1]==1:
  win=1
 if c[0]*c[1]*c[2]==1:
  win=1
 if a[2]*b[2]*c[2]==1:
  win=1
 if a[0]*b[1]*c[2]==1:
  win=1
 if a[2]*b[1]*c[0]==1:
  win=1
 if a[0]*a[1]*a[2]==8:
  win=2
 if a[0]*b[0]*c[0]==8:
  win=2
 if b[0]*b[1]*b[2]==8:
  win=2
 if a[1]*b[1]*c[1]==8:
  win=2
 if c[0]*c[1]*c[2]==8:
  win=2
 if a[2]*b[2]*c[2]==8:
  win=2
 if a[0]*b[1]*c[2]==8:
  win=2
 if a[2]*b[1]*c[0]==8:
  win=2
 i=i+1
if win==1:
 print 'Cong player 1'
if win==2:
 print 'Cong player 2'
if win==0:
 print 'Sorry losers.You are too stupid for this game!!!'