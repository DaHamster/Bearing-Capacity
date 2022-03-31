
import matplotlib.pyplot as plt 
import numpy as np

from numpy import tan, log, radians


def q_ult(gamma, H, K_sr, phi_p, N_c, c_u, B, theta):
    a = gamma * H**2 * K_sr * tan(phi_p) + N_c * c_u * (B + 2*H*tan(theta))-(B + H*tan(theta))*gamma*H
    return a/B

def sand_layer(phi_p, c_u, H, gamma, Q_U, Q_L, N_c):
    A = 0.039 * log(tan(phi_p)) - 0.164
    B = 0.597 * log(tan(phi_p)) - 0.051
    theta = A*log(c_u/(gamma*H)) + B

    K_sr = (1/(gamma*H**2 * tan(phi_p))) * ( (Q_U+Q_L)/2 - N_c * c_u * (B + 2*H*tan(theta)) - gamma * H**2 * tan(theta))
    
    return theta, K_sr

def clay_layer(phi_p, c_u, gamma, H):
    C = -3.48 * tan(phi_p) + 8.693
    K_sr = C * c_u/(gamma*H) + 2
    return K_sr


H = 1
gamma = 17
c_u = 10
phi_p = radians(30)

H = np.linspace(0.5, 10, 100)
print(q_ult(1, 1, 1, 1, 1, 1, 1, 1))

print(sand_layer(1,1,1,1,1,1,1))

K_sr_clay = clay_layer(phi_p, c_u, gamma, H)

plt.plot(H, K_sr_clay, label="clay")
plt.title('$K_{sr}$ vs H')
#plt.show()

Q_U = 5
Q_L = 5
N_c = 5
(theta, K_sr_sand) = sand_layer(phi_p, c_u, H, gamma, Q_U, Q_L, N_c)

plt.plot(H, K_sr_sand,label="Sand")

plt.legend()
plt.show()