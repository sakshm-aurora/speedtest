import speedtest

s=speedtest.Speedtest()

option = int(input('''What do you wanna know ? 
	1) Upload Speed
	2) Download Speed
	: '''))

if option==1:
	print(s.upload())
	exit(0);
elif option==2:
	print(s.download())
else:
	print("Invalid Option")