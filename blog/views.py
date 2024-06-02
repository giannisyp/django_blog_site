from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.

all_posts = [
    {
        "slug" : "hike-in-the-mountains",
        "image" : "mountains.jpg" , 
        "author" : "Giannis" ,
        "date" : date(2021,7,21), 
        "title" : "Mountain Hiking",
        "excerpt" : "Theres nothing like the views you get when hiking in the mountains",
        "content" : """
                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Non reprehenderit minima cumque sed temporibus sequi in! Accusamus at, quo fugit nam, eaque voluptates voluptas quidem, sit quae unde magnam veritatis?

        """
    },
    {
        "slug" : "woods",
        "image" : "woods.jpg" , 
        "author" : "Giannis" ,
        "date" : date(2021,7,21), 
        "title" : "Woods are Great",
        "excerpt" : "Theres nothing like the views you get when hiking in the mountains",
        "content" : """
                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Non reprehenderit minima cumque sed temporibus sequi in! Accusamus at, quo fugit nam, eaque voluptates voluptas quidem, sit quae unde magnam veritatis?

        """
    },
    {
        "slug" : "programming",
        "image" : "coding.jpg" , 
        "author" : "Giannis" ,
        "date" : date(2021,7,21), 
        "title" : "Programming Programming Programming",
        "excerpt" : "Theres nothing like the views you get when hiking in the mountains",
        "content" : """
                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Non reprehenderit minima cumque sed temporibus sequi in! Accusamus at, quo fugit nam, eaque voluptates voluptas quidem, sit quae unde magnam veritatis?

        """
    }
]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts , key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts" : latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts" : all_posts
    }) 

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post" : identified_post
    })