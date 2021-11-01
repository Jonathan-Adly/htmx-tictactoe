from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def change_player(request):
    if request.user.player == "X":
        request.user.player = "O"
    else:
        request.user.player = "X"

    request.user.save()
    return render(request, "components/game_info.html")
