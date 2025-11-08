from sklearn.neighbors import KNeighborsClassifier

x1=[7,7,3,1]
x2=[7,4,4,4]
target=['bad','bad','good','good']

features=zip(x1,x2)

features=list(features)
print(features)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(features,target)
print(knn.predict([[3,6]]))

print(type(list))


