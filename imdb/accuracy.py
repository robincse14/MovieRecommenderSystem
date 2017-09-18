from sklearn import tree
clf = tree.DecisionTreeClassifier()

from XY import *

clf=clf.fit(X,Y)

#accuracy
ans = 0.0
for i in range(len(P1)):
    ele=clf.predict([P1[i]])[0]
    ans = ans+ abs(ele-P2[i])
print(ans/len(P1))
