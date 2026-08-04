from rest_framework.test import APITestCase


class TaskApiTests(APITestCase):
    def test_health(self):
        res = self.client.get('/api/health')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['status'], 'ok')

    def test_list_empty(self):
        res = self.client.get('/api/tasks/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, [])

    def test_create_task(self):
        res = self.client.post('/api/tasks/', {'title': 'Aprender DevOps'}, format='json')
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data['title'], 'Aprender DevOps')
        self.assertFalse(res.data['done'])

    def test_create_without_title_fails(self):
        res = self.client.post('/api/tasks/', {}, format='json')
        self.assertEqual(res.status_code, 400)

    def test_update_task(self):
        self.client.post('/api/tasks/', {'title': 'Tarea'}, format='json')
        res = self.client.patch('/api/tasks/1/', {'done': True}, format='json')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.data['done'])

    def test_delete_task(self):
        self.client.post('/api/tasks/', {'title': 'Tarea'}, format='json')
        res = self.client.delete('/api/tasks/1/')
        self.assertEqual(res.status_code, 204)
