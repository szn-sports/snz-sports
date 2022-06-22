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

# Functions I wish I made sooner 

def skillRange(pos):
    if pos == 'h':
        return random.randint(50,80)
    else:
        return random.randint(0,49)
def notCommonSkill():
    return random.randint(0,50)


def getMax(level):
    if level == 'h':
        return random.randint(85-99)

    


nameFile = open('names.txt', 'r')
allNames = nameFile.readlines()

nameList = []
for name in allNames:
    nameList.append(name.strip())

positionTypes = {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    }

leagues = {
    # ETHEREUM CONFERENCE
    'Ethereum City Miners' : {'leageName' : 'Ethereum City Miners', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    }, 'playerCount' : 0},                   
    'Web3 Warriors' : {'leageName' : 'Web3 Warriors', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    '8bit Tigers' : {'leageName' : '8bit Tigers', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'Blockchain Kings' : {'leageName' : 'Blockchain Kings', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'Two Point Zero' : {'leageName' : 'Two Point Zero', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'WAGMI Ducks' : {'leageName' : 'WAGMI Ducks', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'Floor Sweepers' : {'leageName' : 'Floor Sweepers', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    "The Shiba Inu's" : {'leageName' : 'The Shiba Inus', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'Bullish Bulldogs' : {'leageName' : 'Bullish Bulldogs', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'Bearlin Goblins' : {'leageName' : 'Bearlin Goblins', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'Volume City Vipers' : {'leageName' : 'Volume City Vipers', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'Moon Rockets' : {'leageName' : 'Moon Rockets', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'Broken Sea Pirates' : {'leageName' : 'Broken Sea Pirates', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'The Secondary Snipers' : {'leageName' : 'The Secondary Snipers', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'Pump Punks' : {'leageName' : 'Pump Punks', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'Frenly Falcons' : {'leageName' : 'Frenly Falcons', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    # BITCOIN CONFRENCE
    'Crypto Whales' : {'leageName' : 'Crypto Whales', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'Whitelist Ninjas' : {'leageName' : 'Whitelist Ninjas', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'Wallet Watchers' : {'leageName' : 'Wallet Watchers', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'The Blue Chips' : {'leageName' : 'The Blue Chips', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'The Minters' : {'leageName' : 'The Minters', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'Bitcoin City Mummies' : {'leageName' : 'Bitcoin City Mummies', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    "The One of One's" : {'leageName' : "The One of One's", 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    "Doge Demons" : {'leageName' : 'Doge Demons', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'Cryptoids' : {'leageName' : 'Cryptoids', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'Non Fungible Robots' : {'leageName' : 'Non Fungible Robots', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    "Rugpullin' Raiders" : {'leageName' : "Rugpullin' Raiders", 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'The Profit Prophets' : {'leageName' : 'The Profit Prophets', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'Market Crashers' : {'leageName' : 'Market Crashers', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},
    'Alpha Aliens' : {'leageName' : 'Alpha Aliens', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},

    'The 0x Football Team' : {'leageName' : 'The 0x Football Team', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0},

    'Meta Giants' : {'leageName' : 'Meta Giants', 'positionAmnt' : {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    },'playerCount' : 0}
}

playerSkills = {
    'Physical' : {'Strength' : 0, 'Endurance' : 0}, 
    'Blocking' : {'Run Blocking' : 0, 'Pass Blocking' : 0}, 
    'Passing' : {'Passing Vision' : 0, 'Passing Power' : 0, 'Passing Accuracy' : 0}, 
    'Defense' : {'Pass Coverage' : 0, 'Tackling' : 0, 'Pass Rushing' : 0, 'Run Stopping' : 0}, 
    'Rushing/Receiving' : {'Elusiveness' : 0, 'Route Running' : 0, 'Hands' : 0, 'Ball Security' : 0},
    'Kicking' : {'Kick Power' : 0, 'Kick Accuracy' : 0, 'Punt Power' : 0, 'Punt Accuracy' : 0}
    }


leagueList = list(leagues.keys())




#MASTERLIST = {[ID = zzzz, NAME = xxxx, atb1 = xxxx]}

# GLOBALS

# POSITIONS
avalLeagues = leagueList

positionTypes = {
    'Quarterback': 3,
    'Offensive Linemen': 10,
    'Wide Receiver': 6,
    'Running Back': 4,
    'Tight End': 3,
    'Defensive Linemen': 9,
    'Linebacker': 5,
    'Defensive Back': 10,
    'Kicker': 2,
    'Punter': 1
    }
positionTypeList = list(positionTypes.keys())


# APPERANCE, SKILLS, STAT


skinColors = {'Light' : 706, 'Medium' : 708, 'Dark' : 706}
skinColorList = list(skinColors.keys())

eyeColors = {'Light brown' : 423, 'Dark brown' : 423, 'Green' : 423, 'Blue' : 423, 'Dark yellow' : 423, 'Red' : 5}
eyeColorList = list(eyeColors.keys())

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
prevCleatType = 0

players = {}
artistList = {}
test = []
for pid in range(0,1696):
    pid = str(pid)
    playerInfo = {'Name' : '', 'LeagueInformation' : {}, 'Apperence' : {}, 'Skills' : playerSkills, 'Stats' : {}}


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
    skillsAssigned = False
    fitTypeAssigned = False

    
    ranCleatType = random.randint(0,1)
    
    # NAME SELECTION
    playerName = nameList[int(pid)]
    playerInfo['Name'] = playerName

    # 'RANDOM' LEAGUE SELCTION
    league = ''
    while leagueSelected == False:
        if(len(leagueList) - 1 == 1):
            ranLeague = 0
        
        if(len(leagueList) == 0):
            print(pid)
            break
        else:
            ranLeague = random.randint(0,len(leagueList) - 1)
        league = leagueList[ranLeague]
        if leagues[league]['playerCount'] != 53:    
            playerInfo['LeagueInformation'] = leagues[league]
            leagues[league]['playerCount'] += 1
            leagueSelected = True
        else:
            # print(league+ ' full at ' +pid)
            leagueList.remove(league)
            continue

    # JERSEY NUMBER SELECTION
    playerInfo['LeagueInformation']['jerseyNumber'] = jerseyNumbersList[playerInfo['LeagueInformation']['playerCount'] - 1]
    # POSITION SELECTION
   
    while positionSelected == False:
        
        ranPosition = random.randint(0,9)
        position = positionTypeList[ranPosition]
        if leagues[league]['positionAmnt'][position] != 0:
            playerInfo['LeagueInformation']['position'] = position
            leagues[league]['positionAmnt'][position] -= 1
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
            mouthStyles[mouthStyle] -= 1
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
        if playerInfo['LeagueInformation']['position'] == 'Quarterback' or playerInfo['LeagueInformation']['position'] == 'Punter' or playerInfo['LeagueInformation']['position'] == 'Kicker':
            playerInfo['Apperence']['gloveColor'] = 'NO GLOVES'
            gloveSelected = True
        else:
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


    # 'RANDOM' FIT TYPE SELECTION
    while fitTypeAssigned == False:
        ranFitType = random.randint(0,1)
        if playerInfo['LeagueInformation']['position'] == 'Quarterback': 
            fitType = 'Fit'
            fitTypeAssigned = True
        elif 'Lineman' in playerInfo['LeagueInformation']['position']:
            fitType = 'Bulky'
            fitTypeAssigned = True
        else:
            if ranFitType == 0:
                fitType = 'Fit'
            else:
                fitType = 'Bulky'
        playerInfo['Apperence']['fitType'] = fitType
        fitTypeAssigned = True

    # 'RANDOM' CLEAT SELECTION
    if playerInfo['Apperence']['fitType'] == 'Fit':
        playerInfo['Apperence']['cleatType'] = 'short'
    if playerInfo['Apperence']['fitType'] == 'Bulky':
        if prevCleatType == 0:
            playerInfo['Apperence']['cleatType'] = 'Short'
            prevCleatType = 1
        else:
            playerInfo['Apperence']['cleatType'] = 'Medium'
            prevCleatType = 0
    if 'Lineman' in playerInfo['LeagueInformation']['position']:
        playerInfo['Apperence']['cleatType'] = 'Medium'



    
    ## GENERATE SKILL LEVELS BAISED OFF POSITION 
    overallRating = 0
    while skillsAssigned == False:
        playerInfo['Skills']['Physical']['Strength'] = skillRange('b')
        playerInfo['Skills']['Physical']['Speed'] = skillRange('b')
        playerInfo['Skills']['Physical']['Endurance'] = skillRange('b')
        playerInfo['Skills']['Blocking']['Run Blocking'] = skillRange('b')
        playerInfo['Skills']['Blocking']['Pass Blocking'] = skillRange('b')
        playerInfo['Skills']['Passing']['Passing Vision'] = skillRange('b')
        playerInfo['Skills']['Passing']['Passing Power'] = skillRange('b')
        playerInfo['Skills']['Passing']['Passing Accuracy'] = skillRange('b')
        playerInfo['Skills']['Defense']['Pass Coverage'] = skillRange('b')
        playerInfo['Skills']['Defense']['Tackling'] = skillRange('b')
        playerInfo['Skills']['Defense']['Pass Rushing'] = skillRange('b')
        playerInfo['Skills']['Defense']['Run Stopping'] = skillRange('b')
        playerInfo['Skills']['Rushing/Receiving']['Elusiveness'] = skillRange('b')
        playerInfo['Skills']['Rushing/Receiving']['Route Running'] = skillRange('b')
        playerInfo['Skills']['Rushing/Receiving']['Hands'] = skillRange('b')
        playerInfo['Skills']['Rushing/Receiving']['Ball Security'] = skillRange('b')
        playerInfo['Skills']['Kicking']['Kick Power'] = skillRange('b')
        playerInfo['Skills']['Kicking']['Kick Accuracy'] = skillRange('b')
        playerInfo['Skills']['Kicking']['Punt Power'] = skillRange('b')
        playerInfo['Skills']['Kicking']['Punt Accuracy'] = skillRange('b')
        if position =='Quarterback':
            if notCommonSkill() == 10:
                playerInfo['Skills']['Physical']['Speed'] = skillRange('h')
            playerInfo['Skills']['Passing']['Passing Vision'] = skillRange('h')
            playerInfo['Skills']['Passing']['Passing Power'] = skillRange('h')
            playerInfo['Skills']['Passing']['Passing Accuracy'] = skillRange('h')    
            playerInfo['Skills']['Rushing/Receiving']['Elusiveness'] = skillRange('h')
            playerInfo['Skills']['Rushing/Receiving']['Ball Security'] = skillRange('h')
        elif position == 'Offensive Linemen':
            playerInfo['Skills']['Physical']['Strength'] = skillRange('h')
            playerInfo['Skills']['Blocking']['Run Blocking'] = skillRange('h')
            playerInfo['Skills']['Blocking']['Pass Blocking'] = skillRange('h')
        elif position == 'Wide Receiver': 
            playerInfo['Skills']['Physical']['Speed'] = skillRange('h')
            playerInfo['Skills']['Physical']['Endurance'] = skillRange('h')
            playerInfo['Skills']['Rushing/Receiving']['Elusiveness'] = skillRange('h')
            playerInfo['Skills']['Rushing/Receiving']['Route Running'] = skillRange('h')
            playerInfo['Skills']['Rushing/Receiving']['Hands'] = skillRange('h')
            playerInfo['Skills']['Rushing/Receiving']['Ball Security'] = skillRange('h')
        elif position == 'Running Back':
            playerInfo['Skills']['Physical']['Strength'] = skillRange('h')
            playerInfo['Skills']['Physical']['Speed'] = skillRange('h')
            playerInfo['Skills']['Physical']['Endurance'] = skillRange('h')
            playerInfo['Skills']['Rushing/Receiving']['Elusiveness'] = skillRange('h')
            playerInfo['Skills']['Rushing/Receiving']['Hands'] = skillRange('h')
            playerInfo['Skills']['Rushing/Receiving']['Ball Security'] = skillRange('h')
        elif position == 'Tight End':
            playerInfo['Skills']['Blocking']['Run Blocking'] = skillRange('h')
            playerInfo['Skills']['Blocking']['Pass Blocking'] = skillRange('h')
            playerInfo['Skills']['Rushing/Receiving']['Route Running'] = skillRange('h')
            playerInfo['Skills']['Rushing/Receiving']['Hands'] = skillRange('h')
        elif position == 'Defensive Linemen':
            playerInfo['Skills']['Physical']['Strength'] = skillRange('h')
            playerInfo['Skills']['Physical']['Speed'] = skillRange('h')
            playerInfo['Skills']['Blocking']['Run Blocking'] = skillRange('h')
            playerInfo['Skills']['Blocking']['Pass Blocking'] = skillRange('h')
            playerInfo['Skills']['Defense']['Pass Coverage'] = skillRange('h')
            playerInfo['Skills']['Defense']['Tackling'] = skillRange('h')
            playerInfo['Skills']['Defense']['Pass Rushing'] = skillRange('h')
            playerInfo['Skills']['Defense']['Run Stopping'] = skillRange('h')
        elif position == 'Linebacker':
            playerInfo['Skills']['Physical']['Strength'] = skillRange('h')
            if notCommonSkill() == 10:
                playerInfo['Skills']['Physical']['Speed'] = skillRange('h')
            playerInfo['Skills']['Defense']['Pass Coverage'] = skillRange('h')
            playerInfo['Skills']['Defense']['Tackling'] = skillRange('h')
            playerInfo['Skills']['Defense']['Pass Rushing'] = skillRange('h')
            playerInfo['Skills']['Defense']['Run Stopping'] = skillRange('h')
        elif position == 'Defensive Back':
            playerInfo['Skills']['Physical']['Strength'] = skillRange('h')
            playerInfo['Skills']['Physical']['Speed'] = skillRange('h')
            playerInfo['Skills']['Physical']['Endurance'] = skillRange('h')
            playerInfo['Skills']['Defense']['Pass Coverage'] = skillRange('h')
            playerInfo['Skills']['Defense']['Tackling'] = skillRange('h')
            playerInfo['Skills']['Defense']['Pass Rushing'] = skillRange('h')
            playerInfo['Skills']['Defense']['Run Stopping'] = skillRange('h')
            playerInfo['Skills']['Rushing/Receiving']['Hands'] = skillRange('h')
        elif position == 'Kicker':
            playerInfo['Skills']['Kicking']['Kick Power'] = skillRange('h')
            playerInfo['Skills']['Kicking']['Kick Accuracy'] = skillRange('h')
            playerInfo['Skills']['Kicking']['Punt Power'] = skillRange('h')
            playerInfo['Skills']['Kicking']['Punt Accuracy'] = skillRange('h')
        elif position == 'Punter':
            playerInfo['Skills']['Kicking']['Kick Power'] = skillRange('h')
            playerInfo['Skills']['Kicking']['Kick Accuracy'] = skillRange('h')
            playerInfo['Skills']['Kicking']['Punt Power'] = skillRange('h')
            playerInfo['Skills']['Kicking']['Punt Accuracy'] = skillRange('h')

        skillsAssigned = True

        addSkillPoints = 0
        overallRating = 0
        for i in playerInfo['Skills']:
            if (i != 'Overall Rating' and i != 'Max Rating'):
                for j, num in playerInfo['Skills'][i].items():
                    addSkillPoints += num
        overallRating = round(((addSkillPoints / 2000) * 100))
        test.append(overallRating)
        playerInfo['Skills']['Overall Rating'] = overallRating

    ranPotential = random.randint(0, 3)
    if (ranPotential == 0):
        playerInfo['Apperence']['Potential Rating'] = 'Good'
        playerInfo['Apperence']['Potential Rating Num'] = random.randint(75,80)
    if (ranPotential == 1):
        playerInfo['Apperence']['Potential Rating'] = 'Professional'
        playerInfo['Apperence']['Potential Rating Num'] = random.randint(81,85)
    if (ranPotential == 2):
        playerInfo['Apperence']['Potential Rating'] = 'High'
        playerInfo['Apperence']['Potential Rating Num'] = random.randint(86,90)
    if (ranPotential == 3):
        playerInfo['Apperence']['Potential Rating'] = 'Very High'
        playerInfo['Apperence']['Potential Rating Num'] = random.randint(91,99)


    players[pid] = playerInfo
    
    # FOR ARTIST
    
    artistList[pid] = {
        'Player Information' : {
            'Name' : playerInfo['Name'],
            'Team' : league,
            'Position' : playerInfo['LeagueInformation']['position'],
            'Jersey Number' : playerInfo['LeagueInformation']['jerseyNumber'],
            'Skin Tone' : playerInfo['Apperence']['skinColor'],
            'Eye Color' : playerInfo['Apperence']['eyeColor'],
            'Eye Black' : playerInfo['Apperence']['eyeBlack'],
            'Mouth Style' : playerInfo['Apperence']['mouthStyle'],
            'Face Mask' : playerInfo['Apperence']['facemaskType'],
            'Glove Color' : playerInfo['Apperence']['gloveColor'],
            'Sock Height' : playerInfo['Apperence']['sockHeight'],
            'Cleat Type' : playerInfo['Apperence']['cleatType'],
            'Fit Type' : playerInfo['Apperence']['fitType']
        },
        'Player Skills' : playerInfo['Skills'],
        'Potential Rating' : playerInfo['Apperence']['Potential Rating'],
        'Potential Rating Value' : playerInfo['Apperence']['Potential Rating Num']
    }



# SHIT TO DO FOR ARTIST
#  POTENTIAL RATING ALGORITHM
#  ADD CUSTON NAMES
#  RUN AT FULL PLAYER COUNT
#  MAKE COACH LIST





with open("artistList.json", "w") as outfile:
    json.dump(artistList, outfile)
    print('\n*****************************************************************')
    print('***** astist json dump complete, refer to "artistList.json" *****')
    print('*****************************************************************\n') 


# CLEANED PLAYER DATA



with open("players.json", "w") as outfile:
    json.dump(players, outfile)
    print('\n*******************************************************')
    print('***** json dump complete, refer to "players.json" *****')
    print('*******************************************************\n') 
