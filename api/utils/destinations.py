import numpy as np

class TouristDestinations:
    def __init__(self, activity, climate, length, transport, budget):
        self.activity = 0
        self.climate = 0
        self.length = 0
        self.transport = 0
        self.budget = 0
        
        self.generate_pattern(activity, climate, length, transport, budget)
        
        self.destinations_matrix = {
            # [активность, климат, длительность, транспорт, бюджет]
            "Байкал": np.array([3.0, -2.0, 2.0, 1.0, 1.5]),
            "Камчатка": np.array([3.5, -2.5, 2.5, 2.5, 2.5]),
            "Алтай": np.array([3.0, -1.0, 2.0, 1.5, 1.0]),
            "Сочи": np.array([1.5, 2.5, 1.5, 2.5, 2.0]),
            "Крым": np.array([1.0, 2.5, 1.5, 1.5, 1.0]),
            "Анапа": np.array([0.5, 2.5, 1.0, 1.5, 1.0]),
            "Санкт-Петербург": np.array([1.5, 0.0, 1.0, 2.5, 1.5]),
            "Казань": np.array([1.5, 0.0, 1.0, 2.0, 1.0]),
            "Великий Новгород": np.array([1.0, 0.0, 1.0, 2.0, 1.0]),
            "Астрахань": np.array([0.5, 2.0, 1.0, 1.0, 1.0]),
            "Краснодар": np.array([1.0, 2.0, 1.0, 1.5, 1.0]),
            "Ростов-на-Дону": np.array([1.0, 2.0, 1.0, 1.5, 1.0])
        }

    def generate_pattern(self, activity, climate, length, transport, budget):
        if activity == "active":
            self.activity += 3.0 
        elif activity == "calm":
            self.activity -= 1.0 
        elif activity == "cultural":
            self.activity += 1.5 
        elif activity == "food":
            self.activity += 0.5 

        if climate == "cold":
            self.climate += -2.0 
        elif climate == "warm":
            self.climate += 2.5 
        elif climate == "moderate":
            self.climate += 1.0 

        if length == "short":
            self.length += 1.0 
        elif length == "medium":
            self.length += 1.5 
        elif length == "long":
            self.length += 2.0 

        if transport == "plane":
            self.transport += 2.5 
        elif transport == "train":
            self.transport += 2.0 
        elif transport == "car":
            self.transport += 1.5 
        elif transport == "ship":
            self.transport += 1.0 

        if budget == "low":
            self.budget += 1.0 
        elif budget == "medium":
            self.budget += 1.5 
        elif budget == "high":
            self.budget += 2.0 

        return self.activity, self.climate, self.length, self.transport, self.budget

    def get_destinations(self):
        user_preferences = np.array([
            self.activity,
            self.climate,
            self.length,
            self.transport,
            self.budget
        ])
        
        user_preferences = user_preferences / np.linalg.norm(user_preferences)

        # Векторная модель
        similarities = {}
        for destination, characteristics in self.destinations_matrix.items():
            norm_characteristics = characteristics / np.linalg.norm(characteristics)
            similarity = np.dot(user_preferences, norm_characteristics)
            similarities[destination] = similarity
        
        sorted_destinations = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        
        return sorted_destinations[:3]


if __name__ == "__main__":
    quiz = TouristDestinations(activity="cultural", climate="cold", length="short", transport="plane", budget="high")
    print(quiz.get_destinations())
