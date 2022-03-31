from numpy import *


psi = lambda phi: pi/2 + phi/2
a_0 = lambda phi: exp((3/2 * pi + phi/2 - psi(phi))*tan(phi))


def q(c, N_c, gamma, D, N_q, B, N_gamma):
    return c*N_c + gamma*D*N_q + gamma/2 * B * N_gamma    
    
def N_c(phi):
    return (tan(psi(phi)) + cos(psi(phi) - phi)**2/(sin(psi(phi))*cos(psi(phi))))*((a_0(phi)**2 * (1+sin(phi)-1)))
 
def N_q(phi):
    return cos(psi(phi) - phi)/cos(psi(phi)) * a_0(phi)**2 * tan(pi/2 + phi/2)
 

def N_gamma(phi, K_py):
    return 0.5 * tan(phi) * (K_py/cos(phi)**2 - 1)



