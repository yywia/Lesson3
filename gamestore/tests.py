from django.test import TestCase
from django.urls import reverse

from gamestore import factories, models

# Create your tests here.
class GameStoreTestCase(TestCase):
    def setUp(self):
        self.game = factories.GameFactory()

    def test_get_game_list(self):
        url = reverse('games_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['games'].count(), models.Game.objects.count())

    def test_get_book_detail(self):
        url = reverse('games_detail', kwargs={'pk': self.game.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_game(self):
        url = reverse('games_update', kwargs={'pk': self.game.pk})
        old_title = self.game.title
        old_description = self.game.description
        response = self.client.post(url, {'title': 'new_title'})
        self.game.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(self.game.title, old_title)

    def test_delete_game(self):
        url = reverse('games_delete', kwargs={'pk': self.game.pk})
        old_game_count = models.Game.objects.count()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertGreater(old_game_count, models.Game.objects.count())

    def test_create_game(self):
        url = reverse('game_create')
        old_game_count = models.Game.objects.count()
        response = self.client.post(url, {'title': 'new_title'})
        self.assertEqual(response.status_code, 200)
