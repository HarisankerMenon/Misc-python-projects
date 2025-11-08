t=open("tweet","r")
sum=0
word_count=0
pos_count=0
neg_count=0
pos_dic={"good":1.0,"great":1.0,"smart":1.0,"culture":1.0,"perfect":1.0}
neg_dic={"upper":-1.0,"long":-1.0,"expensive":-1.0,"life":-1.0,"working":-1.0}
inc_dic={"people":0.5,"culture":0.5,"hours":0.5}

for i in t:
    data = i.lower().rstrip("\n").split(" ")
    for i in data:
        if i in inc_dic and data[data.index(i)+1] in pos_dic:
            sum = sum+inc_dic[i]
        elif i in inc_dic and data[data.index(i)+1] in neg_dic:
            sum = sum - inc_dic[i]
        elif i in pos_dic:
            sum = sum + pos_dic[i]
        elif i in neg_dic:
            sum = sum + neg_dic[i]
        else:
            pass


if sum > 0:
    print(f"the review is positive\npolarity:{sum}\n")
elif sum==0:
    print(f"the review is neutral\n")
else:
    print(f"the review is negative\npolarity:{sum}\n")

        