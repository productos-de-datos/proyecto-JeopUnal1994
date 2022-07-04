def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional



    """
    import pandas as pd

    #Leemos la data limpia 
    df = pd.read_csv("data_lake/cleansed/precios-horarios.csv", index_col=None, header=0)
    #Le damos los titulos a las columnas del dataframe segun lo solicitado
    df = df[["fecha", "precio"]]
    df["fecha"] = pd.to_datetime(df["fecha"])
    #Agrupamos por fecha y sacamos la media al precio
    compute_daily_prices = df.groupby("fecha").mean({"precio": "precio"})
    compute_daily_prices.reset_index(inplace=True)
    compute_daily_prices.to_csv("data_lake/business/precios-diarios.csv", index=None, header=True)
    
    #raise NotImplementedError("Implementar esta función")

### TEST ###
#los datos van desde el dia 20 mes 7 de 1995, hasta el dia 30 mes 4 de 2021 para un equivalente a 
#9417 dias por lo cual si se saco el promedio diario, deben haber 9417 registros.
def test_cantidad_dias():
    import pandas as pd
    data = pd.read_csv("data_lake/business/precios-diarios.csv")
    assert len(data) == 9417

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    compute_daily_prices()


