from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from accounts.models import CustomUser


def home(request):
    return render(request, "home.html")


@login_required
def change_player(request):
    if request.user.player == "X":
        request.user.player = "O"
    else:
        request.user.player = "X"

    request.user.save()
    return render(request, "components/game_info.html")


@require_POST
@login_required
def play(request):
    if request.user.player == "X":
        player = 1
    else:
        player = 2
    row = int(request.POST["row"])
    col = int(request.POST["col"])
    request.user.board[row][col] = player
    request.user.save()
    return render(request, "components/square.html")


@login_required
def reset(request):
    request.user.board = CustomUser.get_default()
    request.user.player = "X"
    request.user.save()
    return redirect("home")
