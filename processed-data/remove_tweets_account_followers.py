import helpers
import dataset

def remove_accounts_with_less_than_5000_followers():
    accounts = []
    tweet_count = 0

    df = helpers.load_dataset(dataset.filtered_dataset)
    new_df = df.loc[df['follower_count'] >= 5000]

    helpers.dataframe_to_csv(new_df, dataset.output_data_store + '/follower-filtered-dataset.csv')

remove_accounts_with_less_than_5000_followers()