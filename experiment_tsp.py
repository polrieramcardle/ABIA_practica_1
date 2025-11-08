from aima3.search import hill_climbing, simulated_annealing
from camions_problema import CamionsProblema
from camions_parametres import ProblemParameters
from camions_estat import generate_greedy_initial_state, generate_initial_state, generate_empty_initial_state
from abia_Gasolina import Gasolineres, CentresDistribucio
import time
import random

# Seeds per les rèpliques
seeds = [42, 123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627]

# Tipus d'estat inicial
initial_states_funcs = {
    "empty": generate_empty_initial_state,
    "random": generate_initial_state,
    "greedy": generate_greedy_initial_state
}

# Nombre de rèpliques
n_repliques = len(seeds)

for estat_nom, func_estat in initial_states_funcs.items():
    print(f"=== Estat inicial: {estat_nom} ===")
    
    for i, seed in enumerate(seeds):
        # Generar gasolineres i centres amb seed diferent cada rèplica
        gasolineres = Gasolineres(num_gasolineres=100, seed=seed)
        centres = CentresDistribucio(num_centres=5, multiplicitat=1, seed=seed+1)

        # Paràmetres del problema
        params = ProblemParameters(
            km=640,
            n_viatges=5,
            valor=1000,
            cost_km=2,
            gasolineres=gasolineres,
            centres=centres
        )

        # Generar estat inicial
        initial_state = func_estat(params)
        problema = CamionsProblema(initial_state)

        # Hill Climbing
        start = time.time()
        hc_result = hill_climbing(problema)
        temps_hc = time.time() - start
        valor_hc = problema.value(hc_result)

        # Simulated Annealing
        start = time.time()
        sa_result = simulated_annealing(problema)
        temps_sa = time.time() - start
        valor_sa = problema.value(sa_result)

        # Mostrar resultats
        print(f"Rèplica {i+1} | Seed: {seed} | "
              f"Hill Climbing: {valor_hc:.2f}, {temps_hc:.4f}s | "
              f"Simulated Annealing: {valor_sa:.2f}, {temps_sa:.4f}s")
    
    print("--------------------------------------------")
