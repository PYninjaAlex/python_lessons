def restaurant_data():
  detail = {'details':[]}
  with open('restaurant.txt', 'r', encoding='utf-8') as data:
    items = data.read().split('***\n')
  for item in items:
    temp = item.split('\n')
    detail['details'].append({
      'administrator': temp[0],
      'workers': temp[1].split(', '),
      'turnover': int(temp[2]),
      'profit': int(temp[3]),
      'tips': int(temp[4])})
  return detail

print(restaurant_data())