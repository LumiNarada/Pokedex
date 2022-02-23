import pandas as pd
class DataFrame():
    def __init__(self,df):
        self._nombre = df
        self._df = pd.read_json('Data/'+str(df)+'.json')
        self._filas = self._df.shape[0]-1
        self._columnas = self._df.shape[1]-1
    @property
    def df(self):
        return self._df
    @property
    def filas(self):
        return self._filas
    @property
    def columnas(self):
        return self._columnas

    def exportar(self):
        self._df.to_json('Data/'+str(self._nombre)+'.json')

    def capturar(self, nPok):
        self._df.set_index("num", inplace=True)
        self._df.loc[nPok, ["captura"]]=[1]
        self._df.reset_index(inplace=True)
    
    def actualizar(self, index, fila, columna, datoAct):
        self._df.set_index(index, inplace=True)
        self._df.loc[fila, columna]=datoAct
        self._df.reset_index(inplace=True)
    
    def iactualizar(self,fila, columna, datoAct):
        self._df.iloc[fila, columna]=datoAct
    
    def concatenar(self, dataFrame):
        self._df=pd.concat([self._df,dataFrame],ignore_index=True)

    def eliminarFila(self, fila):
        self._df=self._df.drop(index=fila)

    """def encontrarNum(self, numIndex):
        num= self._df.set_index("num").loc[numIndex,"nombre"]
        return especie"""

    def encontrarEspecie(self, numIndex):
        especie= self._df.set_index("num").loc[numIndex,"nombre"]
        return especie

    """def encontrarNombre(self, numIndex):
        nombre= self._df.set_index("num").loc[numIndex,"nombre"]
        return nombre"""

    def set_index(self, index):
        self._df.set_index(index, inplace=True)

    def reset_index(self):
        self._df.reset_index(inplace=True)


    

