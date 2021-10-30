import dataset
import helpers

def number_of_languages_in_dataset():
    langs = []

    for file in dataset.files:
        df = helpers.load_dataset(file)
        print(file)
        for index, row in df.iterrows():
            if row['tweet_language'] not in langs:
                langs.append(row['tweet_language'])

        print(str(len(langs)))
    
    print('Total languages in all dataset files ' + str(len(langs)))
    store_result(str(len(langs)))
    
def store_result(total):
    helpers.path_checker(dataset.output_data_store)
    output_file = 'total_languages_in_all_datasets.csv'

    helpers.data_to_file_two_values(
        [
            [
                'total languages', 
                str(total)
            ]
        ],
        dataset.output_data_store + '/' + output_file
    )


number_of_languages_in_dataset()