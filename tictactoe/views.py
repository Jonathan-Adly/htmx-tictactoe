from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from accounts.models import CustomUser
from .utils import computer_move, check_status


def home(request):
    """
    If game didn't start, we will render home.html.
    If game did start and user hits refresh, we need to update the game status.
    """
    status = check_status(request.user.board)
    return render(request, "home.html", {"status": status})


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
    status = check_status(request.user.board)
    if status == "X" or status == "O":
        game_won = True
    else:
        game_won = False
    response = render(
        request, "components/board.html", {"user_played": True, "game_won": game_won}
    )
    response["HX-Trigger"] = "checkGameStatus"
    return response


@login_required
def computer_play(request):
    # the computer move
    computer_move(request.user)
    status = check_status(request.user.board)
    if status == "X" or status == "O":
        game_won = True
    else:
        game_won = False
    response = render(
        request, "components/board.html", {"user_played": False, "game_won": game_won}
    )
    response["HX-Trigger"] = "checkGameStatus"
    return response


@login_required
def reset(request):
    request.user.board = CustomUser.get_default()
    request.user.player = "X"
    request.user.save()
    return redirect("home")


def game_status(request):
    """
    we hit this view on each move to check what is the game status.
    The game could a new game, in progress, finished with a winner or finished with a tie.
    """
    status = check_status(request.user.board)
    if status == "X" or status == "Y":
        status = f"The {status} Player have won the game!"
    return render(
        request,
        "components/game_info.html",
        {"status": status},
    )
