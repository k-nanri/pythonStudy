import requests

if __name__ == '__main__':

    url = 'http://localhost:8081/members'
    response = requests.get(url)

    # http status code
    print("HTTP Status Code = ", response.status_code)
    response_body = response.json()
    print(response_body)
    members = response_body['members']

    for item in members:
        print("Name = ", item['name'])


