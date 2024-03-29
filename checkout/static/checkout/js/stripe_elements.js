// Core logic/payment flow for this comes from here:
// https://stripe.com/docs/payments/accept-a-payment

// CSS from here: 
// https://stripe.com/docs/stripe-js

// Adapted from Code Institute's Boutique Ado Walkthrough
// */

// Add the card element & set variables
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
base: {
    color: '#4D4D4D',
    fontFamily: '"Source Sans 3", sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
        color: '#959595',
    }
},
invalid: {
    color: '#B25B76',
    iconColor: '#B25B76'
}
};
var card = elements.create('card', {
style: style,
hidePostalCode: true
});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
var errorDiv = document.getElementById('card-errors');
if (event.error) {
    var html = `
        <span class="me-1" role="alert">
            <i class="fas fa-times"></i>
        </span>
        <span>${event.error.message}</span>
    `;
    $(errorDiv).html(html);
} else {
    errorDiv.textContent = '';
}
});


// Handle form submit
var form = document.getElementById('payment-form');

// Event listener for payment form submit
form.addEventListener('submit', function(ev) {
ev.preventDefault();

// Disables the submit button & card input
card.update({ 'disabled': true});
$('#submit-button').attr('disabled', true);

// Hides the payment form
$('#payment-form').fadeToggle(100);

// Displays the loading animation
$('#loading-overlay').fadeToggle(100);

// Gets the value of the checkbox from the form (save user info)
var saveInfo;
try {
    saveInfo = document.getElementById('id-save-info').checked;
}
catch(err) {
    saveInfo = false;
}


// From using {% csrf_token %} in the form
var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
var postData = {
    'csrfmiddlewaretoken': csrfToken,
    'client_secret': clientSecret,
    'save_info': saveInfo,
};

var url = '/checkout/cache_checkout_data/';

// Posts the data to the URL
// including the additional data from the cache_checkout_data view
// Once done handles the card payment being sent to Stripe
$.post(url, postData).done(function () {

    // Passes card details to Stripe
    stripe.confirmCardPayment(clientSecret, {

        // Sends payment details with user details
        payment_method: {
            card: card,
            billing_details: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address:{
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            }
        },
        shipping: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            address: {
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address2.value),
                city: $.trim(form.town_or_city.value),
                country: $.trim(form.country.value),
                postal_code: $.trim(form.postcode.value),
                state: $.trim(form.county.value),
            }
        },
    }).then(function(result) {

        // if there is an error send error message below input
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="me-1" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);

            // Re-displays the payment form
            $('#payment-form').fadeToggle(100);

            // Hides the loading animation
            $('#loading-overlay').fadeToggle(100);

            // Re-enable the submit button and card input
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);

        // if payment details are valid submit payment form
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
}).fail(function () {
    // if sending the data to URL fails reload the page,
    // the error will be in django messages
    location.reload();
});

});