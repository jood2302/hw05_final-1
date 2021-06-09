from django.contrib.auth import get_user_model
from django.test import TestCase

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class ModelsStrTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_user = User.objects.create_user(
            username='Toster'
        )
        cls.test_commentator = User.objects.create_user(
            username='Commenter'
        )

        cls.test_group = Group.objects.create(
            title='Title test group',
            description='Description test group'
        )
        cls.test_post = Post.objects.create(
            text='Самый тестовый из постов',
            author=cls.test_user
        )
        cls.test_comment = Comment.objects.create(
            post=cls.test_post,
            author=cls.test_commentator,
            text='Новый комментарий для тестового поста'
        )
        cls.test_follow = Follow.objects.create(
            user=cls.test_commentator,
            author=cls.test_user
        )

        cls.test_model_response = (
            (cls.test_group, cls.test_group.title),
            (cls.test_post, cls.test_post.text[:15]),
            (cls.test_comment,
             f'{cls.test_comment.author.username[:15]} '
             f'{cls.test_comment.text[:20]}'),
            (cls.test_follow,
             f'Подписчик {cls.test_commentator.username[:15]}'
             f' на автора {cls.test_user.username[:15]}')
        )

    def test_models_str_return(self):
        """Проверка, что методы __str__ моделей работают корректно."""
        for model_name, str_value in ModelsStrTests.test_model_response:
            with self.subTest(model_name=model_name):
                self.assertEqual(str(model_name), str_value)
