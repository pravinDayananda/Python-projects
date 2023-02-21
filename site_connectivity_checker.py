import urllib.request as urllib



def main(url):
 print("checking connectivity")

 response = urllib.urlopen(url)
 print("connected to",url, "successfully")
 print("the response code was:", response.getcode())


print("This is a site connectivity checker")
input_url = input("input the url of the site")

main(input_url)