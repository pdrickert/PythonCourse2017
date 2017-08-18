import tweepy
import time

#Check the documentation page
#http://docs.tweepy.org/en/v3.2.0/
#Get access to API
auth = tweepy.OAuthHandler('consumer', 'secret')
auth.set_access_token('access', 'secret')
api = tweepy.API(auth)

AlabamaPoliSci = api.get_user('AlabamaPSC')

def MostActiveFollower(name):
    UserName = []
    StatusNum = []
    FollowerIDs = name.followers_ids()
    for follower_id in FollowerIDs:
        user = api.get_user(follower_id)
        StatusNum.append(user.statuses_count)
        UserName.append(user.screen_name.encode('UTF-8'))
    m = max(StatusNum)
    BestFollowerIndex = [i for i, j in enumerate(StatusNum) if j == m][0]
    MostActiveUser = UserName[BestFollowerIndex]
    MostActiveTweets = StatusNum[BestFollowerIndex]
    return "The most active follower of this account is %s with %s tweets. Boy, that's a lot!" %(MostActiveUser, MostActiveTweets)

def MostPopularFollower(name):
    UserName = []
    FollowersNum = []
    FollowerIDs = name.followers_ids()
    for follower_id in FollowerIDs:
        user = api.get_user(follower_id)
        FollowersNum.append(user.followers_count)
        UserName.append(user.screen_name.encode('UTF-8'))
    m = max(FollowersNum)
    PopularFollowerIndex = [i for i, j in enumerate(FollowersNum) if j == m][0]
    MostPopularUser = UserName[PopularFollowerIndex]
    MostPopularFollowers = FollowersNum[PopularFollowerIndex]
    return "The most popular follower of this account is %s with %s followers. What a cool person!" %(MostPopularUser, MostPopularFollowers)

def MostActiveByType(name):
    UserName = []
    StatusNum = []
    FollowerIDs = name.followers_ids()
    for follower_id in FollowerIDs:
        user = api.get_user(follower_id)
        StatusNum.append(user.statuses_count)
        UserName.append(user.screen_name.encode('UTF-8'))
    m = max(StatusNum)
    BestFollowerIndex = [i for i, j in enumerate(StatusNum) if j == m][0]
    MostActiveUser = UserName[BestFollowerIndex]
    MostActiveTweets = StatusNum[BestFollowerIndex]
    return "The most active follower of this account is %s with %s tweets. Boy, that's a lot!" %(MostActiveUser, MostActiveTweets)
