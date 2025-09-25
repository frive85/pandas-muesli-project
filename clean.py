def clean_cols(df):
    """standardize column names of a given df
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df

def clean_data(orders, campaign, process, intern):
    """Cleans our 4 Dataframes from the Sales in terms of:
    - Standardizing Column Names
    - Drop Duplicates depending on order_id in every DF
    - Crate year,month,day,weekday for every date_columns
    """
    # standardize column names
    orders = clean_cols(orders)
    campaign = clean_cols(campaign)
    process = clean_cols(process)
    intern = clean_cols(intern)

    # drop duplicates by order_id 
    orders.drop_duplicates(subset='order_id', keep='first', inplace=True)
    process.drop_duplicates(subset='order_id', keep='first', inplace=True)
    intern.drop_duplicates(subset='order_id', keep='first', inplace=True)
    campaign.drop_duplicates(subset='order_id', keep='first', inplace=True)

    for df in [orders, campaign, process, intern]:
        for i in df.columns:
            if 'date' in i:
                df[f"{i}_year"]=df[i].dt.year
                df[f"{i}_month"]=df[i].dt.month
                df[f"{i}_weekday"]=df[i].dt.dayofweek
                df[f"{i}_day"]=df[i].dt.day

    return orders, campaign, process, intern
    