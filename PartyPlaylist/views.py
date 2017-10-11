from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login

import math

#spotipy imports
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

# Create your views here.
def main(request):
    return render(request, 'PartyPlaylist/main.html')

@login_required
def activate(request):
    client_id = "003d00b69efd44078d62af0fdd5fd81f"
    client_secret = "710ac58f230a4245a13064f9e527257b"
    redirect_uri = "http://127.0.0.1:8000/party"
    scope = 'user-library-read'
    username = 'dasein_kapital'
    sp = spotipy.Spotify()
    number = request.GET.get('number', 0)
    if number != 0:
        offset = ((int(number) - 1) * 50)
    else:
        offset = 0
    token = util.prompt_for_user_token(username, scope=scope, redirect_uri=redirect_uri, client_id=client_id, client_secret=client_secret)
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_playlists(offset=offset)
        playlists = []
        total_playlists = results['total']
        max_pagnation = math.ceil(total_playlists / 50) + 1
        numbers = list(range(1, max_pagnation))
        context = {'offset':0, 'prev_hidden':True, 'numbers':numbers}
        if total_playlists > 50:
            context.update({'next_hidden':False})
        if offset > 50:
            context.update({'prev_hidden':False})
        if (total_playlists-offset) < 50:
            context.update({'next_hidden':True})
        for item in results['items']:
            playlist_name = item['name']
            playlist_id = item['id']
            playlists.append(playlist_name + ' - ' + playlist_id)
        context.update({'playlists':playlists})
        return render(request, 'PartyPlaylist/activate.html', context)
    else:
        return render(request, 'PartyPlaylist/fail.html')

def log(request):
    pass