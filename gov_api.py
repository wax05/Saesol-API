import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

res = requests.get(url)
json_res = res.json()
print(json_res['userId'])