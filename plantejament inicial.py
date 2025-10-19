class Camio:
    '''
    Conté les coords, els tancs disponibles, els km acumulats i els viatges acumulats
    Serà modificat cada cop que arribi a una gasolinera o una warehouse. Ha de tenir una ruta pròpia que sigui solució,
    i que amb l'heurística, s'haurà de modificar en funció dels seu cost-benefici
    (crec que realment no cal una classe Camió, ja que tota la informació es pot guardar a l'Estat)
    '''
    def __init__(self, id_camio, cx, cy, capacitat_tanc):
        self.id_camio = id_camio
        self.cx = cx
        self.cy = cy
        self.capacitat_tanc = capacitat_tanc
        self.tanc_actual = capacitat_tanc
        self.km_acumulats = 0
        self.viatges_acumulats = 0
    
    

class Estat:
    '''
    És el conjunt de camions amb tota la seva informació. Aquesta classe representarà l'estat del problema entre accions 
    dels operadors. Serà aquella modificada pels operadors i contindrà el benefici, el qual hem de maximitzar per mitjà d'una heurísitca.

    '''
    def __init__(self, num_camions: int):
        self.num_camions = num_camions
