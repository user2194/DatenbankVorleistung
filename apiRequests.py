from chessdotcom import get_leaderboards
from chessdotcom import get_player_profile

def getLeaderboards(gamemode,count = 50):#
    response = get_leaderboards()
    profiles = []
    for i in range(count):
        profiles.append(response.json["leaderboards"][gamemode][i])

    return profiles


def getProfile(username):
    response = get_player_profile(username)
    return response.json
