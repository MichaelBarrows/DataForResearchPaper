import helpers
import dataset

df = helpers.load_dataset(dataset.output_data_store + '/sentiwordnet-labelled-follower-filtered.csv')

pos_df = df.loc[df['sentiment_class'] == 'Positive']
neg_df = df.loc[df['sentiment_class'] == 'Negative']
neu_df = df.loc[df['sentiment_class'] == 'Neutral']

helpers.dataframe_to_csv(pos_df, dataset.output_data_store + '/pos-filtered.csv')
helpers.dataframe_to_csv(neg_df, dataset.output_data_store + '/neg-filtered.csv')
helpers.dataframe_to_csv(neu_df, dataset.output_data_store + '/neu-filtered.csv')