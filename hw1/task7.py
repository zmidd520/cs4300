import requests

# send a get request 
print("Making a GET request to https://www.google.com/")
r = requests.get("https://www.google.com/")

# response code - should be 200
print(f"GET Request Status Code: {r.status_code}")

# webpage HTML
print("Raw HTML:")
print(r.text)


# attempting a GET on a fake URL
print("Making a GET request to https://www.google.com/badlink")
fakeR = requests.get("https://www.google.com/badlink")

# response code - should be 404
print(f"Request Status Code: {fakeR.status_code}")

# webpage HTML
print("Raw HTML:")
print(fakeR.text)
