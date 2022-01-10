
import pandas as pd
import numpy as np
#import data from file
mydata=pd.read_csv("Chilla_data2_for_plots.CSV")
print(mydata)
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks",color_codes=True)
mydata=sns.countplot(x="Gender",hue="Age", data=mydata)
plt.show()

