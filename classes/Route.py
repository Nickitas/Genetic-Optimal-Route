import math

class Route:
    def __init__(self, cities):
        self.cities = cities

    def calculate_distance(self):
        total_distance = 0
        for i in range(len(self.cities) - 1):
            city1 = self.cities[i]
            city2 = self.cities[i + 1]
            distance = self.calculate_euclidean_distance(city1, city2)
            total_distance += distance
        # Добавим расстояние от последнего города к первому, чтобы закончить цикл
        total_distance += self.calculate_euclidean_distance(self.cities[-1], self.cities[0])
        self.distance = total_distance
        return total_distance

    def calculate_euclidean_distance(self, city1, city2):
        x1, y1 = city1
        x2, y2 = city2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
