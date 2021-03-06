# -*- coding: utf-8 -*-
"""Metrics_Comparison.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VMjDrKZ8cGB7jWpci2OR2Z3MMT0rDduj
"""

metrics_att = [34.33,38.39,4.787]

metrics_transformer = [59.68,39.69,5.05]

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

"""# Displaying BLEU"""

avg_bleu = {}

avg_bleu['attention'] = metrics_att[0]

avg_bleu['transformer'] = metrics_transformer[0]

avg_bleu

plt.ylim(0, 100)
plt.bar(avg_bleu.keys(),avg_bleu.values(),color=['red','green','blue'])
plt.xlabel("Models")
plt.ylabel("Metrics")

"""# Displaying GLEU"""

avg_gleu = {}

avg_gleu['attention'] = metrics_att[1]

avg_gleu['transformer'] = metrics_transformer[1]

avg_gleu

plt.ylim(0, 100)
plt.bar(avg_gleu.keys(),avg_gleu.values(),color=[ 'red', 'green', 'blue'])
plt.xlabel("Models")
plt.ylabel("Metrics")

"""# Displaying WER"""

avg_wer = {}

avg_wer['attention'] = metrics_att[2]

avg_wer['transformer'] = metrics_transformer[2]

avg_wer

plt.ylim(0, 10)
plt.bar(avg_wer.keys(),avg_wer.values(),color=[ 'red', 'green', 'blue'])
plt.xlabel("Models")
plt.ylabel("Metrics")

