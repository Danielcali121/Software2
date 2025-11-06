import requests

#keyword = input("Enter keyword: ")

# Request template: https://api.tvmaze.com/search/shows?q=girls
#request = "https://api.tvmaze.com/search/shows?q=" + keyword
#response = requests.get(request).json()
#print(response)




# Request template: https://api.tvmaze.com/search/shows?q=girls
request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
print(response['value'])