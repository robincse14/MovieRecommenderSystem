#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    ifstream IF;
     ofstream OF;
     IF.open("input.txt");
     OF.open("dataset_movielens_movienames.py");
     int i,j;
     long long int tmp;
     float rating=-1;
     int s;
     string ss;

     OF<<"dataset_movie_name={";
    // OF<<"\t\t"<<cur<<" :{ ";
     i=0;
     while(i<10198)
     {
        IF>>s;
        getline(IF,ss);
        j=0;

        OF<<"\'"<<s<<"\':{\'"<<ss<<"\'},\n";
        i++;
     }

            OF<<"}\n};";


     return 0;
}

