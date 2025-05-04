"""Erstellt den Plot von zwei Doppelpendeln mit unterschiedlichen Anfangswinkeln."""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def show(simulate, method, alpha0, beta0, alpha_dot0, beta_dot0, steps, t_max, h, g, l, damping, difference):
    """Erstellt den Plot von zwei Doppelpendeln mit unterschiedlichen Anfangswinkeln."""
    
    font = {'family':'normal', 'weight':'light', 'size':10}

    matplotlib.rc('font', **font)
    
    time = np.linspace(0, t_max, steps)
    
    # Anfangsbedingungen A
    alpha0_A = alpha0 + difference   # Anfangswinkel alpha (rad)
    beta0_A = beta0 + difference      # Anfangswinkel beta (rad)
    alpha_dot0_A = 0.0                          # Anfangswinkelgeschwindigkeit alpha (rad/s)
    beta_dot0_A = 0.0                           # Anfangswinkelgeschwindigkeit beta (rad/s)

    alpha_A, beta_A, alpha_dot_A, beta_dot_A = simulate(alpha0_A, beta0_A, alpha_dot0_A, beta_dot0_A, steps, h, g, l, damping)

    # Anfangsbedingungen B
    alpha0_B = alpha0                      # Anfangswinkel alpha (rad)
    beta0_B = beta0                        # Anfangswinkel beta (rad)
    alpha_dot0_B = 0.0                          # Anfangswinkelgeschwindigkeit alpha (rad/s)
    beta_dot0_B = 0.0                           # Anfangswinkelgeschwindigkeit beta (rad/s)

    alpha_B, beta_B, alpha_dot_B, beta_dot_B = simulate(alpha0_B, beta0_B, alpha_dot0_B, beta_dot0_B, steps, h, g, l, damping)

    # Berechnung der Positionen der Pendelkörper
    x1_A = l * np.sin(alpha_A)
    y1_A = -l * np.cos(alpha_A)
    x2_A = x1_A + l * np.sin(beta_A)
    y2_A = y1_A- l * np.cos(beta_A)

    x1_B = l * np.sin(alpha_B)
    y1_B = -l * np.cos(alpha_B)
    x2_B = x1_B + l * np.sin(beta_B)
    y2_B = y1_B - l * np.cos(beta_B)

    x_max = 3 * l
    y_max = 3 * l

    fig, ax = plt.subplots(figsize=(10, 7))

    ax.set_xlim(-x_max, x_max)
    ax.set_ylim(-y_max, y_max)

    ax.set_aspect("equal", adjustable="box")
    
    ax.set_title("Plot von zwei Doppelpendeln mit unterschiedlichen Anfangswinkeln")
 
    ax.set_xlabel(
                "X-Position (in m) des zweiten Massestücks\n\n"
                f"Verfahren: {method}\n"
                f"h = {h:.2e} s | t_max = {t_max} s\n"
                f"g = {g} m/s² | l = {l} m | d = {damping}\n"
                f"α₀ = {alpha0 * 180 / np.pi:.1f}° | β₀ = {beta0 * 180 / np.pi:.1f}°\n"
                f"α̇₀ = {alpha_dot0 * 180 / np.pi:.1f}°/s | β̇₀ = {beta_dot0 * 180 / np.pi:.1f}°/s\n"
                f"Δα₀ und Δβ₀ (Beginn der Simulation): {difference * 180 / np.pi:.2e}°"
                )

    ax.set_ylabel("Y-Position (in m) des zweiten Massestücks")

    ax.plot(x2_A, y2_A, color="blue", label="Pendel A")
    ax.plot(x2_B, y2_B, color="red", label="Pendel B")

    ax.grid()
    ax.legend()

    return fig
