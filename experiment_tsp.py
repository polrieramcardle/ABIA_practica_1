import random
import time
from camions_estat import generate_initial_state, generate_greedy_initial_state, generate_empty_initial_state
from camions_problema import CamionsProblema
from aima3.search import simulated_annealing, hill_climbing
import dataclasses
from abia_Gasolina import Gasolinera, Gasolineres, Distribucio, CentresDistribucio
@dataclasses.dataclass


class ProblemParameters:
    gasolineres: Gasolineres
    centres: CentresDistribucio
    n_viatges: int
    valor: float
    cost_km: float
# --------------------------------------------

gasolineres = Gasolineres([
    Gasolinera(cx=1, cy=2, peticions=[3, 2]),
    Gasolinera(cx=5, cy=6, peticions=[1, 4]),
    Gasolinera(cx=8, cy=3, peticions=[2, 3]),
])

centres = CentresDistribucio([
    Centre(cx=0, cy=0),
    Centre(cx=10, cy=10),
    Centre(cx=5, cy=5),
])

params = ProblemParameters(
    gasolineres=gasolineres,
    centres=centres,
    n_viatges=5,
    valor=100,
    cost_km=1
)

seeds = [42, 123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627]
n_random_reps = 10

resultats = []

for seed in seeds:
    random.seed(seed)

    # === Inicialització ordenada ===
    estat_ordenat = generate_initial_state(params)
    problema_ordenat = CamionsProblema(estat_ordenat)

    inici = time.time()
    solucio_ordenada = simulated_annealing(problema_ordenat)
    temps_ordenat = time.time() - inici

    resultats.append({
        'seed': seed,
        'inicialitzacio': 'ordenada',
        'heuristica': solucio_ordenada.heuristic(),
        'temps': temps_ordenat
    })

    # === Inicialització greedy ===
    estat_greedy = generate_greedy_initial_state(params)
    problema_greedy = CamionsProblema(estat_greedy)

    inici = time.time()
    solucio_greedy = hill_climbing(problema_greedy)
    temps_greedy = time.time() - inici

    resultats.append({
        "seed": seed,
        "inicialitzacio": "greedy",
        "heuristica": solucio_greedy.heuristic(),
        "temps": temps_greedy
    })

    # === Inicialització aleatòria ===
    heuristiques_aleatories = []
    temps_aleatori_list = []

    for _ in range(n_random_reps):
        estat_aleatori = generate_empty_initial_state(params)
        problema_aleatori = CamionsProblema(estat_aleatori)

        inici = time.time()
        solucio_aleatoria = hill_climbing(problema_aleatori)
        temps_aleatori = time.time() - inici

        heuristiques_aleatories.append(solucio_aleatoria.heuristic())
        temps_aleatori_list.append(temps_aleatori)

    # Mitjana dels resultats aleatoris
    heuristica_mitjana = sum(heuristiques_aleatories) / n_random_reps
    temps_mig = sum(temps_aleatori_list) / n_random_reps

    resultats.append({
        "seed": seed,
        "inicialitzacio": "aleatoria",
        "heuristica": heuristica_mitjana,
        "temps": temps_mig
    })

# --------------------------------------------
# Mostrar resultats
# --------------------------------------------
print("RESULTATS EXPERIMENT: Influència de la solució inicial")
print("-" * 80)
for r in resultats:
    print(f"Semilla: {r['seed']:>8} | Inicialització: {r['inicialitzacio']:>9} | "
          f"Heurística final: {r['heuristica']:.2f} | Temps (s): {r['temps']:.2f}")
