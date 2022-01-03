import helpers
import dataset
import pandas

def import_dataset():
    return helpers.load_dataset('output_data/location_labelled_filtered_dataset.csv')

def process(df):
    store = {}
    for index, row in df.iterrows():
        if row.userid in store:
            store[row.userid]['count'] += 1
        else:
            data = {}
            data['count'] = 1
            data['location'] = row.location
            data['name'] = (row.user_display_name, "--- # ---")[row.follower_count < 5000]
            data['hashed'] = row.follower_count < 5000
            data['follower_count'] = row.follower_count
            store[row.userid] = data 

    return store

def process_data(data):
    data_list = []
    for row in data:
        data_list.append([
            row, data[row]['count'], 
            data[row]['location'], 
            data[row]['name'], 
            data[row]['follower_count'], 
            data[row]['hashed'],
        ])
    new_df = pandas.DataFrame(data_list, columns=[
        'userid', 
        'tweet_volume', 
        'location', 
        'display_name', 
        'follower_count', 
        'should_be_hashed',
    ])

    return new_df.sort_values(by=['tweet_volume'], ascending=False)

df = import_dataset()
data = process(df)
processed_data = process_data(data)
helpers.dataframe_to_csv(processed_data, 'output_data/most_active_users.csv')