import requests


base_url =  'https://ctf.wpictf.xyz/{}?page={}'

for i in range(1,33):
  print('Trying page #{}'.format(i))
  team_url = base_url.format('teams',i)
  team_req = requests.get(team_url).text
  user_url = base_url.format('users',i)
  user_req = requests.get(user_url).text

  if ('WPI{' in user_req) or ('WPI{' in team_req):
      print(user_req)
      print(team_req)
      break


