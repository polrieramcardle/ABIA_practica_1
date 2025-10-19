from aima3.search import Problem
from camions_estat import StateRepresentation

class CamionsProblema(Problem):
    '''
    Definició del problema dels camions com a problema de cerca.
    '''
    def __init__(self, initial_state: StateRepresentation):
        super().__init__(initial_state)
