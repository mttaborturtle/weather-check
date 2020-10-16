import http.client


zipcode = input('What is your zipcode? :')

conn = http.client.HTTPSConnection("us-weather-by-zip-code.p.rapidapi.com")

# Enter your personal key that you recieve from https://rapidapi.com/
# You will get a key for free when you sign up.
headers = {
    'x-rapidapi-host': "us-weather-by-zip-code.p.rapidapi.com",
    'x-rapidapi-key': "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}

conn.request("GET", f"/getweatherzipcode?zip={zipcode}", headers=headers)

res = conn.getresponse()
data = res.read()

decoded = data.decode("utf-8")

print(decoded)
