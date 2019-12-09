from shodan import Shodan

api = Shodan('QoN9YkJiB2w5o6AjYXaeXFxRIYocUCPX')


def ipscan():
    ip = raw_input("enter an ip address")

    host = api.host(ip)

    print("""
            IP:                      {}
            Organization:            {}
            City                     {}
            Operating System:        {}
            Hostnames:               {}
            Country:                 {}
            Updated:                 {}
            Number of open ports      {}
    """.format(host['ip_str'], host.get('org', 'n/a'), host.get('city', 'n/a'), host.get('os', 'n/a'), " ".join(host.get('hostnames')), host.get('country_name'), host.get('last_update'), len(host.get('ports'))))

    for item in host['data']:
        print("""Port: {} / {}            Product: {} """.format(
            item['port'], item['transport'], item.get('product', 'n/a')))


def myip():
    print(api.tools.myip())
    pass


def query():
    query = raw_input("enter a query")
    try:

        result = api.search(query)

        for service in result['matches']:
            print("""
            IP:{} Organization:    {} port :{}   {}
    """.format(service['ip_str'], service.get('org', 'n/a'), service.get('port'), " ".join(service.get('hostnames', 'n/a'))))

    except Exception as e:
        print('Error: %s' % e)


# ipscan()
# myip()
# query()
while True:
    choice = raw_input(
        "what would you like to do \n enter one of the following options\n 1: get your ip \n 2: search shodan\n 3: search host \n 4: quit\n ")
    if choice == "1":
        myip()
        pass
    elif choice == "2":
        query()
    elif choice == "3":
        ipscan()
    elif choice == "4":
        break
    else:
        print("invalid option")
        print(choice)
    pass
