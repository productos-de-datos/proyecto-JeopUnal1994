def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    
    """
    #Creamos carpetas recursivas usando la funcion makedirs del modulo os
    import os

    os.makedirs("data_lake/landing", exist_ok=True)
    os.makedirs('data_lake/raw', exist_ok=True)
    os.makedirs('data_lake/cleansed', exist_ok=True)
    os.makedirs('data_lake/business/reports/figures', exist_ok=True)
    os.makedirs('data_lake/business/features', exist_ok=True)
    os.makedirs('data_lake/business/forecasts', exist_ok=True)
    
    #return

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

#----------llamado de funcion-------------
create_data_lake()
