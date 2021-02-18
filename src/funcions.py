def cleaning_data(x):
    
    # Eliminar columnas no relevantes para el análisis.
    
    x.drop(['fee', 'year', 'club_involved_name', 'year'], axis = 1 )
    # Contar valores nulos.

    x.isnull().sum().sort_values(ascending=False)
    
    # Elimininar valores nulos.
    
    x.dropna()
    
    # Eliminar valore duplicados.
    
    x.drop_duplicates()
    
    # Mostrar distritos correctamente.
