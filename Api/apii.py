import requests

api_key="5897e524c5c23fc8e46c7767af82a495"
Url=f"https://jsonplaceholder.typicode.com/comments"
response = requests.get(Url)
print(f"Response code: ={response.status_code}")
data=response.json()
print(data[1])