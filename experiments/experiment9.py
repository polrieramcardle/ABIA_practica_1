import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from aima3.search import hill_climbing, simulated_annealing, exp_schedule

from implementacio.camions_problema import CamionsProblema
from implementacio.camions_parametres import ProblemParameters
from implementacio.camions_estat import generate_greedy_initial_state
from implementacio.abia_Gasolina import Gasolineres, CentresDistribucio

# === Configuració ===
NUM_EXECUCIONS = 10
NUM_GASOLINERES = 100
NUM_CENTRES = 10

# Acumuladors per Hill Climbing i SA
resultats = {
    "Execució": [],
    "HC_Benefici": [],
    "HC_Temps_ms": [],
    "SA_Benefici": [],
    "SA_Temps_ms": []
}

# === Experiments ===
for i in range(NUM_EXECUCIONS):
    # Generar dades amb seed diferent
    gasolineres = Gasolineres(num_gasolineres=NUM_GASOLINERES, seed=1234 + i)
    centres = CentresDistribucio(num_centres=NUM_CENTRES, multiplicitat=1, seed=1234 + i)
    
    params = ProblemParameters(
        km=640,
        n_viatges=5,
        valor=1000,
        cost_km=2,
        gasolineres=gasolineres,
        centres=centres
    )
    
    # Estat inicial (greedy)
    initial_state = generate_greedy_initial_state(params)
    
    # Problema
    problema = CamionsProblema(initial_state)
    
    # --- Hill Climbing ---
    t0 = time.perf_counter()
    sol_hc = hill_climbing(problema)
    t1 = time.perf_counter()
    temps_hc = (t1 - t0) * 1000  # ms
    
    benefici_hc = sol_hc.calcular_ingressos_servits() - sol_hc.calcular_cost_km() - sol_hc.calcular_penalitzacio_pendents()
    
    # --- Simulated Annealing ---
    t0 = time.perf_counter()
    sol_sa = simulated_annealing(problema, exp_schedule(k=0.005, lam=0.0005, limit=1000))
    t1 = time.perf_counter()
    temps_sa = (t1 - t0) * 1000  # ms
    
    benefici_sa = sol_sa.calcular_ingressos_servits() - sol_sa.calcular_cost_km() - sol_sa.calcular_penalitzacio_pendents()
    
    # Guardar resultats
    resultats["Execució"].append(i + 1)
    resultats["HC_Benefici"].append(benefici_hc)
    resultats["HC_Temps_ms"].append(temps_hc)
    resultats["SA_Benefici"].append(benefici_sa)
    resultats["SA_Temps_ms"].append(temps_sa)

# === Taula de resultats amb mitjanes ===
df = pd.DataFrame(resultats)
df.loc["Mitjana"] = df[["HC_Benefici", "HC_Temps_ms", "SA_Benefici", "SA_Temps_ms"]].mean()
print("\n=== Taula comparativa Hill Climbing vs Simulated Annealing ===")
print(df)

# === Gràfics estadístics ===

# 1️⃣ Benefici comparatiu
plt.figure(figsize=(10,6))
plt.boxplot([df["HC_Benefici"][:-1], df["SA_Benefici"][:-1]], labels=["Hill Climbing", "Simulated Annealing"])
plt.title("Benefici de la solució per algorismes")
plt.ylabel("Benefici (€)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 2️⃣ Temps d'execució comparatiu
plt.figure(figsize=(10,6))
plt.boxplot([df["HC_Temps_ms"][:-1], df["SA_Temps_ms"][:-1]], labels=["Hill Climbing", "Simulated Annealing"])
plt.title("Temps d'execució per algorismes")
plt.ylabel("Temps (ms)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 3️⃣ Opcional: comparació mitjana benefici i temps amb barres
mitjanes = df.loc["Mitjana", ["HC_Benefici", "SA_Benefici", "HC_Temps_ms", "SA_Temps_ms"]]
plt.figure(figsize=(10,6))
plt.bar(["HC Benefici","SA Benefici","HC Temps","SA Temps"], mitjanes, color=["skyblue","lightgreen","skyblue","lightgreen"])
plt.title("Mitjanes de benefici i temps")
plt.ylabel("€ / ms")
plt.show()
