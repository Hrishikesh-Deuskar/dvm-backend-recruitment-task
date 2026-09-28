# DVM Backend Task 1 - Django Polls App

This project was made as part of the Department of Visual Media (DVM) backend recruitment task at BITS Pilani.

The project is based on the official Django Polls tutorial. It is a simple polling application where users can view polls, vote for one of the available choices, and view the results.

As an additional feature, I added **categories for polls**, which allow polls to be grouped and viewed based on their category.

## Features

- View the latest polls
- Vote on a poll
- View the results of a poll
- Manage questions and choices using the Django admin page
- Categorize polls into different categories
- View all polls belonging to a particular category

## Additional Feature - Poll Categories

The additional feature I implemented is a category system for polls.

Examples of categories include:

- Sports
- Technology
- Movies
- College
- Other

# DVM Backend Task 2 - Last.fm Music API

This project was made as part of the Department of Visual Media (DVM) backend recruitment task at BITS Pilani.

The project is a simple Django application that uses the Last.fm API to retrieve music-related information. It allows users to view popular artists and tracks from different countries and search for artists, albums, and tracks.

The data is fetched from the Last.fm API and returned in JSON format.

## Features

- View the top artists of a particular country
- View the top tracks of a particular country
- Search for artists
- Search for albums
- Search for tracks
- Retrieve music data using the Last.fm API
- Return the retrieved data in JSON format
- View the top tracks of a particular artist

## Additional Feature - Artist Top Tracks

The additional feature I implemented allows users to search for the top tracks of a particular artist.

The application takes the artist's name and uses the Last.fm API to retrieve their most popular tracks.

For example, a user can request the top tracks of an artist such as:

- Coldplay
- Ed Sheeran
- Taylor Swift
- The Weeknd

The results are returned in JSON format, similar to the other features of the application.

This feature uses the `artist.getTopTracks` method provided by the Last.fm API.