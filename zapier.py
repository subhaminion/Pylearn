import json


data = {  
    "app_name":"com.google.android.lolwa",
    "app_env":"staging",
    "min_os_version":"1",
    "app_action":"halt",
    "login_required":True,
    "user_roles": [
      {
          "userrole": [
          {
            "role": "admin",
            "credentail": [
              {
                "username": "yash",
                "password": "subham12345"
              },
              {
                "username": "lino",
                "password": "test12"
              }
            ]
          }
        ]
      },
      {
        "userrole": [
          {
            "role": "customerwa",
            "credentail": [
              {
                "username": "yashwa",
                "password": "test1"
              },
              {
                "username": "linowa",
                "password": "test12"
              }
            ]
          }
        ]
      }
    ],
    "vpn_required":True,
    "vpn_details":{  
        "address":"dsd",
        "port":"sd",
        "username":"sdsd",
        "password":"sdsds"
    },
    "contact":{  
        "name":"dss",
        "email":"sdsd"
    },
    "additional_comments":"dsd"
}

new_dict = []
for value in data['user_roles']:
	for value2 in value['userrole']:
		for value3 in value2['credentail']:
			new_dict.append({
				'role': value2['role'],
				'username': value3['username'],
				'password': value3['password']
			})
data['user_roles'] = new_dict
# print(data)
print(json.dumps(data, indent=4, sort_keys=True))
