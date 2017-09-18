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
		if b not Actor_ActorId:
			Actor_Actorid[b]=i
			ActorId_Actor[i]=b
			flag=1
		if a not in Movieid_Actorid:
			Movieid_Actorid[a]=()

		Movieid_Actorid[a]=Movieid_Actorid[a]+(Actor_ActorId[b],)
		#print(a)
		#print(i)
		if(flag):
                        
			i=i+10

print(Actor_ActorId)
print("######")
print(ActorId_Actor)
print("######")
print(Movieid_Actorid)
