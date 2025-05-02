"""Berechnung der Winkel und Winkelgeschwindigkeiten mit dem Runge-Kutta-Verfahren."""
import numpy as np
from Functions import derivatives

def simulate(alpha0, beta0, alpha_dot0, beta_dot0, steps, h, g, l, damping):
    """Berechnung der Winkel und Winkelgeschwindigkeiten mit dem Runge-Kutta-Verfahren."""
    
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
        
        k1 = derivatives.calculate(*y, g=g, l=l, damping=damping)
        k2 = derivatives.calculate(*(y + h/2 * k1), g=g, l=l, damping=damping)
        k3 = derivatives.calculate(*(y + h/2 * k2), g=g, l=l, damping=damping)
        k4 = derivatives.calculate(*(y + h * k3), g=g, l=l, damping=damping)
        
        y_next = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        
        alpha[i + 1], beta[i + 1], alpha_dot[i + 1], beta_dot[i + 1] = y_next
        
    return alpha, beta, alpha_dot, beta_dot
