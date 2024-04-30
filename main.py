import requests
import json

url = 'https://jsonplaceholder.typicode.com/posts/1'
url_users = 'https://jsonplaceholder.typicode.com/users'
user_data = {
    "name": "Diyorbek Aliqo'ziyev",
    "username": "dalikuziev",
    "email": "dalikuziev@gmail.com",
    "address": {
        "street": "Chilanzar",
        "suite": "Naqqoshlik 19",
        "city": "Tashkent",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    },
    "phone": "+998772522608",
    "website": "dalikuziev.uz",
    "company": {
        "name": "Company",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets"
    }
}
resp_user = requests.post(url_users, data=json.dumps(user_data), headers={'Content-Type': 'application/json; charset=utf-8'})
if resp_user.ok:
    up_data = {
        "userId": resp_user.json()['id'],
        "title": "Osiyo kubogi U23. O‘zbekiston Indoneziyani mag‘lub etib, o‘z tarixida ilk marta Olimpiadaga yo‘llanma oldi",
        "body": """
        Qatarda o‘tayotgan Osiyo kubogi U23 yarimfinali doirasida O‘zbekiston olimpiya jamoasi Indoneziyani 
        mag‘lub etib, finalga chiqish bilan birga o‘z tarixida ilk bor Olimpiadaga yo‘llanma oldi. 
        Temur Kapadze shogirdlari Parijda o‘tadigan har to‘rt yillikning eng yirik sport musobaqasida ishtirok etishadi. 
        Vakillarimiz finalda 3 may kuni Iroq – Yaponiya o‘yini g‘olibiga qarshi saf tortadi.
        """
    }
    resp_up = requests.put(url, data=json.dumps(up_data), headers={'Content-Type': 'application/json; charset=utf-8'})
    if resp_up.ok:
        resp = resp_up.json()

        print(f"Maqola {resp['id']}\n"
              f"Sarlavha: {resp['title']}\n\n"
              f"{resp['body']}\n\n"
              f"Author: {user_data['name']}, {user_data['address']['city']} {user_data['address']['street']}")
    else:
        print('Ma\'lumotlar o\'zgartirilmadi')
else:
    print('Foydalanuvchi qo\'shilmadi')
