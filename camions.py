from aima3.search import hill_climbing, simulated_annealing
from camions_problema import CamionsProblema
from camions_parametres import ProblemParameters
from camions_estat import generate_initial_state


params = ProblemParameters()
initial_state = generate_initial_state(params)
n =simulated_annealing(CamionsProblema(initial_state))
n = hill_climbing(CamionsProblema(initial_state))
