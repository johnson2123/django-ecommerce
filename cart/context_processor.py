from .cart import Cart

# create context processor so our cart can work on all pages of site

def cart(request):
    #return the default data from our cart
    return {'cart':Cart(request)}