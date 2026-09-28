# DVM Backend Task 2 - Last.fm Music API

This project was made as part of the Department of Visual Media (DVM) backend recruitment task at BITS Pilani.

The project is a simple Django application that uses the Last.fm API to retrieve music-related information.

The application returns the retrieved information in JSON format.

## Features

- View the top artists of a particular country
- View the top tracks of a particular country
- Search for artists
- Search for albums
- Search for tracks
- Retrieve music information using the Last.fm API
- Return the retrieved data in JSON format

## Additional Feature - Artist Top Tracks

The additional feature I implemented allows users to retrieve the top tracks of a particular artist.

The application takes the artist's name and uses the Last.fm API to retrieve their most popular tracks.

For example:

`/artist-top-tracks/?artist=Coldplay`

This uses the `artist.getTopTracks` method provided by the Last.fm API.

## Running the Project

Install the required packages:

`pip install -r requirements.txt`

Set your Last.fm API key:

`$env:LASTFM_API_KEY="YOUR_API_KEY"`

Run the Django development server:

`python manage.py runserver`

Then open:

`http://127.0.0.1:8000/`

## Example Endpoints

Top artists in India:

`/top-artists/India/`

Top tracks in India:

`/top-tracks/India/`

Search for an artist:

`/search/artist/?name=Coldplay`

Search for an album:

`/search/album/?name=Parachutes`

Search for a track:

`/search/track/?name=Yellow`

Top tracks of an artist:

`/artist-top-tracks/?artist=Coldplay`

## Technologies Used

- Python
- Django
- Requests
- Last.fm API
- JSON