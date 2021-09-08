import requests


def test_get_url(url):
    return
    print(f"Getting url: {url}")

    response = requests.get(url)
    print(response.content)
    print()


# Test ping
url = f"http://127.0.0.1:8000"
test_get_url(url)

url = f"http://127.0.0.1:8000/person?name=Ben"
test_get_url(url)

url = f"http://127.0.0.1:8000/person?name=Tawfiq"
test_get_url(url)

url = f"http://127.0.0.1:8000/person?name=Spiros"
test_get_url(url)


url = f"http://127.0.0.1:8000/person"
body = {"height_m": 2.1, "weight_kg": 75}

print(f"\nPosting to url: {url} -- {body}")

response = requests.post(url, json=body)
print(response.content)
