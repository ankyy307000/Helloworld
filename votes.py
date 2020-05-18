from collections import Counter
votes=["ankit", "john", "harry", "vivek", "ankit", "rahul","hemant", "hemant", "vivek","hemant", "vivek", "vivek","rahul"]

cnt=Counter(votes)
max_votes=max(cnt.values()) 
   
l=[i for i in cnt.keys() if cnt[i]==max_votes] 
  
print(sorted(l)[0]) 




