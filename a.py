import json


b = '''{"action":"payment.updated","api_version":"v1","data":{"id":"80149082212"},"date_created":"2024-06-08T23:48:59Z","id":113906728960,"live_mode":true,"type":"payment","user_id":"1842227027"}'''
           
b = json.loads(b)

print(b["data"]["id"])

