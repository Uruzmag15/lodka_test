from django.test import TestCase

from .views import CategoryViewSet
from .models import Category


class Request:
    body = '''{
        "name": "Category 1" ,
        "children": [
            {
                "name": "Category 1.1" ,
                "children": [
                    {
                        "name": "Category 1.1.1" ,
                        "children": [
                            {
                                "name": "Category 1.1.1.1"
                            },
                            {
                                "name": "Category 1.1.1.2"
                            },
                            {
                                "name": "Category 1.1.1.3"
                            }
                        ]
                    },
                    {
                        "name": "Category 1.1.2" ,
                        "children": [
                            {
                                "name": "Category 1.1.2.1"
                            },
                            {
                                "name": "Category 1.1.2.2"
                            },
                            {
                                "name": "Category 1.1.2.3"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Category 1.2" ,
                "children": [
                    {
                        "name": "Category 1.2.1"
                    },
                    {
                        "name": "Category 1.2.2" ,
                        "children": [
                            {
                                "name": "Category 1.2.2.1"
                            },
                            {
                                "name": "Category 1.2.2.2"
                            }
                        ]
                    }
                ]
            }
        ]
    }'''


class CategoryTestCase(TestCase):
    def setUp(self) -> None:
        respones = CategoryViewSet.create(None, Request)
        self.assertEqual(respones.content, b'Success!')

    def test_example_1(self):
        obj = Category.objects.get(name='Category 1.1')
        parents = obj.parents()
        self.assertEqual(parents[0].name, 'Category 1')
        children = obj.children.all()
        self.assertEqual(children[0].name, 'Category 1.1.1')
        self.assertEqual(children[1].name, 'Category 1.1.2')
        siblings = obj.siblings()
        self.assertEqual(siblings[0].name, 'Category 1.2')

    def test_example_2(self):
        obj = Category.objects.get(name='Category 1.1.2.1')
        parents = obj.parents()
        self.assertEqual(parents[0].name, 'Category 1.1.2')
        self.assertEqual(parents[1].name, 'Category 1.1')
        self.assertEqual(parents[2].name, 'Category 1')
        children = obj.children.all()
        self.assertEqual(list(children), [])
        siblings = obj.siblings()
        self.assertEqual(siblings[0].name, 'Category 1.1.2.2')
        self.assertEqual(siblings[1].name, 'Category 1.1.2.3')
