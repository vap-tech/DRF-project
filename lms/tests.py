from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.models import User


class LessonAPITest(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='user@mail.ru', password='test')
        self.group = Group.objects.create(name='manager')
        self.group.user_set.add(self.user)
        self.client.force_authenticate(user=self.user)  # Аутентифицируем клиента с созданным пользователем
        data = {'name': 'course one', 'description': 'test desc', }
        self.client.post('/lms/course/', data)

    def test_course_and_subscribe(self):
        # create course
        data = {'name': '123', 'description': '123'}
        response = self.client.post('/lms/course/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # list course
        response = self.client.get('/lms/course/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # subscribe
        course_pk = dict(response.data['results'][0])['pk']
        self.client.post('/lms/subscribe/', {'course': course_pk})
        response = self.client.get('/lms/course/')
        subscription = dict(response.data['results'][0])['subscription']
        self.assertEqual(subscription, True)

        # unsubscribe
        response = self.client.delete('/lms/unsubscribe/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get('/lms/course/')
        subscription = dict(response.data['results'][0])['subscription']
        self.assertEqual(subscription, False)

    def test_lesson(self):

        # create
        response = self.client.get('/lms/course/')
        course_pk = dict(response.data['results'][0])['pk']
        data = {'name': '123', 'description': '123', 'course': course_pk, 'video_url': 'https://youtube.com/rty234/'}
        response = self.client.post('/lms/lesson/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # list
        response = self.client.get('/lms/lesson/all/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # update
        data = {'name': 'New name', 'course': course_pk, 'video_url': 'https://youtube.com/rty234/'}
        response = self.client.put('/lms/lesson/1/update/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # delete
        response = self.client.delete('/lms/lesson/1/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
