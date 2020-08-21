
import urllib.request
contents = urllib.request.urlopen("http://51.75.250.214:9999/canbricks/ping").read()
print(contents)