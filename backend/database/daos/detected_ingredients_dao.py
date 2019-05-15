from typing import List, Dict

from base_dao import BaseDao
from dao_models.detection import Detection
from dao_models.detected_ingredient import DetectedIngredient

TABLE = "detected_ingredients"
SCAN_ID = "scan_id"
INGREDIENT_ID = "ingredient_id"
DETECTIONS = "detections"
COLUMNS = [SCAN_ID, INGREDIENT_ID, DETECTIONS]


class DetectedIngredientsDao(BaseDao):
    def __init__(self):
        super().__init__(TABLE, COLUMNS)

    def get_detected_ingredients(self, ids: List[int] = None) -> List[DetectedIngredient]:
        if ids is not None:
            rows = self.get(clause="ids in {}".format(self.list_to_in_param(ids)))
        else:
            rows = self.get()
        return [DetectedIngredient(**r) for r in rows]

    def get_waste_by_menu_item(self):
        sql = 'select detected_ingredients.detections, ingredients.name, menu_items.name ' \
              'from detected_ingredients ' \
              'inner join ingredients on ingredients.id = detected_ingredients.ingredient_id ' \
              'inner join scans on scans.id = detected_ingredients.scan_id ' \
              'inner join menu_items on menu_items.id = scans.menu_item_id'
        print(sql)
        return self.fetch_sql(sql)


    def insert_detected_ingredients(self, detected_ingredients: List[DetectedIngredient]) -> int:
        return self.insert([d.get_for_db() for d in detected_ingredients])


if __name__ == "__main__":
    did = DetectedIngredientsDao()
    d1 = Detection(0, 0, 100)
    d2 = Detection(40, 0, 50)
    detected_ingredient = DetectedIngredient(1, 1, [d1, d2])
    print(detected_ingredient.get_for_db())

    did.insert_detected_ingredients([detected_ingredient])
    did.insert_detected_ingredients([detected_ingredient])
    got = did.get_detected_ingredients()
    print(got)