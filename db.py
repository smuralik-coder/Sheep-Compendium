from models.models import Sheep

class FakeDB:
    def __init__(self):
        self.data = {
            1: Sheep(id=1, name="Spice", breed="Gotland", sex="Female")
        }

    def get_sheep(self, sheep_id: int):
        return self.data.get(sheep_id)

    def add_sheep(self, sheep):
        self.data[sheep.id] = sheep
        return sheep

    def update_sheep(self, sheep_id, updated_sheep):
        if sheep_id in self.data:
            self.data[sheep_id] = updated_sheep
            return updated_sheep
        return None

db = FakeDB()