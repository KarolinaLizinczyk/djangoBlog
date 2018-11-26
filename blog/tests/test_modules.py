from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestModels:
    def test_product_is_in_stock(self):
        post = mixer.blend('blog.Post')
        assert str(post) == post.title