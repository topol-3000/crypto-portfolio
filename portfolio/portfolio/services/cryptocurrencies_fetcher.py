from dataclasses import dataclass

from requests import get


@dataclass(frozen=True)
class CryptoCoin:
    name: str
    ticker: str
    image_url: str
    price: float
    market_cap: float


class CoinGeckoCryptoCoinFetcher:
    API_URL = (
        "https://api.coingecko.com/api/v3/coins/markets"
        "?vs_currency=usd&per_page=250&order=market_cap_desc&page={page}"
    )

    def __init__(self, api_key: str, minimum_market_cap: int) -> None:
        """Initializes a CoinGeckoCryptoCoinFetcher instance.

        Parameters:
        api_key (str): The API key for accessing the CoinGecko API.
        minimum_market_cap (int): The minimum market cap for cryptocurrencies to be fetched.
        """
        self.coins = set()
        self.__api_key = api_key
        self.__minimum_market_cap = minimum_market_cap

    def get_coins(self) -> set[CryptoCoin]:
        """Returns a set of CryptoCoin objects.

        Returns:
        set[CryptoCoin]: A set of CryptoCoin objects representing the fetched cryptocurrencies.
        """
        page = 1
        while True:
            try:
                coins = self.__get_page(page)
                self.__fill_coins(coins)
            except ValueError:
                break

            page += 1

        return self.coins

    def __get_page(self, page: int) -> list[dict]:
        """Fetches data for a specific page from the CoinGecko API.

        Parameters:
        page (int): The page number to fetch data for.

        Returns:
        list[dict]: A dictionary containing the data fetched from the API.

        Raises:
        Exception: If the API request fails or returns a status code other than 200.
        """
        response = get(
            self.API_URL.format(page=page), headers={"accept": "application/json", "x-cg-pro-api-key": self.__api_key}
        )
        if response.status_code != 200:
            print(f"Failed to fetch data from page {page}")
            raise ValueError(f"Failed to fetch data from page {page}")

        return response.json()

    def __fill_coins(self, coins: list[dict]) -> None:
        """Fills the set of cryptocurrencies with data from the given list of coins.

        Parameters:
        coins (list[dict]): A list of dictionaries representing cryptocurrency data.
        """
        for coin in coins:
            name = coin["name"]
            ticker = coin["symbol"]
            market_cap = coin["market_cap"]
            if market_cap < self.__minimum_market_cap:
                raise ValueError(f"Market cap of {name} ({ticker}) is below the minimum.")

            crypto_coin = CryptoCoin(
                name=name, ticker=ticker, image_url=coin["image"], price=coin["current_price"], market_cap=market_cap
            )
            self.coins.add(crypto_coin)
