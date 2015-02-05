import requests
import os


def test_1():
	with open('trial') as fileHandle:
	    dataList = fileHandle.read().splitlines()

        # adama login url
	loginUrl = 'https://t1qa2.mediamath.com/api/v1/login'
        
        # make a POST request for login into ADAMA
	cred = {'user':'rmuddu','password':'vasu6883'}
	r = requests.post(loginUrl,data=cred)

        # parse the headers to retrieve cookie information
	cookieValue = r.headers['Set-Cookie'].split(';')[0].split('=')
	myCookie = {cookieValue[0]:cookieValue[1]}

	# reporting generic url
	reportingUrl = 'https://t1qa2.mediamath.com/reporting/v1/std'
 
	#Fetch meta information for performance report
	for aListItem in dataList:
		r = requests.get(reportingUrl + '/' + aListItem, cookies=myCookie)
		assert r.status_code == 200

