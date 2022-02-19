import pandas as pd
class DataFrame():
    def __init__(self,df):
        self._nombre = df
        self._df = pd.read_json('Data/'+str(df)+'.json')
    @property
    def df(self):
        return self._df
    
    def exportar(self):
        self._df.to_json('Data/'+str(self._nombre)+'.json')

    def capturado(self, nPok):
        self._df.loc[nPok, ["Captura"]]=[1]
    
    def actualizar(self, fila, columna, datoAct):
        self._df.loc[fila, [columna][0]]=[datoAct]

