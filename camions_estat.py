from camions_parametres import ProblemParameters
from camions_operadors import CamionsOperator
from typing import List, Set, Generator


class StateRepresentation(object):

    def __init__(self, params: ProblemParameters):
        '''
        Representació de l'estat del problema de camions, amb les següents propietats:
        - params: objecte ProblemParameters amb les dades del problema
        - camions: llista de llistes de viatges per camió, on cada viatge és una llista de peticions ateses
        '''
        self.params = params

    def heuristica(self) -> float:
        """
        B_total = B - C - Pen
        On:
        - B = Ingressos dels dipòsits servits avui
        - C = Cost total dels km recorreguts
        - Pen = Penalització per peticions no servides avui
        
        Retorna: -B_total (per minimitzar, que equival a maximitzar B_total)
        """
        ingressos = self.calcular_ingressos_servits()
        cost_km = self.calcular_cost_km()
        penalitzacio = self.calcular_penalitzacio_pendents()
    
        benefici_total = ingressos - cost_km - penalitzacio
    
        return -benefici_total  # ha de ser negatiu
    
    def calcular_ingressos_servits(self) -> float:
        """
        Calcula el benefici perdut per les peticions no servides.
        Sumatori de les peticions servides avui pel seu factor de preu
        """
        benefici_perdut = 0.0
        # Implementar càlcul del benefici perdut
        return benefici_perdut
    
    def calcular_cost_km(self) -> float:
        """
        Calcula el cost total dels km recorreguts per tots els camions.
        És el cost per quilòmetre recorregut multiplicat pels km totals de tots els viatges
        """
        cost_km = 0.0
        # Implementar càlcul del cost de km totals
        return cost_km
    
    def calcular_penalitzacio_pendents(self) -> float:
        """
        Calcula la penalització per les peticions no servides avui.
        És el sumatori de les penalitzacions no ateses el dia pel que porten pendent.
        Cada petició pendent afegeix una penalització segons els dies que porta pendent.
        """
        penalitzacio = 0.0
        # Implementar càlcul de la penalització per peticions pendents
        return penalitzacio
    
    def _factor_de_preu(self, dies: int) -> float: #f(d) del meu escrit :)
        """
        Factor de preu en funció dels dies que han passat per petició.
        Els dies són estrictament positius.
        """
        if dies == 0:
            return 1.02
        else: return max(0, 1-0.02 * dies)
        
    
    def _manhattan(self, c1, c2):
        """
        Distància Manhattan entre dues coordenades (x, y)
        """
        return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
    

    def __eq__(self, other):
        return isinstance(other, StateRepresentation) and self.params == other.params
    
def generate_initial_state(params: ProblemParameters) -> StateRepresentation:
    pass