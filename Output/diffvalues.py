"""Erstellt den Vergleich von zwei Doppelpendeln mit unterschiedlichen Anfangswinkeln."""
import numpy as np
import matplotlib.pyplot as plt

def show(simulate, method, alpha0, beta0, alpha_dot0, beta_dot0, steps, t_max, h, g, l, damping, difference):
    """Erstellt den Vergleich von zwei Doppelpendeln mit unterschiedlichen Anfangswinkeln."""
    
    time = np.linspace(0, t_max, steps)
    
    # Anfangsbedingungen beider Pendel
    start_alpha = np.pi / 2
    start_beta = np.pi / 2

    # Anfangsbedingungen A
    alpha0_A = start_alpha + difference   # Anfangswinkel alpha (rad)
    beta0_A = start_beta + difference      # Anfangswinkel beta (rad)
    alpha_dot0_A = 0.0                          # Anfangswinkelgeschwindigkeit alpha (rad/s)
    beta_dot0_A = 0.0                           # Anfangswinkelgeschwindigkeit beta (rad/s)

    alpha_A, beta_A, alpha_dot_A, beta_dot_A = simulate(alpha0_A, beta0_A, alpha_dot0_A, beta_dot0_A, steps, h, g, l, damping)

    # Anfangsbedingungen B
    alpha0_B = start_alpha                      # Anfangswinkel alpha (rad)
    beta0_B = start_beta                        # Anfangswinkel beta (rad)
    alpha_dot0_B = 0.0                          # Anfangswinkelgeschwindigkeit alpha (rad/s)
    beta_dot0_B = 0.0                           # Anfangswinkelgeschwindigkeit beta (rad/s)

    alpha_B, beta_B, alpha_dot_B, beta_dot_B = simulate(alpha0_B, beta0_B, alpha_dot0_B, beta_dot0_B, steps, h, g, l, damping)

    # Plot
    fig, ax = plt.subplots(figsize=(10, 7))
    
    ax.set_title("Vergleich der Winkel von zwei Doppelpendeln")

    ax.set_xlabel(
                "Zeit (in s)\n\n"
                f"Verfahren: {method}\n"
                f"h = {h:.2e} s | t_max = {t_max} s\n"
                f"g = {g} m/s² | l = {l} m | d = {damping}\n"
                f"α₀ = {alpha0 * 180 / np.pi:.1f}° | β₀ = {beta0 * 180 / np.pi:.1f}°\n"
                f"α̇₀ = {alpha_dot0 * 180 / np.pi:.1f}°/s | β̇₀ = {beta_dot0 * 180 / np.pi:.1f}°/s\n"
                f"Δα₀ und Δβ₀ (Beginn der Simulation): {difference * 180 / np.pi:.2e}°"
                )
    ax.set_ylabel("Winkelunterschied/π (in rad)")

    ax.plot(time, (alpha_A - alpha_B)/np.pi, color="red", label="Δα")
    ax.plot(time, (beta_A - beta_B)/np.pi, color="blue", label="Δβ")
    
    ax.set_aspect('equal', adjustable='box')

    ax.legend()
    ax.grid()

    return fig
