from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def admin_page_login(request):
    if request.method == 'GET':
        # 사용자 로그인 확인
        if request.user.is_authenticated:
            return redirect("/")
        else: return render(request, "login.html")

    elif request.method == 'POST':
        username = request.POST.get("id", None)
        password = request.POST.get("password", None)

        true_user = auth.authenticate(request, username=username, password=password)
        if true_user is not None:
            auth.login(request, true_user)
            return redirect("/")
        else:
            return render(request, "login.html", {"error": "ID 또는 password 확인해 주세요!"})
    else:
        return redirect("/")


@login_required
def admin_page_logout(request):
    auth.logout(request)
    return redirect('/')
