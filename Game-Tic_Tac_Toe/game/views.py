from django.shortcuts import render, redirect
from django.contrib import messages
from game.models import Room

# Vue pour la page d'accueil
def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    elif request.method == "POST":
        roomId = request.POST.get("room-id", None)
        playerName = request.POST.get("player-name", "Unknown Player").strip()

        # Nettoyer le nom du joueur
        if not playerName or "/" in playerName:
            playerName = "Unknown_Player"

        if roomId:
            try:
                room = Room.objects.get(id=roomId)
                return redirect(f"/game/{room.id}/{playerName}/")
            except Room.DoesNotExist:
                messages.error(request, "Room does not exist.")
                return redirect("/")
        else:
            room = Room.objects.create()
            return redirect(f"/game/{room.id}/{playerName}/")


# Vue pour le jeu
def game(request, id=None, name=None):
    if not id or not name:
        messages.error(request, "Invalid game parameters.")
        return redirect("/")
    
    try:
        room = Room.objects.get(id=id)
        return render(request, "game.html", {"room": room, "name": name})
    except Room.DoesNotExist:
        messages.error(request, "Room does not exist.")
        return redirect("/")
