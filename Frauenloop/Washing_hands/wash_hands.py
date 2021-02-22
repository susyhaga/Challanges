def wash_hands(n,nM):
    days = 30*nM
    times_wash = n*days
    time_spent = times_wash*21
    time_spent_min = time_spent//60
    time_spent_sec = time_spent%60
    return ('{} minutes and {} seconds'.format(time_spent_min,time_spent_sec))


print(wash_hands(8,7))
print(wash_hands(0,0))
print(wash_hands(7,9))
