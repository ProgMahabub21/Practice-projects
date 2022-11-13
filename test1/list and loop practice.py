#list and loop practice

carlists = ['Ducati','Prado','Toyota','bmw','mercedez','Tesla','rolls royales'];

#print(carlists);

print(carlists[-1])
print(carlists[1:3]); #slicing syntax: [start index:end index]; by default [0:n-1]
carlists[0]='honda'; #editing list element
print(carlists[0])

carlists.append('ducati') # append()s elem at end only
carlists.insert(1,'hyundai') #insert elem at any position with first param indicates index
del carlists[1];   #deletes elem from list based on passed index
carlists.pop()   #default value -1, it can assigned specific as well

#carlists.remove('ducati'); #removes elem from list based on passed item value on first occurance
carlists.sort(); #sorting permanently ascending
carlists.sort(reverse=True); #sorting permanently decending,, default false
sorted(carlists);  #sorts temporarly

age = 19;
age <=21
msg= input("Tell your name , i will repeat with you :");
print(msg)

for carlist in carlists:
    if carlist == 'bmw':
        print(carlist.upper());

if 'bmw' in carlist:
    print("BMW")