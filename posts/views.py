from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegistrationForm, LoginForm, BlogPostForm
from .models import BlogPost


def register(request):
    # String used to show a message to the user if any error occurs
    msg = ""

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("posts:login")
            except IntegrityError:
                msg = "Email already in use"
        else:
            msg = "Invalid registration fields"

    form = RegistrationForm()
    return render(request, "posts/register.html", {"form": form, "msg": msg})


def login_view(request):
    # String used to show a message to the user if any error occurs
    msg = ""

    # If user is already logged in, we can avoid showing them the login page
    if request.user.is_authenticated:
        return redirect("posts:home")

    # If trying to login (via POST), validate form and user
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("posts:home")
            else:
                msg = "Incorrect user or password"

    # Else (via GET), render the login page and form
    form = LoginForm()
    return render(request, "posts/login.html", {"form": form, "msg": msg})


def logout_view(request):
    logout(request)
    return redirect("posts:login")


@login_required
def home(request):
    posts = BlogPost.objects.order_by("-date_posted")

    # Paginate the results
    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    data = {"posts": posts, "user": request.user, "page_obj": page_obj}
    return render(request, "posts/home.html", data)


@login_required
def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

    return redirect("posts:home")


@login_required
def detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    data = {"post": post, "user": request.user}
    return render(request, "posts/detail.html", data)


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    # Only admin users can delete a post, so check it
    if request.user.role == "admin":
        post.delete()
    return redirect("posts:home")
