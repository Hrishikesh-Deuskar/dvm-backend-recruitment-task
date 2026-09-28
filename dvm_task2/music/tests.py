from django.test import TestCase


class MusicURLTests(TestCase):

    def test_home_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)


    def test_artist_search_without_name(self):
        response = self.client.get("/search/artist/")

        self.assertEqual(response.status_code, 400)


    def test_album_search_without_name(self):
        response = self.client.get("/search/album/")

        self.assertEqual(response.status_code, 400)


    def test_track_search_without_name(self):
        response = self.client.get("/search/track/")

        self.assertEqual(response.status_code, 400)


    def test_artist_top_tracks_without_artist(self):
        response = self.client.get("/artist-top-tracks/")

        self.assertEqual(response.status_code, 400)