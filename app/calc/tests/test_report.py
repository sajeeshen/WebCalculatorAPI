# from django.test import TestCase
# from app.tasks import add
#
# class AddTestCase(TestCase):
#
#     def test_celery_working(self):
#         """Test that the ``add`` task runs with no errors,
#         and returns the correct result."""
#         result = add.delay(8, 8)
#
#         self.assertEquals(result.get(), 16)
#         self.assertTrue(result.successful())
