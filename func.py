def clean_dataset(x):
    # Removes null values.
    x.isnull().sum().sort_values(ascending=False)
    
    # Eliminates duplicate values
    x.drop_duplicates()

    return x
   

