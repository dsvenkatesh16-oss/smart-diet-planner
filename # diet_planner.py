# diet_planner.py

foods = [
    {"food": "Oats (100g)", "cost": 35, "protein": 12, "calories": 380, "veg": True},
    {"food": "Rice (100g)", "cost": 15, "protein": 2, "calories": 360, "veg": True},
    {"food": "Soya Chunks (100g)", "cost": 25, "protein": 52, "calories": 345, "veg": True},
    {"food": "Eggs (2 pcs)", "cost": 12, "protein": 13, "calories": 155, "veg": False},
    {"food": "Curd (100g)", "cost": 20, "protein": 3, "calories": 61, "veg": True},
    {"food": "Chana (100g)", "cost": 18, "protein": 19, "calories": 364, "veg": True},
    {"food": "Milk (100ml)", "cost": 22, "protein": 6, "calories": 120, "veg": True},
    {"food": "chiken (100g)","cost":25, "protein":32,"calories":165,"veg":False},
    {"food": "poha (100g)","cost":30,"protein":2,"calories":110,"veg":True},
    {"food": "dal(100g)","cost":50,"protein":20,"calories":110,"veg":True},
    {"food": "panner(100g)","cost":60,"protein":22,"calories":360,"veg":True},
    {"food": "giled fish(100g)","cost":80,"protein":18,"calories":200,"veg":False},
    {"food": "giled chicken(100g)","cost":70,"protein":25,"calories":250,"veg":False},
    {"food": "fruit saladd(100g)","cost":40,"protein":1,"calories":80,"veg":True},
    
] # List of foods with cost, protein, calories, and vegetarian status

def calculate_tdee(weight, height, age, gender, activity_level):# Function to calculate Total Daily Energy Expenditure (TDEE)
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5 # Basal Metabolic Rate (BMR) calculation
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    
    activity_factors = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very active": 1.9
    }
    
    return bmr * activity_factors.get(activity_level, 1.55)

def get_meal_plan(calorie_target,veg_only,budget): # Function to get meal plan based on budget and dietary preference
    meal_plan = []
    total_cost = 0
    total_protein = 0
    total_calories = 0

    for item in foods:
        if total_cost + item["cost"] <= budget:
             if veg_only and not item["veg"]:
                 continue
             meal_plan.append(item["food"])
             total_cost += item["cost"]
             total_protein += item["protein"]
             total_calories += item["calories"]

    return meal_plan, total_cost, total_protein, total_calories


            
      
if __name__ == "__main__":
    print("🥗 Welcome to the Smart Diet Planner!\n")

    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))
    age = int(input("Enter your age: "))
    gender = input("Gender (male/female): ").lower()
    activity = input("Activity level (sedentary/light/moderate/active/very active): ").lower()
    goal = input("Goal (fat loss/maintenance/gain): ").lower()
    choice = input("Do you want vegetarian only? (yes/no): ").lower()
    veg_only = choice == "yes"
    budget = int(input("Enter your daily budget (₹): "))

    tdee = calculate_tdee(weight, height, age, gender, activity)

    if goal == "fat loss":
        calorie_target = tdee * 0.8
    elif goal == "gain":
        calorie_target = tdee * 1.1
    else:
        calorie_target = tdee

    print(f"\nYour daily calorie target: {int(calorie_target)} kcal")

    meals, cost, protein, calories = get_meal_plan(calorie_target, veg_only, budget)

    print("\n🍽️ Suggested Meal Plan:")
    for meal in meals:
        print(" -", meal)
    print(f"\n💰 Total Cost: ₹{cost}")
    print(f"💪 Total Protein: {protein} g")
    print(f"🔥 Total Calories: {int(calories)} kcal")
    
