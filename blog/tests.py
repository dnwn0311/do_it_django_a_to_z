from django.test import TestCase

def test_search(self):
    post_about_python = Post.objects.create(
        title='파이썬에 대한 포스트입니다.',
        content='Hello World. We are the world.',
        author=self.user_trump
    )

    response = self.client.get('/blog/search/파이썬/')
    self.assertEqual(response.status_code, 200)
    soup = BeautifulSoup(response.content, 'html.parser')

    main_area = soup.find('div', id='main-area')

    self.assertIn('Search: 파이썬 (2)', main_area.text)
    self.assertNotIn(self.post_001.title, main_area.text)
    self.assertNotIn(self.post_002.title, main_area.text)
    self.assertIn(self.post_002.title, main_area.text)
    self.assertIn(self_about_python.title, main_area.text)

