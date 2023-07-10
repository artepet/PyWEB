from rest_framework.test import APITestCase


class WishlistAPITest(APITestCase):
  def setUp(self):
    self.user = User.objects.create_user(username='testuser', password='testpass')
    self.client.login(username='testuser', password='testpass')
    self.product = Product.objects.create(name='Test Product', description='Test Description')
    self.wishlist = Wishlist.objects.create(user=self.user)

  def test_get_wishlist(self):
    url = '/api/wishlist/'
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.data['products']), 0)

  def test_add_to_wishlist(self):
    url = '/api/wishlist/'
    data = {'product_id': self.product.id}
    response = self.client.post(url, data)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data['message'], 'Product added to wishlist')

  def test_remove_from_wishlist(self):
    self.wishlist.products.add(self.product)
    url = '/api/wishlist/'
    data = {'product_id': self.product.id}
    response = self.client.delete(url, data)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data['message'], 'Product removed from wishlist')
