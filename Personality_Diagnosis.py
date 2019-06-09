
from dataset_movielens import dataset
from math import *
from dataset_movielens_movienames import dataset_movie_name
from operator import itemgetter



Sigma={} #Standard deviation of each user
MatchDict={} # matching of user with other user (P(Ra true=Ri))



#Creating Training and Test Data
TrainData={}
TestData={}


for user in dataset:    
    l=len(dataset[user])
    i=0
    TrainData[user]={}
    TestData[user]={}
    for movie in dataset[user]:
        i=i+1
        if(i<3*floor(l/4)):
            TrainData[user][movie]=dataset[user][movie]
        else:
            TestData[user][movie]=dataset[user][movie]




#helper function to calculate standard deviation

def StdDev(i):
    L=[]
    for movie in TrainData[i]:
        L.append(TrainData[i][movie])
    mean=sum(L)/len(TrainData[i])

    #print(mean)
    
    n=len(TrainData[i])
    
    Sigma_Sqr=(sum([pow(j-mean,2) for j in L]))/n
    
    deviation=sqrt(Sigma_Sqr)

    return deviation

#updating values of standard deviation for each user

for user in TrainData:
    Sigma[user]=StdDev(user)


#guassion function  
def gaussian(x,y):
    return pow(x-y,2)



#matching function returns the dissimilarity between active user and ith user
def matching(active,i):
    sigma=Sigma[i]
    ans=0.0
    
    for movie in TrainData[i]:
        if movie in TrainData[active]:
            ans+=gaussian(TrainData[i][movie],TrainData[active][movie])
    ans/=2*pow(sigma,2)

    return ans

#storing the results of Matching between active and all other users

def MatchDictionary(active):
    MatchDict.clear()
    for user in TrainData:
        MatchDict[user]=matching(active,user)




#predict the most probable rating for active user and movie {movie}
        
def predict(active,movie):
    L=[0]*10

    predicted_rating=0.0
    prob=0.0
    
    for i in range(0,10):
        r=(i+1)/2.0
        ans=0.0
        for user in TrainData:
            temp=0.0
            
            if movie in TrainData[user]:
                temp+=gaussian(r,TrainData[user][movie])
                temp/=2*pow(Sigma[user],2)
                temp+=MatchDict[user]
                ans+=pow(e,-temp)
        L[i]=ans
        
        if ans>prob:
            prob=ans
            predicted_rating=r
            
    return predicted_rating


#recommend the most rated items to users

def recommend(user):
    MatchDictionary(user)
    L=[]
    for movie in dataset_movie_name:
        
        if movie in TrainData[user]:
            continue
        L.append((movie,predict(user,movie)))
    
    L=sorted(L,key=itemgetter(1))

    L.reverse()
    ans=[]
    for i in range(0,10):
        ans.append(list(dataset_movie_name[L[i][0]])[0][1:])
    
    return ans


#Error analysis

error=0
LL=0
for user in dataset:
    print(user)
    MatchDictionary(user)
    LL=LL+len(TestData[user])
    for movie in TestData[user]:
        PR=predict(user,movie)
        r=dataset[user][movie]
        #print(movie+" "+ str(PR))
        print(PR-r)
        error=error+pow(r-PR,2)
print(sqrt(error/LL))



print(recommend('75'))




    
        
        
        
        


