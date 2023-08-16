class Menu:
    def __init__(
        self,
        id: int,
        name: str,
        price: float,
        restaurant_id: int
    ):
        self.id = id
        self.name = name
        self.price = price
        self.restaurant_id = restaurant_id


class Restaurant:
    def __init__(self, id: int, location: str):
        self.id = id
        self.location = location


class User:
    def __init__(
        self,
        id: int,
        username: str, # unique
        email: str, # unique
        password: str
    ):
        self.id = id
        self.username = username
        self.email = email
        self.password = password


class Order:
    def __init__(
        self,
        order_id: int,
        user_id: int,
        date: str,
        menu_id: int,
        success: bool
    ):
        self.order_id = order_id
        self.user_id = user_id
        self.date = date
        self.menu_id = menu_id
        self.success = success
