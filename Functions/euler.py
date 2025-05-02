"""Berechnung der Winkel und Winkelgeschwindigkeiten mit dem Euler-Verfahren."""
import numpy as np
from Functions import derivatives

def simulate(alpha0, beta0, alpha_dot0, beta_dot0, steps, h, g, l, damping):
    """Berechnung der Winkel und Winkelgeschwindigkeiten mit dem Euler-Verfahren."""
    
    alpha = np.zeros(steps)
    beta = np.zeros(steps)
    alpha_dot = np.zeros(steps)
    beta_dot = np.zeros(steps)
    
    alpha[0] = alpha0
    beta[0] = beta0
    alpha_dot[0] = alpha_dot0
    beta_dot[0] = beta_dot0
    
    for i in range(steps - 1):
        y = np.array([alpha[i], beta[i], alpha_dot[i], beta_dot[i]])
        
        y_next = y + h * derivatives.calculate(*y, g=g, l=l, damping=damping)

        alpha[i + 1], beta[i + 1], alpha_dot[i + 1], beta_dot[i + 1] = y_next
        
    return alpha, beta, alpha_dot, beta_dot
