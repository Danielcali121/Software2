#import requests


#hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
#pyyntö = "https://api.tvmaze.com/search/shows?q=" + hakusana
#vastaus = requests.get(pyyntö)
#vastaus1 = vastaus.json()

import json
import requests

#hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
#pyyntö = "https://api.tvmaze.com/search/shows?q=" + hakusana

#try:
    #vastaus = requests.get(pyyntö)
    #if vastaus.status_code==200:
        #json_vastaus = vastaus.json()
        #print(json.dumps(json_vastaus, indent=2))
        #for a in json_vastaus:
            #print(a["show"]["name"])
#except requests.exceptions.RequestException as e:
    #print ("Hakua ei voitu suorittaa.")










from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/prime_number/<int:number>')
def CALC(number):

    if number<2:
        return jsonify({"Number": number, "isPrime": False})

    status = True

    for i in range(2, int(number**0.5)+1):
        if number%i ==0:
            status = False
            break

    return jsonify({"Number": number, "isPrime": status})











if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

#http://127.0.0.1:3000



