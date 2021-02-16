def clean_dataset(x):
    # Removes null values.
    x.isnull().sum().sort_values(ascending=False)
    
    # Eliminates duplicate values
    x.drop_duplicates()
    
    x.drop(['club_involved_name', 'year', 'fee'] axis = 1 )

    return x
   

