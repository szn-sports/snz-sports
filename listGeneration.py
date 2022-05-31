import json,http.client as httplib
from pickle import TRUE
import random
import json

# player count: 2120 
# coach count:520
# matchups: 577 (later coming)
# total: 2640
# python bigasslist.py

## dict = kid 0 - 2639
#   leagues = ?
#       league names
#       amt of players
#   players = 2120
#       leauge
#       all atrbs
#   coach = 520
#       leauge
#       all atrbs

leagues = {
    # ETHEREUM CONFERENCE
    'Ethereum City Miners' : {'leageName' : 'Ethereum City Miners', 'playerCount' : 0},                   
    'Web3 Warriors' : {'leageName' : 'Web3 Warriors','playerCount' : 0},
    '8bit Tigers' : {'leageName' : '8bit Tigers','playerCount' : 0},
    'Blockchain Kings' : {'leageName' : 'Blockchain Kings','playerCount' : 0},
    'Two Point Zero' : {'leageName' : 'Two Point Zero','playerCount' : 0},
    'WAGMI Ducks' : {'leageName' : 'WAGMI Ducks','playerCount' : 0},
    'Floor Sweepers' : {'leageName' : 'Floor Sweepers','playerCount' : 0},
    "The Shiba Inu's" : {'leageName' : 'The Shiba Inus','playerCount' : 0},
    'Bullish Bulldogs' : {'leageName' : 'Bullish Bulldogs','playerCount' : 0},
    'Bearlin Goblins' : {'leageName' : 'Bearlin Goblins','playerCount' : 0},
    'Volume City Vipers' : {'leageName' : 'Volume City Vipers','playerCount' : 0},
    'Moon Rockets' : {'leageName' : 'Moon Rockets','playerCount' : 0},
    'Broken Sea Pirates' : {'leageName' : 'Broken Sea Pirates','playerCount' : 0},
    'The Secondary Snipers' : {'leageName' : 'The Secondary Snipers','playerCount' : 0},
    'Pump Punks' : {'leageName' : 'Pump Punks','playerCount' : 0},
    'Frenly Falcons' : {'leageName' : 'Frenly Falcons','playerCount' : 0},
    # BITCOIN CONFRENCE
    'Crypto Whales' : {'leageName' : 'Crypto Whales','playerCount' : 0},
    'Whitelist Ninjas' : {'leageName' : 'Whitelist Ninjas','playerCount' : 0},
    'Wallet Watchers' : {'leageName' : 'Wallet Watchers','playerCount' : 0},
    'The Blue Chips' : {'leageName' : 'The Blue Chips','playerCount' : 0},
    'The Minters' : {'leageName' : 'The Minters','playerCount' : 0},
    'Bitcoin City Mummies' : {'leageName' : 'Bitcoin City Mummies','playerCount' : 0},
    "The One of One's" : {'leageName' : "The One of One's",'playerCount' : 0},
    "Doge Demons" : {'leageName' : 'Doge Demons','playerCount' : 0},
    'Cryptoids' : {'leageName' : 'Cryptoids','playerCount' : 0},
    'Non Fungible Robots' : {'leageName' : 'Non Fungible Robots','playerCount' : 0},
    "Rugpullin' Raiders" : {'leageName' : "Rugpullin' Raiders",'playerCount' : 0},
    'The Profit Prophets' : {'leageName' : 'The Profit Prophets','playerCount' : 0},
    'Market Crashers' : {'leageName' : 'Market Crashers','playerCount' : 0},
    'Alpha Aliens' : {'leageName' : 'Alpha Aliens','playerCount' : 0},
    'The 0x Football Team' : {'leageName' : 'The 0x Football Team','playerCount' : 0},
    'Meta Giants' : {'leageName' : 'Meta Giants','playerCount' : 0}
}

leagueList = list(leagues.keys())




#MASTERLIST = {[ID = zzzz, NAME = xxxx, atb1 = xxxx]}

# GLOBALS

# POSITIONS

positionTypes = {'Quarterback': 3,'Offensive Linemen': 10,'Wide Receivers': 6,'Running Backs': 4,'Tight Ends': 3,'Defensive Linemen': 9,'Linebacker': 5,'Defensive Back': 10,'Kicker': 2,'Punter': 1}
positionTypeList = list(positionTypes.keys())


# APPERANCE, SKILLS, STAT


skinColors = {'Light' : 706, 'Medium' : 708, 'Dark' : 706}
skinColorList = list(skinColors.keys())

eyeColors = {'Light brown' : 423, 'Dark brown' : 423, 'Green' : 423, 'Blue' : 423, 'Dark yellow' : 423, 'Red' : 5}
eyeColorList = list(eyeColors.keys())
# eyeBlack = ['True', 'False']

mouthStyles = {'Smirk' : 503, 'Grin with teeth' : 403, 'Serious' : 353, 'Angry' : 303, 'Calm' : 278, 'Slight frown' : 253, 'Gold grin' : 27}
mouthStyleList = list(mouthStyles.keys())

facemaskType = {'Two bar' : 380, 'Two bar robot' : 380, 'Three bar' : 380, 'Three bar robot' : 380, 'Full cage': 600}
facemaskTypeList = list(facemaskType.keys())

gloveColors = {'White' : 628, 'Team Color': 626, 'Black' : 313, 'Light grey' : 313}
gloveColorsList = list(gloveColors.keys())

sockHeights = {'Short' : 265, 'Medium' : 1060, 'Tall' : 795}
sockHeightList = list(sockHeights.keys())

# cleatType = ['Short', 'Medium']


jerseyNumbersList = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53']


prevEyeBlack = 0

players = {}
for pid in range(0,53):
    pid = str(pid)
    playerInfo = {'LeagueInformation' : {}, 'Apperence' : {}, 'Skills' : {}, 'Stats' : {}}


    # POSITIONS 

    positionSelected = False
    ranPositionType = random.randint(0,9)

    # APPERERANCES
    
    leagueSelected = False
    skinSelected = False
    eyeSelected = False
    mouthSelected = False
    facemaskSelected = False
    gloveSelected = False
    sockSelected = False
    jerSelected = False
    positionSelected = False
    
    
    ranCleatType = random.randint(0,1)
    ranJerNumber = random.randint(0,52)
    

    # 'RANDOM' LEAGUE SELCTION
    while leagueSelected == False:
        ranLeague = random.randint(0,31)
        league = leagueList[0]
        if leagues[league]['playerCount'] != 53:
            playerInfo['LeagueInformation'] = leagues[league]
            playerInfo['LeagueInformation']['positionAmnts'] = positionTypes
            leagues[league]['playerCount'] += 1
            leagueSelected = True

    # JERSEY NUMBER SELECTION
    playerInfo['LeagueInformation']['jerseyNumber'] = jerseyNumbersList[playerInfo['LeagueInformation']['playerCount'] - 1]

    # POSITION SELECTION
    while positionSelected == False:
        ranPosition = random.randint(0,9)
        position = positionTypeList[ranPosition]
        if positionTypes[position] != 0:
            playerInfo['Position'] = position
            positionTypes[position] -= 1
            positionSelected = True

    # 'RANDOM' SKIN COLOR SELCTION
    while skinSelected == False:
        ranSkinColor = random.randint(0,2)
        skinColor = skinColorList[ranSkinColor]
        if skinColors[skinColor] != 0:
            playerInfo['Apperence']['skinColor'] = skinColor
            skinColors[skinColor] -= 1
            skinSelected = True
            
    # 'RANDOM' EYE COLOR SELECTION
    while eyeSelected == False:
        ranEyeColor = random.randint(0,5)
        eyeColor = eyeColorList[ranEyeColor]
        if eyeColors[eyeColor] != 0:
            playerInfo['Apperence']['eyeColor'] = eyeColor
            eyeSelected = True 

    # 'EVERY OTHER EYE BLACK'
    if prevEyeBlack == 0:
        eyeBlack = True
        prevEyeBlack = 1
        playerInfo['Apperence']['eyeBlack'] = eyeBlack
    else:
        eyeBlack = False
        prevEyeBlack = 0
        playerInfo['Apperence']['eyeBlack'] = eyeBlack

    # 'RANDOM' MOUTH STYLE SELECTION
    while mouthSelected == False:
        ranMouthStyle = random.randint(0,6)
        mouthStyle = mouthStyleList[ranMouthStyle]
        if mouthStyles[mouthStyle] != 0:
            playerInfo['Apperence']['mouthStyle'] = mouthStyle
            mouthSelected = True  

    # 'RANDOM' FACEMASK STYLE SELECTION
    while facemaskSelected == False:
        ranFacemask = random.randint(0,4)
        facemask = facemaskTypeList[ranFacemask]
        if facemaskType[facemask] != 0:
            playerInfo['Apperence']['facemaskType'] = facemask
            facemaskType[facemask] -= 1
            facemaskSelected = True

    # 'RANDOM' GLOVE STYLE SELECTION
    while gloveSelected == False:
        ranGloveColor = random.randint(0,3)
        gloveColor = gloveColorsList[ranGloveColor]
        if gloveColors[gloveColor] != 0:
            playerInfo['Apperence']['gloveColor'] = gloveColor
            gloveColors[gloveColor] -= 1
            gloveSelected = True
            
    # 'RANDOM' SOCK STYLE SELECTION          
    while sockSelected == False:
        ranSockHeight = random.randint(0,2)
        sockHeight = sockHeightList[ranSockHeight]
        if sockHeights[sockHeight] != 0:
            playerInfo['Apperence']['sockHeight'] = sockHeight
            sockHeights[sockHeight] -= 1
            sockSelected = True

    players[pid] = playerInfo

    for pid in players:
        if players[pid]['LeagueInformation']['leageName'] == 'Ethereum City Miners':
            print(players[pid]['LeagueInformation']['positionAmnts'])

    
# with open("players.json", "w") as outfile:
    # json.dump(players, outfile)
    # print('\n*******************************************************')
    # print('***** json dump complete, refer to "players.json" *****')
    # print('*******************************************************\n')
    

