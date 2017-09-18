Movieid_Actorid={}
Actor_ActorId={}
ActorId_Actor={}
with open('movie_actors.dat') as obj:
    i=0
    for line in obj:
        a,b,c,d=line.split("\t")
        
        if(a=="movieID"):
            continue
        flag=0
        
        if b not in Actor_ActorId:
            Actor_ActorId[b]=i
            ActorId_Actor[i]=b
            flag=1
        if a not in Movieid_Actorid:
            Movieid_Actorid[a]=()
        Movieid_Actorid[a]=Movieid_Actorid[a]+(Actor_ActorId[b],)

        if(flag):
            i=i+10
        

print(len(Actor_ActorId))
print("######")
print(len(ActorId_Actor))
print("######")
print(len(Movieid_Actorid))
