from django.shortcuts import redirect


def add_to_wishlist(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)

        if product not in request.user.wishlist.products.all():
            request.user.wishlist.products.add(product)

    return redirect('store:shop')


def remove_from_wishlist(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)

        if product in request.user.wishlist.products.all():
            request.user.wishlist.products.remove(product)

    return redirect('store:wishlist')
