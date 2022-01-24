import requests


print("R A H M A N   C O D I N G")
print("masukan targetnya web contoh : http://xxx.com")
url = input("masukin web target nya :")
output = input("masukin nama file keluaran :")


req = requests.get(url, 'html.parser')



with open(output, "w") as f:
     f.write(req.text)
     f.close()
