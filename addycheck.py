import ethereumwalletgenerator as e
import requests
import time

key = ''
with open('key.txt') as f:
    key = f.readline()
runs = 0
while True:
    start_time = time.time()
    for _ in range(5):
        priv = []
        pub = []
        addr = []

        for _ in range(20):
            [private, public, addy] = e.gen(True)
            priv.append(private)
            pub.append(public)
            addr.append(addy)

        # build req
        req = 'https://api.etherscan.io/api?module=account&action=balancemulti&address='
        addresses = ','.join(addr)
        req += addresses + '&tag=latest&apikey=' + str(key)

        # print(req)
        response = requests.get(req).json()
        for i, account in enumerate(response['result']):
            if int(account['balance']) > 0:
                print(priv[i])
                print(pub[i])
                print(addr[i])
                print(account['account'])
    time_to_sleep = max(0, max(0, start_time - time.time())) # only 5 requests/second allowed
    time.sleep(time_to_sleep)
    runs += 1
    if runs % 10 == 0:
        print(runs, 'runs.\n', runs*100, 'addresses tested')
