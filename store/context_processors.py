from .models import Category

def categories(request):
    category = Category.objects.filter(main_category=None)

    context = {
        'category': category
    }

    return context