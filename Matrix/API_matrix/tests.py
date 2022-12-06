from django.urls import reverse
from rest_framework.test import APITestCase
from django.test import TestCase


class MatrixTests(APITestCase):
    def test_matrix_correct(self):

        url = reverse(viewname='c_vec', args=[2, [[-1, -6], [2, 6]]])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "size": 2,
            "matrix": [[-1, -6], [2, 6]],
            "count": [2.0, 3.0],
            "vec": [[-0.89442719, 0.83205029], [0.4472136, -0.5547002]]
        })
