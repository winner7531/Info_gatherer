import whois
import socket
import requests
#hokage dattebayouu

proxies = {
    'https': 'socks5h://127.0.0.1:9050',
    'http': 'socks5h://127.0.0.1:9050'
}



def privat_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def get_geo_location():
    ip = input("Enter the ip address: ")
    if '.' not in ip:
        ip += ".com"
    geo_url = "http://ip-api.com/json/" + ip
    geo_data = requests.get(geo_url).json()
    print("Geo IP location...")
    print("IP: ", ip)
    print("Country: ", geo_data.get("country"))
    print("Region: ", geo_data.get("region"))
    print("City: ", geo_data.get("city"))
    print("ISP: ", geo_data.get("isp"))
    print("Timezone: ", geo_data.get("timezone"))
    print("Latitude/Longitude: ", geo_data.get("lat"), ",", geo_data.get("lon"))

def get_domain_info():
    try:
        d_name = input("Enter the domain (for eg. google.com)")
        
        domain_info = whois.whois(d_name)
        print(domain_info)
    except Exception as err:
        print(err)

def get_domain_ip():
    try: 
        d_name = input("enter the domain (for eg. google.com): ")
        if '.' not in d_name:
            d_name += ".com"
        domain_ip = socket.gethostbyname(d_name)
        print("getting domain ip")
        print("Domain IP: ", domain_ip)
    
    except Exception as err:
         print(err)


print("starting info-gatehrer...")


while(True):

    print('''🔥 INFO-GATHERING TOOL 🔍 by Panda
    Choose an option:
    1. Get Private IP
    2. Get Public IP
    3. Get Domain IP
    4. Get WHOIS Info
    5. Get Geo Info
    6. Get Tor IP
    7. Exit    
    '''
    )

    task = input("what do  want to do. Write the respecting number: ")
    if(task == '1'):#Get private IP address
        print("private IP", privat_ip())
        print("-" * 40)
    elif(task == '2'): #Get Public IP adress
        public_host_ip = requests.get('https://api.ipify.org').text
        print("Public IP", public_host_ip)
        print("-" * 40)
    elif(task == '3'):#Get domain IP
        get_domain_ip()
        print("-" * 40)
    elif(task == '4'):#GET whois info
        get_domain_info()
        print("-" * 40)
    elif(task =='5'): #get Geo Info
        get_geo_location()
        print("-" * 40)
    elif(task == '6'):
        try:
            tor_ip = requests.get("https://api.ipify.org", proxies=proxies).text
            print("Tor IP: ", tor_ip)
        except Exception as err:
            print("Tor is not running")
            print("Error", err)
    elif(task == '7'):#exit
        print("exiting...")
        break
    
print("-" * 40)