import helpers
import dataset
import pandas

def import_dataset(ds):
    return helpers.load_dataset(ds)

def process():
    store = {}

    for ds in dataset.files:
        print(ds)
        df = ''
        df = import_dataset(dataset.dataset + ds)
        for index, row in df.iterrows():
            if row.userid in store:
                store[row.userid] += 1
            else:
                store[row.userid] = 1 
                print('new user ' + str(len(store)))
                
        print("Complete - " + ds)
        print(str(len(store)))
    return store


data = process()

print('Total Users Across All Files: ' + str(len(data)))
