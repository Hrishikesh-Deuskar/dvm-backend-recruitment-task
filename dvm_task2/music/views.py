import os
import requests

from django.http import JsonResponse


API_KEY = os.environ.get("LASTFM_API_KEY")
BASE_URL = "https://ws.audioscrobbler.com/2.0/"

HEADERS = {
    "User-Agent": "DVM-Backend-Recruitment-Task"
}

def call_lastfm(params):

    # Check whether the API key exists
    if not API_KEY:
        return {
            "error": "LASTFM_API_KEY is not set."
        }

    # Add the API key and JSON format
    params["api_key"] = API_KEY
    params["format"] = "json"

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            headers=HEADERS,
            timeout=10,
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException as error:
        return {
            "error": "Could not connect to Last.fm.",
            "details": str(error),
        }

def home(request):

    return JsonResponse({
        "message": "DVM Last.fm API",
        "endpoints": {
            "top_artists":
                "/top-artists/India/",

            "top_tracks":
                "/top-tracks/India/",

            "search_artist":
                "/search/artist/?name=Coldplay",

            "search_album":
                "/search/album/?name=Parachutes",

            "search_track":
                "/search/track/?name=Yellow",

            "artist_top_tracks":
                "/artist-top-tracks/?artist=Coldplay",
        }
    })

def top_artists(request, country):

    data = call_lastfm({
        "method": "geo.gettopartists",
        "country": country,
        "limit": 10,
    })

    return JsonResponse(data)

def top_tracks(request, country):

    data = call_lastfm({
        "method": "geo.gettoptracks",
        "country": country,
        "limit": 10,
    })

    return JsonResponse(data)

def search_artist(request):

    artist_name = request.GET.get("name")

    if not artist_name:
        return JsonResponse({
            "error": "Please provide an artist name."
        }, status=400)

    data = call_lastfm({
        "method": "artist.search",
        "artist": artist_name,
        "limit": 10,
    })

    return JsonResponse(data)

def search_album(request):

    album_name = request.GET.get("name")

    if not album_name:
        return JsonResponse({
            "error": "Please provide an album name."
        }, status=400)

    data = call_lastfm({
        "method": "album.search",
        "album": album_name,
        "limit": 10,
    })

    return JsonResponse(data)

def search_track(request):

    track_name = request.GET.get("name")

    if not track_name:
        return JsonResponse({
            "error": "Please provide a track name."
        }, status=400)

    data = call_lastfm({
        "method": "track.search",
        "track": track_name,
        "limit": 10,
    })

    return JsonResponse(data)

def artist_top_tracks(request):

    artist_name = request.GET.get("artist")

    if not artist_name:
        return JsonResponse({
            "error": "Please provide an artist name."
        }, status=400)

    data = call_lastfm({
        "method": "artist.gettoptracks",
        "artist": artist_name,
        "limit": 10,
    })

    return JsonResponse(data)