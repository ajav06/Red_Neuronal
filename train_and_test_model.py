from sklearn.feature_extraction.text import (CountVectorizer,
                                             TfidfTransformer,
                                             TfidfVectorizer)
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

import matplotlib.pyplot as plt
import pandas as pd
import pickle
import sys

def read_doc(path): # El parametro es la ruta donde se encuentra almacenado el documento, seguido del nombre del mismo
    """ Lee el documento .csv de entramiento """
    document = pd.read_csv(path, error_bad_lines=False)
    document.head()

    columns = ['Supervision','Texto', 'ID']
    document = document[columns]
    document = document[pd.notnull(document['Texto'])]
    document.columns = ['Supervision', 'Texto', 'ID']

    return document


def train_model(document):  # El parametro es el documento leido anteriormento
    """ Entrena la red neuronal con un modelo matemático: 
        LinearSVC para la clasicación """
    X_train, X_test, y_train, y_test = train_test_split(document['Texto'], 
            document['Supervision'], random_state=0)

    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(X_train)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

    model = LinearSVC()
    model.fit(X_train_tfidf, y_train)

    return model, count_vect

def test_model(paragraph, model): # Los parametros son: el párrafo de prueba y el modelo entrenado
    """ Prueba la red neuronal con párrafo de prueba,
        la cual, debe detectar que tipo de párrafo es """
    count_vect = model[1]
    prediction = model[0].predict(count_vect.transform([paragraph]))
    type_prediction = ''

    if prediction == 1:
        type_prediction = 'Correcto'
    elif prediction == 2:
        type_prediction = 'Incorrecto'
    elif prediction == 3:
        type_prediction = 'Dudoso'

    return type_prediction

def save_model(paths, model): # Los parametros son: la ruta donde va almacenar y el modelo a almacenar
    """ Almacena en el disco los modelos de 
        entramiento de la red nueronal """
    filename_model = paths + 'finalized_model.sav'
    filename_count_vect = paths + 'finalized_count_vect.sav'

    try:
        pickle.dump(model[0], open(filename_model, 'wb'))
        pickle.dump(model[1], open(filename_count_vect, 'wb'))
        print("Datos guardados con éxito...")
    except:
        print("Error inesperado: ", sys.exc_info()[0])


def load_model(paths): # El parametro es la ruta donde esta almacenado el modelo de respaldo
    """ Recupera los modelos de entramiento de la 
        red nueronal, almacenados en el disco"""
    filename_model = paths + 'finalized_model.sav'
    filename_count_vect = paths + 'finalized_count_vect.sav'

    try:
        model = pickle.load(open(filename_model, 'rb'))
        count_vect = pickle.load(open(filename_count_vect, 'rb'))
        print("Datos cargados con éxito...")
        return model, count_vect
    except:
        print("Error inesperado: ", sys.exc_info()[0])


# Para Entrenar
# document = read_doc('boletines/boletines1.csv')
# model = train_model(document)

# Para Guardar
# save_model('backup/')

# Para Cargar los datos
if __name__ == "__main__":
    model = load_model('backup/')
    paragraph = "diari oficial de la generalitat de catalunya núm. 7316 - 24.2.2017 cve-dogc-b-17048101-2017 anuncios de la generalidad de cataluña otros entes infraestructures de la generalitat de catalunya, sau anuncio sobre la formalización de un contrato de servicios (ta-nb-01134.f1). 1.- se hace público, para conocimiento general, que infraestructures de la generalitat de catalunya, sau, sau, empresa pública de la generalitat de catalunya, ha formalizado el contrato que a continuación se detalla. perfil del contratante: http://www.infraestructures.gencat.cat. 2.- objeto del contrato: a) tipo: servicios. b) descripción: contrato de servicios para la asistencia técnica para la redacción del proyecto de trazado de mejora general. nueva carretera. eix del llobregat. implantación de un tercer carril reversible en la carretera c-16, del pk 96+500 al 117+300. tramo: berga – bagà. clave: ta-nb-01134.f1. d) cpv: 71311000-1. g) medio de publicación anuncio de lici"
    prediction = test_model(paragraph, model)
    print(prediction)