from vpython import *
from vpython import gdots

tgraph = graph(xtitle='x', ytitle='f(X)', xmin=-15, xmax=25, width=1400, height=600)
ff = gdots(color=color.blue, label="f(t)")
fg = gdots(color=color.red, label="g(t)")
# fc= gcurve(color=color.green, label="f*g")

fc = gvbars(color=color.green, delta=0.01)
fcline = gdots()

result = 0


def f(t):
    if 3 <= t <= 8:
        return (0.99)
    else:
        return (0)


def g(t):
    if 4 <= t <= 15:
        return (1)
    else:
        return (0)


def convo(time):
    sum = 0
    t = 0
    dx = 1
    while t < 25:
        sum = sum + f(time - t) * g(t)
        t = t + dx
    return (sum)


def static(result=result):
    time = -5
    dt = 1
    while time < 25:
        ff.plot(time, f(time))
        fg.plot(time, g(time))
        result += convo(time)
        # fc.plot((time-3),convo(time))
        time = time + dt
    print('result', result)


def motion():
    dt = 1
    dx = round(0.01, 3)
    x = round(int(-2), 3)
    while x < 30:
        rate(300)
        data = []
        t = -2
        if round(x, 3) == int(round(x, 3)):
            while t < 30:
                data = data + [[t, f(t - x)]]
                t = t + dt
            ff.data = data
            fg.plot(x, g(x))
            fc.plot((x - 3), convo(x))
            fcline.plot((x - 3), convo(x))
        x = round(dx, 3) + round(x, 3)

# static()
motion()
