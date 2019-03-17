# -- coding: utf-8 --
# language: ru
from urllib.parse import urlencode
import requests
import pprint

OAUTH_URL = "https://oauth.vk.com/authorize"
APP_ID = 6892877

auth_data = {
  "client_id": APP_ID,
  "display": "page",
  "scope": "friends, status",
  "response_type": "token",
  "v": 5.92
}
print("?".join((OAUTH_URL, urlencode(auth_data))))
token = "9b9b712ed51513ae1b98258881b5baed75f544006f3c93f26af06858f617d962004a0d2f4721e8f08104b"

class Friends:
  def __init__(self, access_token):
    self.access_token = access_token

  def get_params(self):
    return {
      "access_token": token,
      "v": 5.92,
      "source_uid": 505135958,
      "target_uid": 457256223,
      "target_uids": "",
      "order": "",
      "count": "",
      "offset": ""
    }

  def getMutual_friends(self):
    params = self.get_params()
    response1 = requests.get("https://api.vk.com/method/friends.getMutual", params)
    return response1.json()

  def get_friends_name(self):
    params_2 = {
      "access_token": token,
      "v": 5.92,
      "user_id": "",
      "order": "",
      "list_id": "",
      "count": "",
      "offset": "",
      "fields": "verified",
      "name_case": ""
    }
    response = requests.get("https://api.vk.com/method/friends.get", params_2)
    return response.json()
    
    def __and__(self, other):
      return self.response & other.response
     
    def __str__(self):
      return "{}".format(self.access_token)

Me = Friends(token)
Mutual_friends = Me.getMutual_friends()
print (Mutual_friends)
Get_friends_name = Me.get_friends_name()
print(Get_friends_name)
print(Get_friends_name)
print(Me)
