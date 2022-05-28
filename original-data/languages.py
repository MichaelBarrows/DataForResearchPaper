import helpers
import dataset
import numpy
import pandas as pd
import language_code_mapper

def get_language_counts():
    langs = {}
    total = 0
    for ds in dataset.files:
        print(ds)
        df = helpers.load_dataset(dataset.dataset + ds)
        for index, row in df.iterrows():
            total += 1
            if row['tweet_language'] not in langs:
                langs[row['tweet_language']] = 1
            else:
                langs[row['tweet_language']] += 1

    langs = helpers.sort_dict(langs)
    data = list(langs.items())
    langs_array = numpy.array(data)

    new_langs = []
    for lang in langs_array:
        if lang[0] in language_code_mapper.iso:
            new_langs.append([language_code_mapper.iso[lang[0]] + " (" + lang[0] + ")", lang[1], round((int(lang[1]) / total) * 100, 2)])
        else:
            new_langs.append([lang[0], lang[1], round((int(lang[1]) / total) * 100, 2)])

    new_langs = pd.DataFrame(new_langs, columns=['language', 'volume', 'percentage'])
    print(new_langs)

    helpers.dataframe_to_csv(new_langs, dataset.output_data_store + '/language_counts.csv')

get_language_counts()