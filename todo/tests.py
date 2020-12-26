from django.test import TestCase, Client

# Create your tests here.
from todo.models import Todo


class TodoTestCase(TestCase):
    todos_list_url = "/api/todos/"
    client = Client()

    def setUp(self):
        Todo.objects.all().delete()

    def test_todo_item_creation(self):
        """Check fields for created item"""
        resp = self.client.post(self.todos_list_url,
                                {'title': "testtitle", 'priority': "High", "description": "test_description"})
        self.assertEquals(resp.status_code, 201)
        resp_json = resp.json()
        self.assertIn('id', resp_json)
        self.assertIn('title', resp_json)
        self.assertIn('description', resp_json)
        self.assertIn('category', resp_json)
        self.assertIn('priority', resp_json)
        self.assertIn('created', resp_json)
        self.assertIn('modified', resp_json)
        single_resp_json = self.client.get(f"/api/todos/{resp_json['id']}/").json()
        self.assertEquals(single_resp_json['title'], "testtitle")
        self.assertEquals(single_resp_json['priority'], "High")
        self.assertEquals(single_resp_json['category'], None)
        self.assertEquals(single_resp_json['description'], "test_description")
        self.assertEquals(single_resp_json['completed'], False)

    def test_todo_list_create_new_item(self):
        expected_items = 3
        for i in range(expected_items):
            Todo.objects.create(title=f"testtitle", priority="High")
        self.assertEqual(Todo.objects.count(), expected_items)
        resp = self.client.get(self.todos_list_url)
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(len(resp.json()), expected_items)
        resp2 = self.client.post(self.todos_list_url, {'title': "testtitle", 'priority': "High"})
        self.assertEquals(resp2.status_code, 201)
        resp3 = self.client.get(self.todos_list_url)
        self.assertEqual(resp3.status_code, 200)
        self.assertEquals(len(resp3.json()), expected_items + 1)
        self.assertEqual(Todo.objects.count(), expected_items + 1)

    def test_todo_list_create_wrong_item_is_not_possible_mandatory_fields(self):
        self.assertEqual(Todo.objects.count(), 0)
        resp = self.client.post(self.todos_list_url, {'title_field_not_present': "testtitle"})
        self.assertEquals(resp.status_code, 400)
        self.assertEqual(Todo.objects.count(), 0)

    def test_todo_item_delete(self):
        id = self.client.post(self.todos_list_url, {'title': "testtitle"}).json()['id']
        self.assertEqual(len(self.client.get(self.todos_list_url).json()), 1)
        resp_delete = self.client.delete(f"/api/todos/{id}/")
        self.assertEquals(resp_delete.status_code, 204)
        self.assertEqual(len(self.client.get(self.todos_list_url).json()), 0)
