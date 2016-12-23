from django.shortcuts import render
from . import models
# Create your views here.
def index(req):
    # users = models.Users.objects.all()
    # users = models.Users.objects.filter(last_name="Rodriguez")
    # users = models.Users.objects.exclude(last_name="Rodriguez")
    # users = models.Users.objects.filter(last_name="Rodriguez").filter(first_name="Daniel")
    # users = models.Users.objects.filter(last_name="Rodriguez").exclude(first_name="Madison")
    # users = models.Users.objects.exclude(first_name="Daniel").exclude(first_name="Michael")

    # users = models.Users.objects.get(id=1)
    # 'Users' object has no attribute 'query' - comment print users.query
    # 'Users' object is not iterable - comment out for loop in index.html, change user to users to print

    # users = models.Users.objects.get(last_name="Rodriguez")
    # get() returned more than one Users -- it returned 3!

    # users = models.Users.objects.get(id=10000)
    # Users matching query does not exist.

    # users = models.Users.objects.all().order_by('first_name')
    # users = models.Users.objects.all().order_by('-last_name')


    # friendships = models.Friendships.objects.all()
    # friendships = models.Friendships.objects.filter(user=4)
    # friendships = models.Friendships.objects.filter(friend=4)
    # users = models.objects.get(id=4)
    # friendships = models.Friendships.objects.exclude(user=4).exclude(user=5).exclude(user=6)
    # friendships = models.Friendships.objects.all().order_by('user')

    # friendships = models.Friendships.objects.filter(user__first_name="Michael")
    # friendships = models.Friendships.objects.exclude(user__first_name="Daniel").exclude(friend__first_name="Daniel")
    # friendships = models.Friendships.objects.filter(friend__id=1)
    # print friendships.query

    friendships = models.Friendships.objects.filter(user__id=1) | models.Friendships.objects.filter(user__last_name="Hernandez")
    # friendships = models.Friendships.objects.filter(user__id=1) | models.Friendships.objects.filter(friend__last_name="Hernandez").order_by("user__last_name")
    # distinct()
    # Cannot combine a unique query with a non-unique query.

    # users = models.Users.objects.filter(usersfriend__friend__id=2)
    # models.Users.objects.filter(usersfriend__user__id=1) |
    users = models.Users.objects.filter(usersfriend__user__id=1) | models.Users.objects.filter(usersfriend__friend__last_name="Hernandez")
    # models.Users.objects.filter(usersfriend__user__last_name="Hernandez")
    print (users.query)
    # for user in users:
    #     for friendship in user.usersfriend.all:
    #         print friendship.friend.first_name
        # print user.first_name
    # print users.query
    # print users
    # context = {'users':users}
    context = {
        'users' : users,
        'friends':friendships,
        # 'friends2':friendships2,
        # 'friends3':friendships3,
        }
    return render(req, "friendapp/index.html",context)
