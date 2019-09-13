
"""

Get data from yahoo finance

"""

import json
import pandas as pd
import yfinance as yf

def get_stock():
    """
    AAPL est le stock ticket (id du cours de bourse)
    On le télécharge pour les jours entre les les 2 dates spécifiées
    On s'intéresse au prix à la fermeture journalière des marchés (Close)
    """
    # data = yf.download('AAPL','2016-01-01','2019-01-01').Close
    # print("type de donnees",data.index)
    # dict_ = yf.download('AAPL','2016-01-01','2019-01-01').to_dict()



# ce que je viens d'ajouter pour tester 
    # with open("feature.json") as json_data:
    #     data_dict = json.load(json_data)

    # data=pd.DataFrame.from_dict(data_dict, orient='columns')
    # print("index",data.index)
    # print(data.values[10])
    # *****************Traitement des objets pandas***********************
    with open("factures.json") as json_data:
        data_dict = json.load(json_data)

        dataframe=pd.DataFrame.from_dict(data_dict, orient='columns')
        print(dataframe)
        dict_client = dict()



        for i in range(len(dataframe)):
        # print(dataframe.client[0].get('name'))

            if (dataframe.client[i].get('name') in dict_client):
                # print(dataframe.client[i].get('name'),"=>",dataframe.shipping[i])
                
                dict_client[dataframe.client[i].get('name')] += dataframe.shipping[i]
            else:
                dict_client[dataframe.client[i].get('name')] = dataframe.shipping[i]
                # print(dataframe.client[i].get('name'),"=>",dataframe.shipping[i])
        data=pd.DataFrame.from_dict(dict_client, orient='index')
 

    return data
"""

Matplotlib

"""

## Trickshots pour Mac :
import matplotlib
matplotlib.use('Agg')

from matplotlib import pylab
from pylab import *
from io import BytesIO
import PIL, PIL.Image


def get_graph_data():
    """
    This function generates the data for a certain graph.
    We can display this graph in a template by passing the data using an HttpResponse.
    """
    # Data is a pandas.Series object (x = index, values = y)
    data = get_stock()
    # x
    x = data.index
    # y
    # y = data.values
    y = data.values
    # Display Plot
    plt.figure(figsize=(20,10))
    plot(x, y, linewidth=1.0)
    # Display X label
    xlabel('Users')
    # Display Y label
    ylabel('Total dépenses ($)')
    # Display Title
    title('nombre de facture par moi, !')
    # Display grid
    grid(True)

    # Store image in a bytes buffer
    buffer = BytesIO()
    # Create a canvas object
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    # Create a PIL.Image object
    pilImage = PIL.Image.frombytes("RGB", # "RGB" for colors
                                 canvas.get_width_height(), # canvas.get_width_height() for size
                                 canvas.tostring_rgb()) # canvas.tostring_rgb() for data
    # Save as PNG
    pilImage.save(buffer, "PNG")
    # Close pylab
    pylab.close()
    return(buffer.getvalue())



"""

MongoDB

"""


import pymongo

# On définit le client comme étant le client local
client = pymongo.MongoClient()
