home_appliances=['coffee maker','watering controller','sprinkler controller','plant monitor','automatic feeder','precision cooker','oven','grill thermometer']

entertainment=['wristband','wireless speakers','tv','television']

health_fitness=['activity tracker','yoga mat','thermometer','blood pressure monitor','fitbit','sleep tracker','heart rate monitoring']

general_purpose=['kindle','laptops','computer','desktop','mobile','cellphones']

def categorize(dnss, dest_ip_count):
    dns = dnss.split()
    for index,x in enumerate(dns):
        dns[index]=x.lower()

    for i in dns:
        print i
        if i in home_appliances:
            return 'home'
        elif i in entertainment:
            return 'enter'
        elif i in health_fitness:
            return 'health'
        elif i in general_purpose:
            return 'general'

    if dest_ip_count < 50:
        return 'health'
    elif dest_ip_count < 100:
        return 'home'
    elif dest_ip_count < 1000:
        return 'enter'
    else:
        return 'general'


print categorize(["samsung"], 100)