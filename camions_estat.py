from camions_parametres import ProblemParameters

class StateRepresentation(object):
    def __init__(self, params: ProblemParameters): #llista de sets que un set és un contenidor i els elements del set són els paquets
        self.params = params


def generate_initial_state(params: ProblemParameters) -> StateRepresentation:
    pass