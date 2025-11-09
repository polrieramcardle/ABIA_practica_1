from aima3.search import hill_climbing
from camions_problema import CamionsProblema
from camions_parametres import ProblemParameters
from camions_estat import generate_greedy_initial_state
from abia_Gasolina import Gasolineres, CentresDistribucio
import time

# ----------------------------------------
# Configuració del problema
# ----------------------------------------
gasolineres = Gasolineres(num_gasolineres=100, seed=1234)
centres = CentresDistribucio(num_centres=10, multiplicitat=1, seed=1234)

params = ProblemParameters(
    km=640,  # Màxim km per camió
    n_viatges=5,  # Màxim viatges per camió
    valor=1000,  # Valor base del dipòsit (€)
    cost_km=2,  # Cost per km recorregut (€/km)
    gasolineres=gasolineres,
    centres=centres
)

# Estat inicial
initial_state = generate_greedy_initial_state(params)

# ----------------------------------------
# Definició de conjunts d'operadors per provar
# ----------------------------------------
conjunts_operadors = {
    "swapCentres": ["swapCentres"],
    "mourePeticio": ["mourePeticio"],
    "swap+moure": ["swapCentres", "mourePeticio"],
    "swap+moure+intercanvia": ["swapCentres", "mourePeticio", "intercanviaPeticio"]
}

# ----------------------------------------
# Experiments
# ----------------------------------------
for nom_conjunt, operadors in conjunts_operadors.items():
    print(f"\n=== Experiment amb operadors: {nom_conjunt} ===")
    
    # Crear una nova instància del problema per cada experiment
    problema = CamionsProblema(initial_state)
    problema.operadors = operadors  # Afegir aquesta línia per configurar els operadors
    
    start = time.perf_counter()
    solucio = hill_climbing(problema)
    end = time.perf_counter()
    temps_ms = (end - start) * 1000
    
    # Benefici total: Ingressos - Cost km - Penalització
    ingressos = solucio.calcular_ingressos_servits()
    cost_km = solucio.calcular_cost_km()
    penalitzacio = solucio.calcular_penalitzacio_pendents()
    benefici = ingressos - cost_km - penalitzacio
    
    peticions_servides = len(solucio._get_peticions_servides())
    peticions_totals = len(solucio.peticions_info)
    peticions_pendents = peticions_totals - peticions_servides
    
    km_totals = sum(solucio._calcular_km_viatge(id_camio, viatge)
                    for id_camio, camio in enumerate(solucio.camions)
                    for viatge in camio)
    
    # Mostrar resultats
    print(f"Benefici obtingut: {benefici:.2f} €")
    print(f"Temps d'execució: {temps_ms:.2f} ms")
    print(f"Peticions servides: {peticions_servides}/{peticions_totals}")
    print(f"Peticions pendents: {peticions_pendents}")
    print(f"Km totals recorreguts: {km_totals:.2f} km")
    print("-" * 70)