from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer

import pandas as pd
import matplotlib.pyplot as plt
import os



df = pd.read_csv('boletines1.csv', error_bad_lines=False)
df.head()

col = ['Supervision', 'Texto']
df = df[col]
df = df[pd.notnull(df['Texto'])]
df.columns = ['Supervision', 'Texto']

df['text_id'] = df['Supervision'].factorize()[0]
text_id_df = df[['Supervision', 'text_id']].drop_duplicates().sort_values('text_id')
text_to_id = dict(text_id_df.values)
id_to_text = dict(text_id_df[['text_id', 'Supervision']].values)
df.head()

# fig = plt.figure(figsize=(8, 6))
# df.groupby('Supervision').Texto.count().plot.bar(ylim=0)
# plt.show()

X_train, X_test, y_train, y_test = train_test_split(df['Texto'], df['Supervision'], random_state = 0)
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

clf = LinearSVC().fit(X_train_tfidf, y_train)

print(clf.predict(count_vect.transform(["1 diciembre 2016 boletín oficial de la provincia de huesca nº 230 administración del estado ministerios ministerio de fomento dirección general de carreteras demarcación de carreteras del estado en aragón anuncio 5143 unidad de carreteras huesca por el servicio de obras públicas y patrimonio de la diputación provincial de huesca, con domicilio en porches de galicia, 4, 22071 - huesca, se ha solicitado de la dirección general de carreteras autorización para el acondicionamiento de enlace de acceso a allué en la carretera n-260, p.k. 483,500 (huesca), según el proyecto técnico presentado, de fecha noviembre de 2016, suscrito por d. david sarasa alcubierre, ingeniero de caminos, canales y puertos, colegiado nº 23.952. en cumplimiento del artículo 104.5 del r.d. 1812/1994,  artículos 18 y 19.1 de la ley de expropiación forzosa, de 16 de diciembre de 1954, y concordantes de su reglamento (decreto de 26 de abril de 1957), esta demarcación de carreteras del estado"])))
