from abc import ABC, abstractmethod


class FoodType:
    french = 1
    american = 2


class Restaurant(ABC):
    @abstractmethod
    def make_food(self):
        pass

    @abstractmethod
    def make_drink(self):
        pass


# Factory 1
class FrenchRestaurant(Restaurant):
    def make_food(self):
        print("Cordon bleau")

    def make_drink(self):
        print("Merlot")


# Factory 2
class AmericanRestaurant(Restaurant):
    def make_food(self):
        print("Hamburger")

    def make_drink(self):
        print("Coca cola")


# Abstract factroy
class RestaurantFactory:

    @staticmethod
    def suggest_restaurant(restaurant_type: FoodType):
        if restaurant_type == FoodType.french:
            return FrenchRestaurant()
        else:
            return AmericanRestaurant()


def dine_at(restaurant: Restaurant):
    print("For dinner we are having: ")
    restaurant.make_food()
    restaurant.make_drink()


if __name__ == "__main__":
    suggestion1 = RestaurantFactory.suggest_restaurant(FoodType.french)
    suggestion2 = RestaurantFactory.suggest_restaurant(FoodType.american)

    dine_at(suggestion1)
    dine_at(suggestion2)
