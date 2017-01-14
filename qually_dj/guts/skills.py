import mechanize
from BeautifulSoup import BeautifulSoup
import urllib2 
import cookielib
import requests
cj = cookielib.CookieJar()
br = mechanize.Browser()

# br.set_handle_robots(False)
br.set_cookiejar(cj)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)



# br.addheaders = [('user-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36)'),
# ('authority', 'jobscan.co'), ('method', 'POST'),('path','/login'), ('scheme','https'), ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
# ('accept-encoding', 'gzip, deflate, br'), ('accept-language','en-US,en;q=0.8'), ('cache-control','max-age=0'),('content-length', '114'), ('content-type', 'application/x-www-form-urlencoded'),
# ('cookie', "__cfduid=daf31fdcfcb707d7b982ccb1ab191378f1482459489; optimizelyEndUserId=oeu1482459490356r0.15679222256993564; freescans=eyJpdiI6ImsxaVMybHkwemU3NjRDXC9yNkhnYmd3PT0iLCJ2YWx1ZSI6IlJQNXZRRmE3blRYQWNQU3diMVJBb3c9PSIsIm1hYyI6IjljZDg4MzUzYjk3YmRkMmJhZmY0MTdkNGM3ODliNDFjNjBjOTYzYjE0MGU4YTFjNDIxNGNmZDE0NzNlYzIzZjUifQ%3D%3D; a=eyJpdiI6IkE3MWpJR21xMzJZKzl2b3kyd3I1Y1E9PSIsInZhbHVlIjoiTUVSdEVXQXp2V0s3MUw3WHhiVkwzQT09IiwibWFjIjoiYzBiNjViM2I4NzIyZGIxM2FjZDc3MjczZjhhYjliMjgyYjc3M2VhOWQyMDEzYWViZjkzMTI0NjRjM2M5NjI2ZSJ9; __atssc=google%3B4%2Clinkedin%3B1; toaster_Dashboard intro=showed; toaster_Dashboard direct=showed; optimizelySegments=%7B%222538020172%22%3A%22gc%22%2C%222540870161%22%3A%22false%22%2C%222543250160%22%3A%22search%22%7D; optimizelyBuckets=%7B%227853986581%22%3A%227878600951%22%2C%228090063586%22%3A%228093893474%22%7D; XSRF-TOKEN=eyJpdiI6IlJ0XC9cL0wrNEFFajJlWk1sSU5Ob2hkQT09IiwidmFsdWUiOiJEdkJJRXd1SExaMThcL2thaFcwVmZpOERTY2xRXC9FQTlWeXBpclhOZzBNR3VqZ2dtbWFLS3JqYzRXWUtreUVXQ0FvUWhpV3RoNk5oVHVcL04rYnVMM1E5UT09IiwibWFjIjoiNjBiNjk1NGJmODUxYjIyMzk4NGZhY2RhZTdjOGRiMjM3ODY3NmJkNGMxNGZkZDVlMGRkZGJiM2ZhYmFjNjFjMiJ9; laravel_session=eyJpdiI6Im1HUm1DZzVnOExmN0ZpNTBYWGFlMXc9PSIsInZhbHVlIjoiczFUZkU5enhFVkQ5Zzh5b3RjQnBLbEljdHlsaXhjSTVzWWhmS3AwN0hDaUNZQ1lcL1hvUDJGK093Y1JmN3p2cU50Znd5YTFKY0FyRmp1MUNqeEpiQ2FBPT0iLCJtYWMiOiIxODhiZDBmNDlhMjg1YjFmYmFhMjIzZjgyNTI0ZDk0NGFlNDljN2JkYzVlNzk5NGViY2E0NjAyMzgyZWNmZmYxIn0%3D; __atuvc=11%7C51%2C64%7C52%2C13%7C1%2C26%7C2; __atuvs=5879c6b326877776007; _gat_UA-46519623-1=1; _ga=GA1.2.1859961107.1482459491; _gat=1; mp_8372d7d978a2c95c7c831351ed0025f5_mixpanel=%7B%22distinct_id%22%3A%20%22102923%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpap%22%3A%20%5B%5D%7D; mp_mixpanel__c=1; optimizelyPendingLogEvents=%5B%22n%3Dhttps%253A%252F%252Fwww.jobscan.co%252Flogin%26u%3Doeu1482459490356r0.15679222256993564%26wxhr%3Dtrue%26time%3D1484376456.214%26f%3D8152542042%26g%3D%22%5D"),
# ('origin', 'https://www.jobscan.co'), ('referer', 'https://www.jobscan.co/login'), ('upgrade-insecure-requests', '1')]
br.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3'),
('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]


br.open('https://www.jobscan.co/login')
 
br.select_form(name='reg')

br.form['email']= 'quai.wentt@gmail.com'

br.form['password']= 'qually123'

br.submit()

#open the job scan page
response = br.open('https://www.jobscan.co/results/1545538')
# soupify the response
soup = BeautifulSoup(response)

# get skills
skills=soup.findAll("span", attrs={"data-skillkey":True})

# get categories
categories = soup.findAll(attrs={"data-skill":True})


keywords =[]
for skill in skills:
	keywords.append(skill.getText())
for cat in categories:
	keywords.append(cat.getText())

keywords = set(keywords)

print keywords



