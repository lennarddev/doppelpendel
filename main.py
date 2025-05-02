import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import streamlit.components.v1 as components
import io

import Functions.euler as euler
import Functions.rk4 as rk4
import Output.animation as animation
import Output.diffvalues as diffvalues
import Output.singleplot as singleplot
import Output.diffplot as diffplot
import Output.diffmethod as diffmethod

# Streamlit App
# Beschreibung
st.title("Simulation eines Doppelpendels")

st.markdown("""
            Diese Webseite simuliert ein chaotisches Doppelpendel. Sowohl die Massen der beiden Punkte, als auch die Längen der Stäbe sind gleich.

            Es können unterschiedliche Parameter für die Simulation eingestellt werden. Die Lösung erfolgt durch eine numerische Methode.
            
            Der Programmcode kann auf [GitHub](https://github.com/lennarddev/doppelpendel) eingesehen werden.
            """)

# Eingabefelder
method = st.selectbox("Numerisches Verfahren", ["Euler", "Runge-Kutta"], index=1)
outputformat = st.selectbox("Ausgabeformat", ["Animation", "Plot", "Plot der Winkelunterschiede", "Verlauf der Winkelunterschiede", "Vergleich von Euler und Runge-Kutta"], index=0)

st.subheader("Physikalische Parameter")
g = st.number_input("Erdbeschleunigung `g` (m/s²)", value=9.81)
l = st.number_input("Pendellänge `l` (m)", value=1.0)
damping = st.number_input("Dämpfungsfaktor", value=0.0)

st.subheader("Zeitparameter")
h = st.number_input("Zeitschritt `h` (s)", value=0.001, step=0.001, format="%.5f")
t_max = st.number_input("Simulationsdauer `t_max` (s)", value=30.0)

st.subheader("Anfangsbedingungen")
alpha0 = (st.number_input("Anfangswinkel `α` (°)", value=90))/180 * np.pi
beta0 = (st.number_input("Anfangswinkel `β` (°)", value=90))/180 * np.pi
alpha_dot0 = (st.number_input("Anfangsgeschwindigkeit `α̇` (°/s)", value=0.0))/180 * np.pi
beta_dot0 = (st.number_input("Anfangsgeschwindigkeit `β̇` (°/s)", value=0.0))/180 * np.pi

st.subheader("Vergleichsparameter")
st.markdown("Nur für das Anzeigen der Ausgabeformate: 'Plot der Winkelunterschiede' und"
            " 'Verlauf der Winkelunterschiede' relevant. Der Winkelunterschied wird auf die Anfangswerte des ersten Pendels addiert.")
difference = (st.number_input("Winkelunterschied Δα & Δβ (°)", value=0.001, step=0.001, format="%.6f"))/180 * np.pi

steps = int(t_max / h)

# Berechnung
def calculate():
    info_container = st.empty()
    info_container.info("Simulation wird erstellt... Dies kann einige Sekunden bis Minuten dauern, je nach gewähltem Zeitintervall und Anzahl der Schritte.")

    if outputformat == "Animation":

        fig = animation.show(simulate, method, alpha0, beta0, alpha_dot0, beta_dot0, steps, t_max, h, g, l, damping)

        st.html(fig.to_html5_video(embed_limit=200))

    elif outputformat == "Plot":
        fig = singleplot.show(simulate, method, alpha0, beta0, alpha_dot0, beta_dot0, steps, t_max, h, g, l, damping)
        st.pyplot(fig)

    elif outputformat == "Plot der Winkelunterschiede":
        fig = diffplot.show(simulate, method, alpha0, beta0, alpha_dot0, beta_dot0, steps, t_max, h, g, l, damping, difference)
        st.pyplot(fig)

    elif outputformat == "Verlauf der Winkelunterschiede":
        fig = diffvalues.show(simulate, method, alpha0, beta0, alpha_dot0, beta_dot0, steps, t_max, h, g, l, damping, difference)
        st.pyplot(fig)

    elif outputformat == "Vergleich von Euler und Runge-Kutta":
        fig = diffmethod.show(alpha0, beta0, alpha_dot0, beta_dot0, steps, t_max, h, g, l, damping)
        st.pyplot(fig)

    else:
        st.error("Ungültiges Ausgabeformat.")
        st.stop()
        
    info_container.empty()

    try:
        if not outputformat == "Animation":
            buffer = io.BytesIO()
            fig.savefig(buffer, format='png', dpi=300, bbox_inches='tight', pad_inches=0.25)
            buffer.seek(0)
            
            st.download_button(
                label="📂 Herunterladen",
                data=buffer,
                file_name="doppelpendel.png",
                mime="image/png"
            )
    except Exception as e:
        st.error(f"Fehler beim Herunterladen der Datei.: {e}")

# Start der Simulation
if st.button("🚀 Simulation starten"):
    try:
        # Wahl des numerischen Verfahrens
        if method == "Euler":
            simulate = euler.simulate
            method = "Euler"
            calculcate()
        elif method == "Runge-Kutta":
            simulate = rk4.simulate
            method = "Runge-Kutta"
            calculate()
        else:
            st.error("Ungültiges Berechnungsverfahren.")
            
    except Exception as e:
        st.error(f"Fehler bei der Berechnung.: {e}")
