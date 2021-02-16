def clean_data(x):
    #remove null values
    x.dropna()
    #remove duplicates
    x.drop_duplicates()
    #remove columns
    x.drop(['club_involved_name', 'fee', 'league_name', 'season'], axis = 1 )
    
    return x


   

