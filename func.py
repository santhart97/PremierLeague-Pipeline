def cleaning_data(data):
    
    # Eliminar columnas no relevantes para el análisis.
    
    data = data.drop(['fee', 'year', 'club_involved_name', 'year'], axis = 1 )
    # Contar valores nulos.

    data.isnull().sum().sort_values(ascending=False)
    
    # Elimininar valores nulos.
    
    data.dropna()
    
    # Eliminar valore duplicados.
    
    data.drop_duplicates()
    
    # Mostrar distritos correctamente.
