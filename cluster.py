
home_appliances=['coffee maker','watering controller','sprinkler controller','plant monitor','automatic feeder','precision cooker','oven','grill thermometer']

entertainment=['wristband','wireless speakers','tv','television']

heatlth_fitness=['activity tracker','yoga mat','thermometer','blood pressure monitor','fitbit','sleep tracker','heart rate monitoring']

general_purpose=['kindle','laptops','computer','desktop','mobile','cellphones']


a=['Samsung']

def categorize(dns, dest_ip_count, dest_port):
    for index,x in enumerate(a):
        dns[index]=x.lower()
#print 'snxkaan'
#print a
    for i in a:
        print i
        if i in home_appliances:
            print 'I am home app'
            return 'home'
        elif i in entertainment:
            print 'I am enter'
            return 'enter'
        elif i in heatlth_fitness:
            print 'I am health'
            return 'health'
        elif i in general_purpose:
            print 'I am general'
            return 'general'

    for i in a:
        if dest_ip_count < 50:
            print 'I am health'
            return 'health'
        elif dest_ip_count < 100:
            print 'I am home app'
            return 'home'
        elif dest_ip_count < 1000:
            print 'I am enter'
            return 'enter'
        else:
            print 'I am general'
            return 'general'

    #input is a list of destination ports

    heavily_used_port=max(set(dest_port), key=lst.count)
    if (heavily_used_port== || heavily_used_port ==):
        print 'I am health'
        return 'health'
    elif (heavily_used_port == || heavily_used_port ==):
         print 'I am home app'
         return 'home'
    elif (heavily_used_port == || heavily_used_port ==):
        print 'I am enter'
        return 'enter'
    else:
        print 'I am general'
        return 'general'




#b=[samsung,smart,tv,hd,hdquality,sony,lg,panasonic,vizio,toshiba,sharp,philips,Mmitsubishi,hisense,television,google,googletelevision,]