import tweepy
import time

#Check the documentation page
#http://docs.tweepy.org/en/v3.2.0/
#Get access to API
auth = tweepy.OAuthHandler('consumer', 'secret')
auth.set_access_token('access', 'secret')
api = tweepy.API(auth, wait_on_rate_limit = True)

BamaPoliSci = api.get_user('AlabamaPSC')

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

MostActiveFollower(BamaPoliSci)

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

MostPopularFollower(BamaPoliSci)

def MostActiveByType(name):
    CelebrityUserName = []
    ExpertUserName = []
    LaymanUserName = []
    CelebrityStatusNum = []
    ExpertStatusNum = []
    LaymanStatusNum = []
    FriendIDs = api.friends_ids(name.screen_name)
    for friend_id in FriendIDs:
        user = api.get_user(friend_id)
        if user.followers_count > 1000:
            CelebrityStatusNum.append(user.statuses_count)
            CelebrityUserName.append(user.screen_name.encode('UTF-8'))
        elif user.followers_count > 100:
            ExpertStatusNum.append(user.statuses_count)
            ExpertUserName.append(user.screen_name.encode('UTF-8'))
        else:
            LaymanStatusNum.append(user.statuses_count)
            LaymanUserName.append(user.screen_name.encode('UTF-8'))
    m1 = max(CelebrityStatusNum)
    m2 = max(ExpertStatusNum)
    m3 = max(LaymanStatusNum)
    ActiveCelebrityIndex = [i for i, j in enumerate(CelebrityStatusNum) if j == m1][0]
    ActiveExpertIndex = [i for i, j in enumerate(ExpertStatusNum) if j == m2][0]
    ActiveLaymanIndex = [i for i, j in enumerate(LaymanStatusNum) if j == m3][0]
    MostActiveCeleb = CelebrityUserName[ActiveCelebrityIndex]
    CelebTweets = CelebrityStatusNum[ActiveCelebrityIndex]
    MostActiveExpert = ExpertUserName[ActiveExpertIndex]
    ExpertTweets = ExpertStatusNum[ActiveExpertIndex]
    MostActiveLayman = LaymanUserName[ActiveLaymanIndex]
    LaymanTweets = LaymanStatusNum[ActiveLaymanIndex]
    print "The most active celebrity friend of this account is %s with %s tweets." %(MostActiveCeleb, CelebTweets)
    print "The most active expert friend of this account is %s with %s tweets." %(MostActiveExpert, ExpertTweets)
    print "The most active layman friend of this account is %s with %s tweets." %(MostActiveLayman, LaymanTweets)

MostActiveByType(BamaPoliSci)

def MostPopularFriend(name):
        UserName = []
        FriendsNum = []
        FriendIDs = api.friends_ids(name.screen_name)
        for friend_id in FriendIDs:
            user = api.get_user(friend_id)
            FriendsNum.append(user.friends_count)
            UserName.append(user.screen_name.encode('UTF-8'))
        m = max(FriendsNum)
        PopularFriendIndex = [i for i, j in enumerate(FriendsNum) if j == m][0]
        MostPopularUser = UserName[PopularFriendIndex]
        MostPopularFriend = FriendsNum[PopularFriendIndex]
        return "The most popular friend of this account is %s with %s followers. What a cool person!" %(MostPopularUser, MostPopularFriend)

MostPopularFriend(BamaPoliSci)

## 2nd Degree

def MostActiveFollower2Deg(name):
    Deg1Followers = []
    UserName = []
    StatusNum = []
    FollowerIDs = name.followers_ids()
    for follower_id in FollowerIDs:
        user = api.get_user(follower_id)
        if user.followers_count > 1000:
            pass
        else:
            Deg1Followers.append(user.id)
            StatusNum.append(user.statuses_count)
            UserName.append(user.screen_name.encode('UTF-8'))
    for follower in Deg1Followers:
        user = api.get_user(follower)
        if user.followers_count > 1000:
            pass
        else:
            StatusNum.append(user.statuses_count)
            UserName.append(user.screen_name.encode('UTF-8'))
    m = max(StatusNum)
    BestFollowerIndex = [i for i, j in enumerate(StatusNum) if j == m][0]
    MostActiveUser = UserName[BestFollowerIndex]
    MostActiveTweets = StatusNum[BestFollowerIndex]
    return "The most active follower or follower of followers of this account is %s with %s tweets. Boy, that's a lot!" %(MostActiveUser, MostActiveTweets)

MostActiveFollower2Deg(BamaPoliSci)

def MostActiveFriend2Deg(name):
    Deg1Friends = []
    UserName = []
    StatusNum = []
    FriendIDs = api.friends_ids(name.screen_name)
    for friend_id in FriendIDs:
        user = api.get_user(friend_id)
        if user.friends_count > 1000:
            pass
        else:
            Deg1Friends.append(user.id)
            StatusNum.append(user.statuses_count)
            UserName.append(user.screen_name.encode('UTF-8'))
    for friend in Deg1Friends:
        user = api.get_user(friend)
        if user.friends_count > 1000:
            pass
        else:
            StatusNum.append(user.statuses_count)
            UserName.append(user.screen_name.encode('UTF-8'))
    m = max(StatusNum)
    BestFriendIndex = [i for i, j in enumerate(StatusNum) if j == m][0]
    MostActiveUser = UserName[BestFriendIndex]
    MostActiveTweets = StatusNum[BestFriendIndex]
    return "The most active friend or friend of friends of this account is %s with %s tweets. Boy, that's a lot!" %(MostActiveUser, MostActiveTweets)

MostActiveFriend2Deg(BamaPoliSci)
