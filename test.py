import requests


def test_get_url(url):
    print(f"Getting url: {url}")

    response = requests.get(url)
    print(response.content)
    print()


# # Test ping
# url = f"http://127.0.0.1:8000"
# test_get_url(url)

# url = f"http://127.0.0.1:8000/person?name=Ben"
# test_get_url(url)

# url = f"http://127.0.0.1:8000/person?name=Tawfiq"
# test_get_url(url)

# url = f"http://127.0.0.1:8000/person?name=Spiros"
# test_get_url(url)


# url = f"http://127.0.0.1:8000/person"
# body = {"height_m": 2.1, "weight_kg": 75}

# print(f"\nPosting to url: {url} -- {body}")

# response = requests.post(url, json=body)
# print(response.content)


# url = f"http://127.0.0.1:8000/predict_boston"
# body = {
#     "Crim": 0.22,
#     "Zn": 12.50,
#     "Indus": 7.87,
#     "Chas": 0.00,
#     "Nox": 0.52,
#     "Rm": 6.38,
#     "Age": 94.30,
#     "Dis": 6.35,
#     "Rad": 5.00,
#     "Tax": 311.00,
#     "Ptratio": 15.20,
#     "B": 392.52,
#     "Lstat": 20.45,
# }

# print(f"\nPosting to url: {url} -- {body}")

# response = requests.post(url, json=body)
# print("Predicted :", response.content)


url = f"http://127.0.0.1:8000/database"
test_get_url(url)


url = f"http://127.0.0.1:8000/database"
body = {
    "first_name": "Tester",
    "last_name": "Newman",
    "height": 1.56,
    "weight": 67,
}

print(f"\nPosting to url: {url} -- {body}")
response = requests.post(url, json=body)
print("Database posted:", response.content)


url = f"http://127.0.0.1:8000/database"
body = {
    "first_name": "Tester",
    "last_name": "Newman",
    "height": 1.56,
    "weight": 67,
    "id": 1,
}

print(f"\nPosting to url: {url} -- {body}")
response = requests.put(url, json=body)
print("Database put-ed:", response.content)
