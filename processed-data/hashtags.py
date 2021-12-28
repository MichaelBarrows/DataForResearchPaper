import helpers
import dataset
import more_itertools

def get_ten_most_popular_hashtags():
    df = helpers.load_dataset(dataset.filtered_dataset)
    hashtags = {}
    counter = 0
    for index, row in df.iterrows():
        if (isinstance(row['hashtags'], str)):
            tweet_hashtags = row['hashtags'].replace('[', '')
            tweet_hashtags = tweet_hashtags.replace(']', '')
            tweet_hashtags = tweet_hashtags.replace("'", '')
            tweet_hashtags = tweet_hashtags.split(', ')
            for hashtag in tweet_hashtags:
                counter += 1
                if (hashtag == ''):
                    continue
                hashtag = hashtag.lower()
                if (hashtag in hashtags):
                    hashtags[hashtag] += 1
                else:
                    hashtags[hashtag] = 1

    hashtags = helpers.sort_dict(hashtags)
    first_ten = more_itertools.take(10, hashtags.items())
    
    first_ten.append(['total hashtags', counter])
    helpers.data_to_file_two_values(first_ten, dataset.output_data_store + '/10_most_frequent_hashtags.csv')

get_ten_most_popular_hashtags()