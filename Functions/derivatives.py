"""Berechnung der Ableitungen."""
import numpy as np

def calculate(a, b, a_dot, b_dot, g, l, damping):
    """Berechnung der Ableitungen."""
    
    delta = a - b
    sin_a = np.sin(a)
    sin_b = np.sin(b)
    sin_delta = np.sin(delta)
    cos_delta = np.cos(delta)
    
    a_ddot_term1 = -a_dot**2 * sin_delta * cos_delta
    a_ddot_term2 = + (g/l) * sin_b * cos_delta
    a_ddot_term3 = - b_dot**2 * sin_delta
    a_ddot_term4 = - 2 * (g/l) * sin_a
    a_ddot_term5 = 2 - cos_delta**2

    a_ddot = ( a_ddot_term1 + a_ddot_term2 + a_ddot_term3 + a_ddot_term4) / a_ddot_term5 - damping * a_dot
    
    b_ddot = -a_ddot * cos_delta + a_dot**2 * sin_delta - (g/l) * np.sin(b) - damping * b_dot
    
    return np.array([a_dot, b_dot, a_ddot, b_ddot])
