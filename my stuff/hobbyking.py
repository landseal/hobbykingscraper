import urllib.request

response = urllib.request.urlopen('https://hobbyking.com/en_us/turnigy-aerodrive-sk3-6374-149kv-brushless-outrunner-motor.html')
html = response.read().decode('utf-8')

price = ''
index = 0
for i in range(len(html)):
	if html[i:i+5] == 'price':
		index = i+7
		break

for i in range(7):
	if str(html[index+i]) == '}':
		break
	price += str(html[index+i])
		
print('$'+price)