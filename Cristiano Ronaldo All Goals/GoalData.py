class Goal:
    dia : str
    competicion : str
    visita_local : str
    equipo_local : str
    equipo_visitante : str
    marcador_local : int
    marcador_visitante : int
    goles_anotados : int
    asistencias : int
    minutos_jugados : int
    def __init__(self, dia, competicion, visita_local, equipo_local, equipo_visitante, marcador_local, marcador_visitante, goles_anotados, asistencias, minutos_jugados):
        self.dia = dia
        self.competicion = competicion
        self.visita_local = visita_local
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.marcador_local = marcador_local
        self.marcador_visitante = marcador_visitante
        self.goles_anotados = goles_anotados
        self.asistencias = asistencias
        self.minutos_jugados = minutos_jugados
    def to_dict(self):
        return{
            "dia" : self.dia,
            "competicion" : self.competicion,
            "visita_local" : self.visita_local,
            "equipo_local" : self.equipo_local,
            "equipo_visitante" : self.equipo_visitante,
            "marcador_local" : self.marcador_local,
            "marcador_visitante" : self.marcador_visitante,
            "goles_anotados" : self.goles_anotados,
            "asistencias" : self.asistencias,
            "minutos_jugados" : self.minutos_jugados,
        }