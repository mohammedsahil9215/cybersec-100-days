# import requests

# response = requests.get("https://example.com")
# print(response.text)

# import requests

# response = requests.get("https://example.com")
# html = response.text

# start = html.find("<title>") + len("<title>")
# end = html.find("</title>")
# title = html[start:end]

# print(title)

# import requests

# session = requests.Session()

# login_data = {
#     "username": "admin",
#     "password": "wrongpass"
# }
# response = session.post("https://0a5b0008032731d18140433500bf00bd.web-security-academy.net/login", data=login_data)

# html = response.text
# start = html.find("<title>") + len("<title>")
# end = html.find("</title>")
# title = html[start:end]

# print(title)

# import sys
# import requests

# url = sys.argv[1]  # takes the lab URL from the command line

# session = requests.Session()

# login_data = {
#     "username": "admin",
#     "password": "wrongpass"
# }
# response = session.post(url + "/login", data=login_data)

# html = response.text
# start = html.find("<title>") + len("<title>")
# end = html.find("</title>")
# title = html[start:end]

# print(title)
import sys
import requests

url = sys.argv[1]

session = requests.Session()

login_data = {
    "username": "admin",
    "password": "wrongpass"
}
response = session.post(url + "/login", data=login_data)

html = response.text
start = html.find("<title>") + len("<title>")
end = html.find("</title>")
title = html[start:end]

print(title)