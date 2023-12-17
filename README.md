cocktailbuilder.py

Web-API for cocktailbuilder.com

![image](https://github.com/aminobotskek/cocktailbuilder/assets/94906343/5ce98283-c5f2-4295-acda-ad93930a9dd1)

### Example
```python3
import cocktailbuilder
client = cocktailbuilder.Client()
ingredients=client.best_ingredients_to_buy(param=1,max=3)
