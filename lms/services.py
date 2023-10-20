import stripe

from config.settings import API_KEY


def get_pay_url(name: str, amount):

    # set API_KEY
    stripe.api_key = API_KEY

    # create product
    product = stripe.Product.create(name=name)

    # create price
    price = stripe.Price.create(
      unit_amount=int(amount)*100,
      currency="usd",
      recurring={"interval": "month"},
      product=product,
    )

    # get pay url
    url = stripe.PaymentLink.create(
      line_items=[
        {
          "price": price,
          "quantity": 1,
        },
      ],
    )

    return url['url']
