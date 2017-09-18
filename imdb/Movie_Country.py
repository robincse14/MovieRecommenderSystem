Movieid_Countryid={}
CountryId_Country={}

with open('movie_countries.dat') as obj:
    i=1
    for line in obj:
        a,b=line.split("\t")
        b=b[:-1]
        
        if(a=="movieID"):
            continue
        if b not in CountryId_Country:
            CountryId_Country[b]=i
            i=i+1
        Movieid_Countryid[a]=CountryId_Country[b]
        
print(CountryId_Country)
print("####")
print(Movieid_Countryid)


