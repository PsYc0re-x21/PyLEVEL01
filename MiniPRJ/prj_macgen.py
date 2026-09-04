import random

a = int(input("Number of mac address you wanna generate: "))
# Lets save the macs in a file

def save(mac):
    with open("Macaddressgen.txt", "a") as file:
        file.write(mac + "\n")
def mac_gen():
    macaddr= ""
    count = 0 #for appending hyphen after every 2nd digits#
    
    charset = "1234567890abcdef"
    for i in range(1,12+1):
        count = count+1
        macaddr = macaddr + random.choice(charset)
        if count == 2:
            macaddr = macaddr + "-"
            count=0
    return macaddr

for i in range(1, a +1):

    mac = (mac_gen().upper()[:-1])
    print(mac)
    save(mac)


