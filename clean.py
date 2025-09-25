def clean_cols(df):
    """Strips whitespace, converts to lowercase, and replaces spaces with underscores."""
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df

def clean_data(orders, campaign, process, intern):
    orders = clean_cols(orders)
    campaign = clean_cols(campaign)
    process = clean_cols(process)
    intern = clean_cols(intern)

# Handle Duplicates: The raw data may have multiple rows per order (e.g., for each product).
# For our process analysis, we only need one unique entry per order.
    orders.drop_duplicates(subset='order_id', keep='first', inplace=True)
    process.drop_duplicates(subset='order_id', keep='first', inplace=True)
    intern.drop_duplicates(subset='order_id', keep='first', inplace=True)
    campaign.drop_duplicates(subset='order_id', keep='first', inplace=True)

    return orders, campaign, process, intern
    