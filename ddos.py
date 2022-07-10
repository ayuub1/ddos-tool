import requests as req


print("""

    tool by lord sabokaa well try it

        """)
print("")


url = input("enter url : ")

number = int(input("enter number of times you want to sent requests : "))

for i in range(number):
    req.sent(url)



