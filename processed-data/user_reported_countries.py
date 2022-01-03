import helpers
import dataset
import pandas

def count_unique_values(df):
    counter = {}
    processed_users = []
    mapper = {}
    mapper['nan'] = "Missing"
    for index, row in df.iterrows():
        if row.userid not in processed_users:
            processed_users.append(row.userid)
            location = str(row.user_reported_location).lower()

            if location not in mapper:
                response = input(location + " : ")
                mapper[location] = response
            else:
                response = mapper[location]
                
            if response not in counter:
                counter[response] = 1
            else:
                counter[response] += 1

    counter = helpers.sort_dict(counter)
    data = []
    for row in counter:
        data.append([row, counter[row]])
    
    new_df = pandas.DataFrame(data, columns=['location', 'users'])
    helpers.dataframe_to_csv(new_df, 'output_data/user_reported_location_volumes.csv')

def import_dataset():
    df = helpers.load_dataset(dataset.filtered_dataset)
    return df

count_unique_values(import_dataset())