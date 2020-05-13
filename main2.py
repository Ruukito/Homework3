
import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')

Voter= []
Country = []
Candidate = []
Khan = 0
Correy = 0
Li = 0
Tooley = 0

with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter =",")
    next(csvreader,None)
    for row in csvreader:
        Voter.append(row[0])
        Candidate.append(row[2])

        if row[2] == "Khan":
            Khan  = Khan + 1
        if row[2] == "Correy":
            Correy  = Correy + 1
        if row[2] == "Li":
            Li  = Li + 1
        if row[2] == "O'Tooley":
            Tooley  = Tooley + 1
        

if Correy > Khan > Li > Tooley:
    Winner = "Correy"
if Khan > Correy > Li > Tooley:
    Winner = "Khan"
if Li > Correy > Li > Tooley:
    Winner = "Li"
if Tooley> Correy > Li > Tooley:
    Winner = "Tooley"  
Khan_percentage= Khan/len(Voter)
Correy_percentage= Correy/len(Voter)
Li_percentage = Li/len(Voter)
Tooley_percentage = Tooley/len(Voter)

Khan_percentage_f = "{0:.3f}%".format(Khan_percentage*100)
Correy_percentage_f = "{0:.3f}%".format(Correy_percentage*100)
Li_percentage_f = "{0:.3f}%".format(Li_percentage*100)
Tooley_percentage_f = "{0:.3f}%".format(Tooley_percentage*100)



print("Election results")
print("-------------------------")
print(f"Total Votes: {len(Voter)}")
print("-------------------------")
print(f"Khan: {(Khan_percentage_f)}  ({(Khan)})" )
print(f"Khan: {(Correy_percentage_f)}  ({(Correy)})" )
print(f"Khan: {(Li_percentage_f)}  ({(Li)})" )
print(f"Khan: {(Tooley_percentage_f)}  ({(Tooley)})" )
print("-------------------------")
print(f"Winner: {(Winner)}")
print("-------------------------")



A=["Election Results:", "Total Votes:", "Khan:","Correy:","Li:","O'Tooley:","Winner:"]
B=["",len(Voter),Khan_percentage_f,Correy_percentage_f, Li_percentage_f,Tooley_percentage_f,Winner]
C=["","",Khan,Correy,Li,Tooley,""]

Final_list =zip(A,B,C)
outputfile="main3.csv"
with open(outputfile,"w") as datafile:
    writer=csv.writer(datafile)
    writer.writerows(Final_list)