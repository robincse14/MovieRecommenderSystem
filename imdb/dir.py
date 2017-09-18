

Movieid_Directorid={}
Directorid_Director={}
temp={}
with open('movie_directors.dat') as obj:
	i=0
	for line in obj:
		a,b,c=line.split("\t")
	
	
		if(a=="movieID"):
			continue
		if b not in Directorid_Director:
			Directorid_Director[b]=i
			temp[i]=b
			i=i+10
		Movieid_Directorid[a]=Directorid_Director[b]

print(temp)
print("######")
print(Movieid_Directorid)
