import http.client


zipcode = input('What is your zipcode? :')

conn = http.client.HTTPSConnection("us-weather-by-zip-code.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "us-weather-by-zip-code.p.rapidapi.com",
    'x-rapidapi-key': "87150c8337msh689ce6b15fb86e9p196a27jsn583463ea8378"
}

conn.request("GET", f"/getweatherzipcode?zip={zipcode}", headers=headers)

res = conn.getresponse()
data = res.read()

decoded = data.decode("utf-8")

print(decoded)
