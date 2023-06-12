import apiRequests

profile = apiRequests.getLeaderboards("live_bullet",10)

for i in range(10):
    print(i+1,": ", profile[i])
    print()
    print()
    print()

