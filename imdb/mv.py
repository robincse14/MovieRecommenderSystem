#! /usr/bin/python

Movieid_Countryid={}
CountryId_Country={}
temp={}
with open('movie_countries.dat') as obj:
	i=0
	for line in obj:
		a,b=line.split("\t")
		b=b[:-1]
	
		if(a=="movieID"):
			continue
		if b not in CountryId_Country:
			CountryId_Country[b]=i
			temp[i]=b
			i=i+10
		Movieid_Countryid[a]=CountryId_Country[b]

print(temp)
print("######")
print(CountryId_Country)
print("######")
print(Movieid_Countryid)
