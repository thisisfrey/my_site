from django.shortcuts import render
from .data import all_posts


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/posts.html",
                  {"all_posts": all_posts}
                  )


def post(request, slug):
    identified_post = next(p for p in all_posts if p['slug'] == slug)
    return render(request, "blog/post.html", {"post": identified_post})
