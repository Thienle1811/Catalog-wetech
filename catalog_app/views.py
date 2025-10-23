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

def about_company(request):
    return render(request, 'about_company.html')

def careers(request):
    return render(request, 'careers.html')

def press(request):
    return render(request, 'press.html')

def help_index(request):
    return render(request, 'help_index.html')

def help_speaklife(request):
    return render(request, 'help_speaklife.html')

def help_sortic(request):
    return render(request, 'help_sortic.html')

def help_vista(request):
    return render(request, 'help_vista.html')

def help_optisync(request):
    return render(request, 'help_optisync.html')

def help_optimind(request):
    return render(request, 'help_optimind.html')

def help_vera(request):
    return render(request, 'help_vera.html')

def warranty_policy(request):
    return render(request, 'warranty_policy.html')

def purchase_guide(request):
    return render(request, 'purchase_guide.html')

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
