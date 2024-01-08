from django import forms

class VoucherForm(forms.Form):
    voucher_code = forms.CharField(label='Voucher Code', max_length=20)
