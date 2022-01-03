import helpers
import dataset
import pandas

def count_unique_values(df):
    counter = {}
    processed_users = []
    for index, row in df.iterrows():
        if row.userid not in processed_users:
            processed_users.append(row.userid)
            location = row.location

            if location not in counter:
                counter[location] = 1
            else:
                counter[location] += 1
            
    counter = helpers.sort_dict(counter)
    data = []
    for row in counter:
        data.append([row, counter[row]])
    
    new_df = pandas.DataFrame(data, columns=['location', 'users'])
    helpers.dataframe_to_csv(new_df, 'output_data/user_reported_location_volumes.csv')

def normalise_labels(df):
    df['location'] = ""
    mapper = {}
    mapper['nan'] = "Missing"
    for index, row in df.iterrows():
        location = str(row.user_reported_location).lower()

        if location not in mapper:
            response = input(location + " : ")
            mapper[location] = response
        else:
            response = mapper[location]
            
        df.location.at[index] = response

    helpers.dataframe_to_csv(df, 'output_data/location_labelled_filtered_dataset.csv')
    return df
    

def import_dataset():
    df = helpers.load_dataset(dataset.filtered_dataset)
    return df

df = import_dataset()
df = normalise_labels(df)
count_unique_values(df)