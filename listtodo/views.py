
from datetime import datetime
import time
import json
import jwt
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import TweetSerializers,UsersSerializers,FollowingSerializers
from .models import Following,Users,Tweet
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
def getid():
    time.sleep(0.001)
    return int(datetime.now().timestamp() * 1000)

@csrf_exempt
@api_view(["POST","GET"])
def home(request):
    try:
        authtoken = request.data['authtoken']
        if authtoken !='':
            userData = jwt.decode(authtoken, "encryption_key_for_hash", algorithms=["HS256"])
            usr = user(userData['user'])
            recentTweet = usr.getRecentPost()
            allProfile = usr.allUser()
        return JsonResponse([recentTweet,allProfile], safe=False)
    except Exception as e:
        return JsonResponse(json.dumps({"status":"fail","msg":"Please Login Again"}), safe=False)


@csrf_exempt
@api_view(["POST","GET"])
def signin(request):
    try:
        username = request.data['userid']
        password = request.data['password']
        #usr = user(username=username,password=username,useremail=None,usern_mobile_no=None,)
        passwo = Users.objects.all().filter(username=username)[0]
        if passwo:
            if passwo.password == password:
                new_token = jwt.encode(
                    payload={"id": passwo.id, "user": username},
                    key="encryption_key_for_hash",
                    algorithm="HS256"
                )
                return JsonResponse( json.dumps({"status":new_token}), safe=False)
            return JsonResponse( json.dumps({"status":"fail"}), safe=False)
    except Exception as e:
        exit()


@csrf_exempt
@api_view(["POST","GET"])
def signup(request):
    try:
        username =request.data['username']
        password = request.data['password']
        useremail = request.data['email']
        usern_mobile_no =request.data['usern_mobile_no']
        userfullname  =request.data['userfullname']
        pic = request.data['profile_pic']
        usr = user(username,password,useremail,usern_mobile_no,userfullname,pic = pic)
        return JsonResponse( json.dumps({"status":"success"}), safe=False)
    except Exception as e:
        return HttpResponse("some error occured")

@csrf_exempt
@api_view(["POST","GET"])
def dotweet(request):
    try:
        authtoken = request.data['authtoken']
        if authtoken !='':
            userData = jwt.decode(authtoken, "encryption_key_for_hash", algorithms=["HS256"])
            usr = user(userData['user'])
            usr.post(request.data['desc'],request.data['tweeting'])
            return JsonResponse( json.dumps({"status":"success"}), safe=False)
        else:
            return JsonResponse(json.dumps({"status": "fail"}), safe=False)
    except Exception as e:
        return HttpResponse("some error occured")

@csrf_exempt
@api_view(["POST","GET"])
def dofollow(request):
    try:
        authtoken = request.data['authtoken']
        if authtoken !='':
            userData = jwt.decode(authtoken, "encryption_key_for_hash", algorithms=["HS256"])
            usr = user(userData['user'])
            usr.follow(request.data['id'])
            return JsonResponse( json.dumps({"status":"success"}), safe=False)
        else:
            return JsonResponse(json.dumps({"status": "fail"}), safe=False)
    except Exception as e:
        return HttpResponse("some error occured")

class user:
    def __init__(self ,username,password=None,useremail=None,usern_mobile_no=None,userfullname = None,pic = None):
        try:
            id = getid()
            if userfullname != None and password !=None: # sign in
                json_obj = {'id':id,'username':username,'userfullname': userfullname, 'password': password,'useremail': useremail, 'usern_mobile_no': usern_mobile_no,'profile_pic':pic}
                todo_serialize = UsersSerializers(data=json_obj)
                if todo_serialize.is_valid():
                    todo_serialize.save()
                self.username = username
                self.userfullname = userfullname
                self.password = password
                self.useremail = useremail
                self.username = username
                self.usern_mobile_no = usern_mobile_no
            else:
                self.id = (Users.objects.all().filter(username=username)[0]).id
                self.username = username
        except Exception as e:
            print(e)


    def follow(self,followeeid):
        try:
            id  = getid()
            json_obj = {'id':id,'userid':self.id,'followedby' :followeeid}
            followrequest = FollowingSerializers(data = json_obj)
            if followrequest.is_valid(raise_exception=True):
                followrequest.save()
                print("yes")
            else:
                print("no")
        except Exception as e:
            print(e)
    def post(self,desc,img):
        tweetpost = Tweets(desc,self.id,img)

    def getRecentPost(self):
        try:
            rs=  Following.objects.all().filter(userid=self.id)
            following =set()
            for row in rs:
                following.add(row.followedby)
            post =Tweet.objects.all().filter(tweetedby__in = following).order_by('tweetedon').reverse()
            ans =[]
            for row in post:
                ans.append({
                    'id':row.id,
                    'desc':row.desc,
                    'img' :str(row.img),
                    'tweetedby':row.tweetedby,
                    'username' : Users.objects.all().filter(id = row.tweetedby)[0].username,
                    'date':row.tweetedon
                })

            print(ans)
            # todo_serializers = TweetSerializers(post, many=True)
            # return JsonResponse(json.dumps({"row":todo_serializers.data}), safe=False)
            return ans
        except Exception as e:
            print(e)
    def allUser(self):
        try:
            rs=  Users.objects.all()
            ans = []
            for row in rs:
                ans.append({
                    'id': row.id,
                    'username': row.username,
                    'img': str(row.profile_pic)
                })
            return ans
        except Exception as e:
            raise Exception

class Tweets:
    try:
        def __init__(self,desc,userid,img):
            self.description = desc;
            self.timestamp = datetime.time
            self.twittedby  = userid
            id = getid()
            now = int(time.time())
            json_obj = {'id':id,'desc':desc, 'tweetedby' :userid,'tweetedon':int(time.time()),'img':img  }
            todo_serialize = TweetSerializers(data =json_obj )
            try:
                    if  todo_serialize.is_valid(raise_exception=True):
                        todo_serialize.save()
                        print("tweeted")
                    else:
                        print("no")
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)





