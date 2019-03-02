import requests
import json
token = '30aeb1079b3ec0c1e9734e20d682259219d305bcf6cb374fed8b4dc2868e5396'

url = 'https://api.digitalocean.com/v2/droplets'

name = input("Please give name for your droplet: ")

drop = {
    'ssh_keys': None,
    'tags': ['web'],
    'region': 'nyc3',
    'user_data': None,
    'volumes': None,
    'ipv6': True,
    'private_networking': None,
    'backups': False,
    'size': 's-1vcpu-1gb',
    'image': 'centos-7-x64',
    'name': name
    }

droplet = requests.post(url, json=drop, headers={'Authorization': 'Bearer {}'.format(token)})

print(drop.json())
