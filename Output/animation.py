"""Erstellt die Animation des Doppelpendels."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib


def show(simulate, method, alpha0, beta0, alpha_dot0, beta_dot0, steps, t_max, h, g, l, damping):
    """Erstellt die Animation des Doppelpendels."""
    
    font = {'family':'normal', 'weight':'light', 'size':10}

    matplotlib.rc('font', **font)

    
    time = np.linspace(0, t_max, steps)
    
    alpha, beta, alpha_dot, beta_dot = simulate(alpha0, beta0, alpha_dot0, beta_dot0, steps, h, g, l, damping)
    
    # Berechnung der Positionen der Pendelkörper
    x1 = l * np.sin(alpha)
    y1 = -l * np.cos(alpha)
    x2 = x1 + l * np.sin(beta)
    y2 = y1 - l * np.cos(beta)

    # Animation
    x_max = 2.5 * l
    y_max = 2.5 * l
    
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-x_max, x_max)
    ax.set_ylim(-y_max, y_max)
    ax.set_aspect('equal', adjustable='box')
    ax.grid()
    
    plt.subplots_adjust(bottom=0.2)

    line, = ax.plot([], [], 'o-', lw=2, markersize=8)
    time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

    def init():
        line.set_data([], [])
        time_text.set_text('')
        return line, time_text

    fps = 60
    num_frames = int(t_max * fps)

    frame_indices = np.linspace(0, steps - 1, num_frames, dtype=int)

    def update(i):
        frame = frame_indices[i]
        x = [0, x1[frame], x2[frame]]
        y = [0, y1[frame], y2[frame]]
        line.set_data(x, y)
        time_text.set_text(f'Zeit = {time[frame]:.2f} s')
        return line, time_text

    ani = FuncAnimation(
        fig,
        update,
        frames=num_frames,
        init_func=init,
        blit=True,
        interval=1000 / fps
    )

    plt.title("Simulation eines Doppelpendels")
    plt.xlabel("X-Position (in m)\n\n"
                f"Verfahren: {method}\n"
                f"h = {h:.2e} s | t_max = {t_max} s\n"
                f"g = {g} m/s² | l = {l} m | d = {damping}\n"
                f"α₀ = {alpha0 * 180 / np.pi:.1f}° | β₀ = {beta0 * 180 / np.pi:.1f}°\n"
                f"α̇₀ = {alpha_dot0 * 180 / np.pi:.1f}°/s | β̇₀ = {beta_dot0 * 180 / np.pi:.1f}°/s"
            )
    plt.ylabel("Y-Position (in m)")

    
    return ani
