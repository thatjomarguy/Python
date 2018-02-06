import requests

def requestData(region, summonerName, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

def requestMastery(region, ID, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/champion-mastery/v3/scores/by-summoner/" + ID + "?api_key=" + APIKey
    response = requests.get(URL)
    print("Summoner Mastery Level: " + str(response.json()) + "\n")

def main():
    region = str('na1')
    summonerName = str(input('Enter Summoner Name: '))
    APIKey = str('RGAPI-2b346912-db62-466e-aa7f-da1c2701b9bf')

    if summonerName == '-1':
        return 0

    responseJSON = requestData(region, summonerName, APIKey)

    #Account Details
    ID = str(responseJSON['id'])
    accountID = str(responseJSON['accountId'])
    name = str(responseJSON['name'])
    profileIconID = str(responseJSON['profileIconId'])
    summonerLevel = str(responseJSON['summonerLevel'])

    print("\nSummoner: " + name)
    print("Level: " + summonerLevel)
    print("SummonerID: " + ID)
    print("AccountID: " + accountID)
    print("Profile Icon: " + profileIconID)

    requestMastery(region, ID, APIKey)

    main()

if __name__ == "__main__":
    main()
