import numpy as np

Hein_2018 = dict(Tg0=-16.8, Tg8=225, lam=.543,  # DiBenedetto
                 a=.04, b=3.93,  # X_max
                 A1=np.exp(11.149), EA1=75549,  # Cure model parameters
                 A2=np.exp(8.762), EA2=50911,
                 l=.489, m=1.549, n=2.179,
                 Hr=490e3  # Enthalpy [J / kg]
                 )

Pantelelis_2005 = dict(A1=2.54e4, EA1=71.46e3,
                       A2=6.05e4, EA2=61.25e3,
                       l=.492, m=1.252, n=1.75,
                       Hr=490e3)  # Enthalpy [J / kg] Hein2018

Karkanas_1998 = dict(A1=2.6e4, EA1=74.69e3,
                     A2=5.78e4, EA2=57.88e3,
                     l=.449, m=1.217, n=1.786,
                     Hr=490e3)  # Enthalpy [J / kg] Hein2018

