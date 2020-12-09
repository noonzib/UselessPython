import urllib.request
import requests

url = "https://www.google.com/search?q=apple&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi-oPCgrcDtAhWPv5QKHY4FCGMQ_AUoAXoECAUQAw&biw=1920&bih=937"

response = requests.get(url)

print(response.text)

f = open("./temp.html","w")
f.write(response.text)
f.close()

#urllib.request.urlretrieve