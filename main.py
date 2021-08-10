
from vpython import *

tgraph = graph(xtitle='x',ytitle='f(X)', xmin=-3.1,xmax=5,width=1200,height=600)
ff= gcurve(color=color.blue, label="f(t)")
fg= gcurve(color=color.red, label="g(t)")
# fc= gcurve(color=color.green, label="f*g")

fc = gvbars(color=color.green,delta=0.005)
fcline = gcurve()

def f(t):
  if 0<= t <=1:
      return(1)
  else:
      return(0)

def g(t):
  if 0<= t <=2:
      return(1)
  elif -1<= t <0:
      return(t+1)
  else:
      return(0)

def convo(x):
  sum = 0
  t = -2
  dx = 0.005
  while t<5:
    sum = sum + f(x-t) * g(t) * dx
    t = t + dx
  return(sum)

def static():
    t=-2
    dt=0.005
    while t<5:
        ff.plot(t,f(t))
        fg.plot(t,g(t))
        # fc.plot(t,convo(t))
        t=t+dt

def motion():
    dx = 0.004
    x=-3
    dt = 0.005
    while x<5:
        rate(300)
        data = []
        t = -3
        while t<5:
            data = data + [[t,f(t-x)]]
            t = t + dt
        ff.data = data
        fg.plot(x, g(t))
        fc.plot(x,convo(x))
        fcline.plot(x,convo(x))
        x = x + dx
# static()
motion()