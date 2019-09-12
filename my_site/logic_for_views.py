
"""

Get data from yahoo finance

"""


import yfinance as yf

def get_apple_stock():
    """
    AAPL est le stock ticket (id du cours de bourse)
    On le télécharge pour les jours entre les les 2 dates spécifiées
    On s'intéresse au prix à la fermeture journalière des marchés (Close)
    """
    data = yf.download('AAPL','2016-01-01','2018-01-01').Close
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
    data = get_apple_stock()
    # x
    x = data.index
    # y
    y = data.values
    # Display Plot
    plt.figure(figsize=(20,10))
    plot(x, y, linewidth=1.0)
    # Display X label
    xlabel('Date')
    # Display Y label
    ylabel('Apple stock (closing price)')
    # Display Title
    title('Apple seems to be very well those days !')
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
# Le nom de la DB est "questions" (si elle n'existe pas elle est créée)
db = client["question"]
# Le nom de la collection est "from_app" (si elle n'existe pas elle est créée)
# On affiche le nombre d'objets dans la DB dans la console lors du démarrage de l'appelle
print("{} questions in the DB".format(db["from_app"].count_documents({})))


def store_question(question_text, question_int, db, collection):
    """
    Cette fonction crée et stocke un document contenant question_int et question_text.
    Elle est stockée dans db[collection].
    """
    document = {'question': question_text,
                'question_int': question_int }
    db[collection].insert_one(document)
    return None
