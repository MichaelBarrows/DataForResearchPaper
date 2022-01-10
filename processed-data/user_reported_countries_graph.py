import helpers
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

df = helpers.load_dataset("output_data/user_reported_location_volumes.csv")

x, y = [], []
for index, row in df.iterrows():
    x.append(row.location)
    y.append(row.users)

seaborn.set(rc={'figure.figsize':(10, 7.5)})

import numpy as np
plt.ylabel("Volume")
plt.xlabel("User Reported Country")
plt.title("User Volume by Location\n")
plt.style.use('fivethirtyeight')
plt.subplots_adjust(bottom=0.35)
splt = seaborn.barplot(x=x, y=y, palette=['#1f77b4'])
splt.set_xticklabels(splt.get_xticklabels(),rotation = 90)
fig = splt.get_figure()
fig.savefig("output_data/volume_by_user_reported_country.png")
