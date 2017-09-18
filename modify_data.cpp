#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    ifstream IF;
     ofstream OF;
     IF.open("input.txt");
     OF.open("dataset_movielens_items.py");
     int cur,prev,mov,i;
     long long int tmp;
     float rating=-1;
     prev=-1;
     OF<<"dataset={";
    // OF<<"\t\t"<<cur<<" :{ ";
     i=0;
     while(i<855599)
     {
        IF>>cur>>mov>>rating;
        //OF<<" "<<mov<<" "<<rating;
        if(i==0)
           OF<<"\t\t\'"<<cur<<"\' :{ ";
        if(i>0)

             {OF<<"\'"<<mov<<"\': "<<rating;}
         if(cur==prev)
         {
             OF<<",\n\t\t\t\t";

         }
         else if(i>0)
         {
             OF<<"},\n\t\t\'"<<cur<<"\' :{ ";
         }

       // IF>>mov>>rating>>tmp;
       // IF>>mov>>rating>>tmp;
        prev=cur;
        i++;
     }

            OF<<"}\n};";


     return 0;
}
