from flask import Flask, render_template, request

app = Flask(__name__)

foods =[
    {"food": "Oats (100g)", "cost": 35, "protein": 12, "calories": 380, "veg": True},
    {"food": "Rice (100g)", "cost": 15, "protein": 2, "calories": 360, "veg": True},
    {"food": "Wheat Roti (1 pc)", "cost": 8, "protein": 3, "calories": 120, "veg": True},
    {"food": "Dal (100g cooked)", "cost": 25, "protein": 9, "calories": 120, "veg": True},
    {"food": "Chana (100g)", "cost": 18, "protein": 19, "calories": 364, "veg": True},
    {"food": "Rajma (100g)", "cost": 20, "protein": 15, "calories": 330, "veg": True},
    {"food": "Soya Chunks (50g)", "cost": 25, "protein": 26, "calories": 170, "veg": True},
    {"food": "Paneer (100g)", "cost": 60, "protein": 22, "calories": 360, "veg": True},
    {"food": "Milk (200ml)", "cost": 12, "protein": 6, "calories": 122, "veg": True},
    {"food": "Curd (100g)", "cost": 15, "protein": 4, "calories": 98, "veg": True},
    {"food": "Potato (100g)", "cost": 10, "protein": 2, "calories": 87, "veg": True},
    {"food": "Spinach (100g)", "cost": 15, "protein": 3, "calories": 23, "veg": True},
    {"food": "Broccoli (100g)", "cost": 30, "protein": 3, "calories": 34, "veg": True},
    {"food": "Carrot (100g)", "cost": 12, "protein": 1, "calories": 41, "veg": True},
    {"food": "Apple (1 pc)", "cost": 20, "protein": 0, "calories": 95, "veg": True},
    {"food": "Banana (1 pc)", "cost": 8, "protein": 1, "calories": 105, "veg": True},
    {"food": "Orange (1 pc)", "cost": 15, "protein": 1, "calories": 62, "veg": True},
    {"food": "Peanuts (50g)", "cost": 15, "protein": 13, "calories": 280, "veg": True},
    {"food": "Almonds (30g)", "cost": 25, "protein": 6, "calories": 170, "veg": True},
    {"food": "Cashews (30g)", "cost": 30, "protein": 5, "calories": 160, "veg": True},
    {"food": "Walnuts (30g)", "cost": 35, "protein": 4, "calories": 180, "veg": True},
    {"food": "Peanut Butter (2 tbsp)", "cost": 20, "protein": 8, "calories": 188, "veg": True},
    {"food": "Bread (2 slices)", "cost": 12, "protein": 6, "calories": 150, "veg": True},
    {"food": "Biscuits (4 pcs)", "cost": 10, "protein": 2, "calories": 120, "veg": True},
    {"food": "Eggs (2 pcs)", "cost": 12, "protein": 13, "calories": 155, "veg": False},
    {"food": "Boiled Egg (1 pc)", "cost": 6, "protein": 6, "calories": 70, "veg": False},
    {"food": "Chicken Breast (100g)", "cost": 40, "protein": 31, "calories": 165, "veg": False},
    {"food": "Chicken Curry (150g)", "cost": 60, "protein": 25, "calories": 280, "veg": False},
    {"food": "Fish (100g)", "cost": 60, "protein": 22, "calories": 200, "veg": False},
    {"food": "Prawns (100g)", "cost": 80, "protein": 24, "calories": 99, "veg": False},
    {"food": "Mutton (100g)", "cost": 120, "protein": 25, "calories": 250, "veg": False},
]

def get_meal_plan(budget, veg_only):
    meal_plan = []
    total_cost = total_protein = total_calories = 0
    for item in foods:
        if total_cost + item["cost"] <= budget:
            if veg_only and not item["veg"]:
                continue
            meal_plan.append(item)
            total_cost += item["cost"]
            total_protein += item["protein"]
            total_calories += item["calories"]
    return meal_plan, total_cost, total_protein, total_calories


@app.route("/", methods=["GET", "POST"])
def index():
    meal_plan = []
    total_cost = total_protein = total_calories = 0
    if request.method == "POST":
        budget = int(request.form.get("budget", 0))
        veg_only = request.form.get("veg_only") == "yes"
        meal_plan, total_cost, total_protein, total_calories = get_meal_plan(budget, veg_only)
    return render_template("index.html",
                           meal_plan=meal_plan,
                           total_cost=total_cost,
                           total_protein=total_protein,
                           total_calories=total_calories)


if __name__ == "__main__":
    app.run(debug=True)
