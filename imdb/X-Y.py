from dataset_movielens import dataset

user=dataset['75']
from try1 import Movieid_Countryid

from try2 import Movieid_Directorid

from try3 import Movieid_Genreid

X=[]
Y=[]

for movie in user:
    c=Movieid_Countryid[movie]
    d=Movieid_Directorid[movie]
    for genre in Movieid_Genreid[movie]:
        L=[c,d,genre]
        X.append(L)
        Y.append(dataset['75'][movie])
print(len(X))
print(len(Y))


