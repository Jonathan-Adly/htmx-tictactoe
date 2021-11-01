from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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
