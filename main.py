import random

food=('Burger King','Five Guys','BGR Joint',' Nandos', 'Checkers', 'New Fortune', 'Subway', 'Wendys', 'Baja Fresh', 'Jerrys', 'Corner Bakery', 'Red Robin', 'McDonalds', 'KFC', 'Panera',' Taco Bar', 'IHop(IHob)', 'Popeyes', 'Red Lobster', 'Chipotle', 'Sardis', 'Guapos', 'Pieology', 'Boston Market', 'Wow Deli', 'Firehouse Subs', 'Mission BBQ', 'Halal Guys', 'The Habit', 'Potbelly', 'Qdoba', 'Asia Cafe', 'Woodside Deli', 'Gordon Biersch', 'Mellow Mushroom', 'Wing Stop', 'BWW', 'Giuseppi',  'Cooking at Home', 'Taco Bell', 'First Place You Pass' )

group=" ".join(random.choice(food) for _ in range(1))

print(group)
