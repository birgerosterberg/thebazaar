from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import VoucherForm
from .models import Voucher

def apply_voucher(request):
    if request.method == 'POST':
        form = VoucherForm(request.POST)
        if form.is_valid():
            voucher_code = form.cleaned_data['voucher_code']
            try:
                voucher = Voucher.objects.get(code=voucher_code, active=True)
                request.session['voucher_id'] = voucher.id
                request.session['voucher_code'] = voucher.code
                request.session['discount_percentage'] = float(voucher.discount_percentage)
                messages.success(request, 'Voucher applied successfully.')
            except Voucher.DoesNotExist:
                request.session.pop('voucher_id', None)  # Remove any existing voucher info
                request.session.pop('voucher_code', None)
                request.session.pop('discount_percentage', None)
                messages.error(request, 'Invalid voucher code.')
        else:
            messages.error(request, 'Invalid form submission.')
    return redirect('view_bag')

def remove_voucher(request):
    # Remove voucher information from the session
    request.session.pop('voucher_id', None)
    request.session.pop('voucher_code', None)
    request.session.pop('discount_percentage', None)

    messages.info(request, "Voucher removed successfully.")
    return redirect('view_bag')