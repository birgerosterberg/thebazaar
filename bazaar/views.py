from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower, Coalesce
from django.db.models import Q, Value, DecimalField
from .models import Product, Category
from review.models import Review
from review.views import user_can_review_product, update_product_rating
from .forms import ProductForm

# Create your views here.


def bazaar(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            elif sortkey == 'category':
                sortkey = 'category__name'
            elif sortkey == 'rating':
                products = products.annotate(
                    actual_rating=Coalesce(
                        'rating', Value(0), output_field=DecimalField())
                )
                sortkey = 'actual_rating'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('bazaar'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,


    }

    return render(request, 'bazaar/bazaar.html', context)


def product_detail(request, product_id):
    """ A view to show individual product
    details and handle review submissions. """
    product = get_object_or_404(Product, pk=product_id)
    user_can_review = False
    # Get reviews for the product
    reviews = Review.objects.filter(product=product)

    if request.user.is_authenticated:
        user_can_review = user_can_review_product(request.user, product)
        if request.method == 'POST' and user_can_review:
            review_text = request.POST.get('review_text')
            # Retrieve rating from form
            rating = int(request.POST.get('rating'))
            Review.objects.create(
                product=product,
                user=request.user,
                review_text=review_text,
                rating=rating
                )
            # Update the average product rating
            update_product_rating(product)
            return redirect('product_detail', product_id=product.id)

    context = {
        'product': product,
        'user_can_review': user_can_review,
        'reviews': reviews,  # Include reviews in the context
    }

    return render(request, 'bazaar/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
                )
    else:
        form = ProductForm()

    template = 'bazaar/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            # Save the form but don't commit immediately
            updated_product = form.save(commit=False)
            # Preserve the current rating
            updated_product.rating = product.rating
            # Now save the product
            updated_product.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'bazaar/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('bazaar'))
