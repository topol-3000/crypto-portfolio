import os

from django.core.management.base import BaseCommand

from portfolio.models import Cryptocurrency
from portfolio.services.cryptocurrencies_fetcher import CoinGeckoCryptoCoinFetcher


class Command(BaseCommand):
    help = "Fetch all cryptocurrencies and add them to the DB if they are not added yet."

    def handle(self, *args, **kwargs):
        min_market_cap_to_fetch_crypto = int(os.environ.get("MIN_MARKET_CAP_TO_FETCH_CRYPTO"))
        coin_fetcher = CoinGeckoCryptoCoinFetcher(os.environ.get("COIN_GECKO_API_KEY"), min_market_cap_to_fetch_crypto)
        added_count = 0
        for coin in coin_fetcher.get_coins():
            self.stdout.write(f"Adding {coin}.")
            try:
                obj, created = Cryptocurrency.objects.get_or_create(
                    name=coin.name,
                    ticker=coin.ticker,
                    image=coin.image_url,
                    price=coin.price,
                    market_cap=coin.market_cap,
                )

                if created:
                    added_count += 1

            except Exception as exp:
                self.stdout.write(self.style.ERROR(f"Error: {exp}. Skipping the crypto."))

        self.stdout.write(self.style.SUCCESS(f"{added_count} new cryptocurrencies added to the database."))
