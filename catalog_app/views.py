from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def product_detail(request):
    return render(request, 'product-detail.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def product_page(request, product_slug):
    if product_slug == 'meetflow':
        return render(request, 'product-detail.html')
    elif product_slug == 'notiq':
        return render(request, 'product_notiq.html')
    elif product_slug == 'vista':
        return render(request, 'product_vista.html')
    elif product_slug == 'optisync':
        return render(request, 'product_optisync.html')
    elif product_slug == 'opsmind':
        return render(request, 'product_opsmind.html')
    elif product_slug == 'vera':
        return render(request, 'product_vera.html')
    else:
        # Dùng một template chung cho các sản phẩm chưa có nội dung
        context = {'product_name': product_slug.replace('-', ' ').title()}
        return render(request, 'product_placeholder.html', context)
