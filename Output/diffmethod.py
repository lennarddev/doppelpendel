"""Erstellt den Vergleich der Euler und RK4 Methode für das Doppelpendel."""
import numpy as np
import matplotlib.pyplot as plt

from Functions import euler, rk4

def show(alpha0, beta0, alpha_dot0, beta_dot0, steps, t_max, h, g, l, damping):
    """Erstellt den Vergleich der Euler und RK4 Methode für das Doppelpendel."""
    
    time = np.linspace(0, t_max, steps)
    
    # Euler Methode
    alpha_A, beta_A, alpha_dot_A, beta_dot_A = euler.simulate(alpha0, beta0, alpha_dot0, beta_dot0, steps, h, g, l, damping)
    
    # RK4 Methode
    alpha_B, beta_B, alpha_dot_B, beta_dot_B = rk4.simulate(alpha0, beta0, alpha_dot0, beta_dot0, steps, h, g, l, damping)

    fig, ax = plt.subplots(figsize=(10, 7))

    ax.set_title("Vergleich von Euler und RK4 für das Doppelpendel")
    ax.set_xlabel(
                "Zeit (in s)\n\n"
                f"h = {h:.2e} s | t_max = {t_max} s\n"
                f"g = {g} m/s² | l = {l} m | d = {damping}\n"
                f"α₀ = {alpha0 * 180 / np.pi:.1f}° | β₀ = {beta0 * 180 / np.pi:.1f}°\n"
                f"α̇₀ = {alpha_dot0 * 180 / np.pi:.1f}°/s | β̇₀ = {beta_dot0 * 180 / np.pi:.1f}°/s"
                )
    ax.set_ylabel("β/PI (in rad)")

    ax.plot(time, beta_A/np.pi, color="red", label="βA (Euler)")
    ax.plot(time, beta_B/np.pi, color="blue", label="βB (RK4)")
    ax.plot(time, beta_A - beta_B, color="orange", label="βA - βB")

    ax.set_aspect('equal', adjustable='box')

    ax.legend()
    ax.grid()
    
    return fig
