import numpy as np 
import matplotlib.pyplot as plt
from math import tan, cos, sin, radians




def N_gamma_s(alpha, beta, K_v, K_h, phi_AC, phi_BC, phi_DC):
    a = tan(alpha)**2/tan(beta)

    numerator = (1+K_v * sin(beta + phi_DC) - K_h * cos(beta + phi_DC) * cos(alpha - phi_AC - phi_BC)) 
    denominator = (1+K_v * sin(alpha - phi_AC) + K_h * cos(alpha + phi_AC) * cos(beta - phi_DC - phi_BC))

    return a * (numerator/denominator) - tan(alpha) 



if __name__ == '__main__':
    alpha = radians(60)
    beta = radians(40)
    K_v = 1.3
    K_h = 1.4
    phi_AC = radians(35)
    phi_BC = radians(30)
    __phi_DC = radians(29)

    phi_DC = np.linspace(0, 0.5,50)
    N_GAMMA_1 = []
    for _phi_DC in phi_DC:
        N_GAMMA_1.append(N_gamma_s(alpha, beta, _phi_DC, _phi_DC, phi_AC, phi_BC, __phi_DC))
    
    plt.plot(phi_DC, N_GAMMA_1)


    N_GAMMA_2 = []
    for _phi_DC in phi_DC:
        N_GAMMA_2.append(N_gamma_s(alpha, beta, _phi_DC/2, _phi_DC, phi_AC, phi_BC, __phi_DC))
    
    plt.plot(phi_DC, N_GAMMA_2)


    plt.show()

