"""Erstellt den Plot des Doppelpendels mit den gegebenen Anfangsbedingungen."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def show(simulate, method, alpha0, beta0, alpha_dot0, beta_dot0, steps, t_max, h, g, l, damping):
    """Erstellt den Plot des Doppelpendels mit den gegebenen Anfangsbedingungen."""

    time = np.linspace(0, t_max, steps)

    alpha, beta, alpha_dot, beta_dot = simulate(alpha0, beta0, alpha_dot0, beta_dot0, steps, h, g, l, damping)

    # Berechnung der Positionen der Pendelkörper
    x1 = l * np.sin(alpha)
    y1 = -l * np.cos(alpha)
    x2 = x1 + l * np.sin(beta)
    y2 = y1 - l * np.cos(beta)

    # Plot
    x_max = 2.5 * l
    y_max = 2.5 * l

    fig, ax = plt.subplots(figsize=(10, 7))

    ax.set_xlim(-x_max, x_max)
    ax.set_ylim(-y_max, y_max)
    ax.set_aspect('equal', adjustable='box')
    
    ax.set_title("Visualisierung eines Doppelpendels")
 
    ax.set_xlabel(
                "X-Position (in m)\n\n"
                f"Verfahren: {method}\n"
                f"h = {h:.2e} s | t_max = {t_max} s\n"
                f"g = {g} m/s² | l = {l} m | d = {damping}\n"
                f"α₀ = {alpha0 * 180 / np.pi:.1f}° | β₀ = {beta0 * 180 / np.pi:.1f}°\n"
                f"α̇₀ = {alpha_dot0 * 180 / np.pi:.1f}°/s | β̇₀ = {beta_dot0 * 180 / np.pi:.1f}°/s"
                )
    ax.set_ylabel("Y-Position (in m)")

    ax.plot(x1, y1, color="red", label="Punkt 1")
    ax.plot(x2, y2, color="blue", label="Punkt 2")

    ax.legend()
    ax.grid()
    
    return fig
