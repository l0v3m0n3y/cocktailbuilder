import requests
class Client():
	def __init__(self):
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
		self.api='https://www.cocktailbuilder.com/json'
	def best_ingredients_to_buy(self,param:int=3,max:int=25):
	    return requests.get(f"{self.api}/bestIngredientsToBuy?max={max}&param={param}",headers=self.headers).json()
	def top_ingredients(self,param:int=3,max:int=25):
	    return requests.get(f"{self.api}/topByIngredients?&max={max}&param={param}",headers=self.headers).json()