#-*- coding: utf-8 -*-
"""
====================================
:mod:`test_double_slit` 
====================================
.. moduleauthor:: Ki-Hwan Kim <kh.kim@kiaps.org>
.. note:: This module is designed for use by nosetests.

Description
========

Test the 2-D FDTD code using a double slit experiment

Reference
========

* [Optical interference] http://www.sparknotes.com/physics/optics/phenom/section1.rhtml

Associated Devolopers
========
* Ki-Hwan KIM <kh.kim@kiaps.org>
*  
* 

Update
========

* 2016.3.6 dk.lee: Add irradiance()
* 2016.3.7 kh.kim: Formulate for a automatic documentation using Sphinx
                   Add test_double_slit()
"""



from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




def irradiance(d, L, wl, y, I0=1):
    """
    Returns irradience of the double-slit interferences

    :param float d: distance between two slits [micro-meter]
    :param float L: distance between the plane of slits and screen [meter]
    :param float wl: wavelength of source [nano-meter]
    :param float y: distance from central maximum [milli-meter]
    :param float I0: irradience of source

    :return float irradiance: irradience of interferences which is shown on screen.
    """

    D, Y = np.meshgrid(d, y)
    I = 4*I0*np.cos(Y*D*np.pi/(L*wl))**2 
    
    return D, Y, I 




def plot_irradiance_3d():
    """
    Plot 2d irradiance
    """

    nm = 1e-9
    um = 1e-6
    d = np.arange(5*um,25*um,um) 
    L = 5
    wl = 650*nm     # red light

    N = 200         # number of points
    y = np.linspace(0,0.5,N)
    
    D, Y, I = irradiance(d,L,wl,y) 
    fig = plt.figure(figsize=(15,10))
    ax = Axes3D(fig)

    ax.plot_wireframe(Y, D, I, color='B')
    ax.set_xlabel('Distance from central maximum')
    ax.set_ylabel('Distance between two slits')
    ax.set_zlabel('Irradiance')
    plt.show() 




def plot_irradiance():
    """
    Plot irradiance on the screen
    """

    nm = 1e-9
    um = 1e-6
    d = 20*um 
    L = 5
    wl = 650*nm     # red light

    N = 200         # number of points
    y = np.linspace(0,0.5,N)
    
    D, Y, I = irradiance(d, L, wl, y) 
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.plot(Y, I)
    ax.set_xlabel('Distance from central maximum')
    ax.set_ylabel('Irradiance')
    plt.show() 




def test_irradiance():
    """
    Test 2D-FDTD with a double-slit interference
    """
    pass
