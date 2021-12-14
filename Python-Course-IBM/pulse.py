#!/usr/bin/python
""" Analysis of pulses, looking for high-frequency elements in pulse shapes"""

__author__ = "Daniel Brue"
__status__ = "Development"

if (__name_ == "__main__"):



    import matplotlib.pyplot as plt
    import numpy
    import scipy.fftpack as fft
    import math


    ######################################################################################
    # PULSE DEFINITION

    Nt=10001
    tmin=0.0
    tmax=10.0
    tmid=5.0
    dt=(tmax-tmin)/(Nt-1)
    nwave=40

    times=numpy.linspace(tmin,tmax,Nt)
    sig_amp=numpy.zeros_like(times)

    for i in range(Nt):
        if (times[i] < tmid):
            sig_amp[i]=0.0
        else:
            sig_amp[i] = math.sin(nwave*2*math.pi*(times[i]-tmid)/(tmax-tmid)) +\
                         0.0 #math.cos(nwave*2*math.pi*(times[i]-tmid)/(tmax-tmid))

    ######################################################################################
    # PERFORM FFT
    freq=fft.rfftfreq(Nt,dt)
    freq_amp = fft.rfft(sig_amp)

    for i in range(len(freq_amp)):
        freq_amp[i] = math.fabs(freq_amp[i])

    log_amp = numpy.zeros_like(freq_amp)
    for i in range(len(log_amp)):
        if (freq_amp[i] > 0.0):
            log_amp[i]=math.log10(freq_amp[i])
        elif (freq_amp[i] < 0.0):
            log_amp[i]=-math.log10(-freq_amp[i])
        else:
            log_amp[i]=-14.0

    ######################################################################################
    # LOOK AT THE RESULTS
    fig=plt.figure()
    ax0=fig.add_subplot(3,1,1)
    plt.plot(times,sig_amp)
    plt.xlabel("Time")
    plt.ylabel("Signal")
    ax1=fig.add_subplot(3,1,2)
    plt.plot(freq,freq_amp,"bo")
    plt.xlabel("Frequency")
    plt.ylabel("Frequency Amplitude")
    ax2=fig.add_subplot(3,1,3)
    plt.plot(freq,log_amp,"go")
    plt.xlabel("Frequency")
    plt.ylabel("Log Frequency Amplitude")
    plt.show()
