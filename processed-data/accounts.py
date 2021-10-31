import dataset
import helpers

def number_of_accounts_in_dataset():
    accounts = []

    df = helpers.load_dataset(dataset.filtered_dataset)
    for index, row in df.iterrows():
        if row['userid'] not in accounts:
            accounts.append(row['userid'])
    print('accounts ' + str(len(accounts)))
    print('tweets ' + str(len(df)))

    helpers.data_to_file_two_values(
        [
            [
                'total accounts',
                str(len(accounts))
            ],
            [
                'total tweets',
                str(len(df))
            ]
        ],
        dataset.output_data_store + '/total_unique_accounts_in_filtered_dataset.csv'
    )

def number_of_accounts_with_more_than_five_thousand_followers():
    accounts = []

    df = helpers.load_dataset(dataset.filtered_dataset)
    df = df.loc[df['follower_count'] > 5000]
    for index, row in df.iterrows():
        if row['userid'] not in accounts:
            accounts.append(row['userid'])
        
    print('accounts ' + str(len(accounts)))
    print('tweets ' + str(len(df)))
    
    helpers.data_to_file_two_values(
        [
            [
                'total accounts filtered',
                str(len(accounts))
            ],
            [
                'total tweets filtered',
                str(len(df))
            ]
        ],
        dataset.output_data_store + '/total_unique_accounts_in_filtered_dataset_more_than_5000_followers.csv'
    )


number_of_accounts_in_dataset()
number_of_accounts_with_more_than_five_thousand_followers()
