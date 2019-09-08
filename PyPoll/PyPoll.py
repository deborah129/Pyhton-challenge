
import csv



csvpoll = ("election_data.csv")
total_votes = 0
candidate_list = set()
candidate_name = 0
candidate_vote_count = {}
per = []
with open (csvpoll, newline = '')as csvpoll_file:
    csvpoll_reader = csv.reader(csvpoll_file, delimiter = ',')

    next(csvpoll_reader, None)

#The total number of votes cast
    for row in csvpoll_reader:

        total_votes += 1


#A complete list of candidates who received votes
        candidate_list.add(row[2])
        if  row[2] in candidate_vote_count:
            candidate_vote_count[row[2]] += 1
        else:
            candidate_vote_count[row[2]] = 1

        # print(candidate_vote_count[row[2]])
        #print(name)
#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.

#As an example, your analysis should look similar to the one below:
    string_list =[]
    #print("Election Results: ")
    string_list.append("Election Results:")
    #print("-------------------------")
    string_list.append("-----------------")
    #print(f" Total Votes: {total_votes}")
    string_list.append(f"Total Votes: {total_votes}")
    #print("-------------------------")
    string_list.append("-------------------")
    #print(f"{candidate_vote_count}")
    #string_list.append(f"{candidate_vote_count}")

    maxper = 0.0
    for name in candidate_list:
        per = (candidate_vote_count[name]/total_votes*100)
        #per_new = '{0: .3f}'.format(per)

        #string_list.append(f" {name} : {per:.3f}% ({candidate_vote_count[name]})")

        #print(f" {name} : {per_new}% ({candidate_vote_count[name]})")

        if(per > maxper) :
            winner =name
            maxper = per

        string_list.append(f" {name} : {per:.3f}% ({candidate_vote_count[name]})")

    string_list.append("----------------------")
    #print("------------------------")
    string_list.append(f"Winner : {winner}")
    #print(f"Winner : {winner}")
    string_list.append("--------------------")
    #print("------------------------")

    filename = "Results.txt"
    with open (filename, 'w') as file:
        for i in string_list:
            print(i)
            file.write(i + "\n")



#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
