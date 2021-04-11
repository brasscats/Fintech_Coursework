

## format data as jason

import json

data = response_data.json()

#indent data

print(json.dumps(data, indent=4))


## Store value and store as variable
selected_value = data[0]


## Execute the numbers API fror the number 42

import requests
import json

#create parameterized url
request_URL = "httop;//numberapi.com/42?json"

# Submit request and format output
response_data = requests.get(request_url).json()
print(json.dumps(reponse_data, indent=4))

#select fact
response_data['text']



## House of Requests - TA Exercise
import requests
import json

#Declare request URL to create deck id
create_deck_url = "API url.com"

# Execute create deck url

response_data = requests.get(create_deck_url).json()
response_data


# Parse JSON data
deck_id = response_data['deck_id']
print(deck_id)

#declare draw_cards url and shuffle_deck_url
#use string interpolation to incorporate the deck_id
draw_cards_url = f
