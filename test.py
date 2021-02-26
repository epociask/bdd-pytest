import requests

headers = {
    'Content-Type': 'application/json',
}

data = '{"INPUT": "hello world"}'

response = requests.post('http://api.shoutcloud.io/V1/SHOUT', headers=headers, data=data)

print(response.status_code)
