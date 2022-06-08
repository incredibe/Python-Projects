import pyshorteners

url = pyshorteners.Shortener()

print(url.tinyurl.short("www.google.com"))
