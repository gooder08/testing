import requests
import yadisk
from pprint import pprint


# def get_yadisk():
#     with open("/home/gooder08/Projects/testing/ya_disk/token ya.ini") as file:
#         token_ya = file.read().strip()
#         y = yadisk.YaDisk(token=token_ya)
#         y.mkdir("/vvv")


# get_yadisk()


def ya_disk_create_folder():
    with open("/home/gooder08/Projects/testing/ya_disk/token ya.ini") as file:
        token_ya = file.read().strip()
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            "Authorization": token_ya,
            "Content-Type": "application/json",
        }
        params = {'path': 'new_folder', 
                  'overwrite': 'false'
        }
      
        # res = requests.get(url=url, headers=headers, params=params)
        
        record = requests.put(url, headers=headers, params=params)
        return record.status_code
 
    
def ya_auth():
    with open("/home/gooder08/Projects/testing/ya_disk/token ya.ini") as file:
        token_ya = file.read().strip()
        url = "https://cloud-api.yandex.net/v1/disk"
        headers = {
            "Authorization": token_ya,
            "Content-Type": "application/json",
        }
        res = requests.get(url=url, headers=headers)
        return res.status_code
    
def delete_folder():
    with open("/home/gooder08/Projects/testing/ya_disk/token ya.ini") as file:
        token_ya = file.read().strip()
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            "Authorization": token_ya,
            "Content-Type": "application/json",
        }
        params = {'path': 'new_folder', 
    
        }
        res = requests.delete(url=url, headers=headers, params=params)
        return res.status_code
    


    
    




