'''

1.	Get dictionary length
2.	Print the password of facebook
3.	Change the gmail password to “nopassword”
4.	Add an item to the dictionary, Spotify as key and myspotifypassword as a value
5.	Delete the facebook record
6.	Export the dictionary to excel
'''

# 1.	Get dictionary length
mypasswords = {
  "gmail": "mygmailpassword",
  "trebas": "mytrebaspassword",
  "facebook": "myfacebookpassword"
}

print(len(mypasswords))

# 2. Print the password of facebook

print(mypasswords["facebook"])

# 3. Change the gmail password to “nopassword”

mypasswords['gmail'] = "nopassword"
print(mypasswords)

# 4. Add an item to the dictionary, Spotify as key and myspotifypassword as a value

mypasswords['Spotify'] = "myspotifypassword"
print(mypasswords)

# 5. Delete the facebook record

mypasswords.pop("facebook")
print(mypasswords)

# 6. Export the dictionary to excel
import pandas as pd

df = pd.DataFrame(list(mypasswords.values()), index=mypasswords.keys()).T

df.to_excel('mid_term_TI1010664.xlsx', index=False)



