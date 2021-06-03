import numpy as np

def FFT(d):
    n=len(d)
    if n==1:
        return d
    W = np.exp(-1j*2*np.pi/n)
    d_even, d_odd = d[::2],d[1::2]
    y_even,y_odd = FFT(d_even),FFT(d_odd)
    y = [0+0j]*n
    for j in range(int(n/2)):
        y[j] = y_even[j] + W**j*y_odd[j]
        y[j+int(n/2)] = y_even[j] - W**j*y_odd[j]
    return np.array(y)
