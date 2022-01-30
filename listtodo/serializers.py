from rest_framework import serializers, parsers
from .models import Tweet,Users,Following
class TweetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('id','desc', 'tweetedby','tweetedon','img')
        # {'id': 1643458470884, 'desc': 'myname is khan', 'tweetedby': 1643452956461, 'tweetedon': 1643458470}
class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id','username','password','userfullname','useremail','usern_mobile_no','profile_pic')
class FollowingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = ('id','userid','followedby')
        #{'id':id,'UsersSerializers':userid,'followedby' :followeeid}