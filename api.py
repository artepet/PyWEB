from rest_framework.views import APIView
from rest_framework.response import Response


class WishlistAPIView(APIView):
    def get(self, request):
        wishlist = Wishlist.objects.get(user=request.user)
        serializer = WishlistSerializer(wishlist)
        return Response(serializer.data)

    def post(self, request):
        product_id = request.data.get('product_id')
        product = Product.objects.get(id=product_id)

        wishlist = Wishlist.objects.get(user=request.user)
        wishlist.products.add(product)

        return Response({'message': 'Product added to wishlist'})

    def delete(self, request):
        product_id = request.data.get('product_id')
        product = Product.objects.get(id=product_id)

        wishlist = Wishlist.objects.get(user=request.user)
        wishlist.products.remove(product)

        return Response({'message': 'Product removed from wishlist'})
