import requests

url = 'http://127.0.0.1:8000/extract/'

files = {
    'file': open('C:/Users/akash/Desktop/sample_input.txt', 'rb')  # update path as needed
}

response = requests.post(url, files=files)

print("STATUS CODE:", response.status_code)
print("RESPONSE TEXT:", response.text)
