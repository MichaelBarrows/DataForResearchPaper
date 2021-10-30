import dataset
import helpers

def number_of_accounts_in_dataset():
    accounts = []

    for file in dataset.files:
        df = helpers.load_dataset(file)
        print(file)
        for index, row in df.iterrows():
            if row['userid'] not in accounts:
                accounts.append(row['userid'])
        print(str(len(accounts)))
        
    
    print('Total accounts in all dataset files ' + str(len(accounts)))
    store_result(str(len(accounts)))
    
def store_result(total):
    helpers.path_checker(dataset.output_data)
    output_file = 'total_unique_accounts_in_all_datasets.csv'

    helpers.data_to_file_two_values(
        [
            [
                'total unique user ids', 
                str(total)
            ]
        ],
        '',
        dataset.output_data + '/' + output_file
    )


number_of_accounts_in_dataset()