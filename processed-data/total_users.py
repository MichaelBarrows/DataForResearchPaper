import helpers
import dataset
import pandas

def import_dataset(ds):
    return helpers.load_dataset(ds)

def process():
    store = {}
    counter = 0

    df = import_dataset(dataset.swn_labelled_dataset)
    for index, row in df.iterrows():
        counter += 1
        if row.userid in store:
            store[row.userid] += 1
        else:
            store[row.userid] = 1 
            print('new user ' + str(len(store)))
            
    print("Complete - " + dataset.swn_labelled_dataset)
    print(str(len(store)))
    print('Number of tweets: ' + str(counter))
    return store


data = process()

print('Total Users Across All Files: ' + str(len(data)))
