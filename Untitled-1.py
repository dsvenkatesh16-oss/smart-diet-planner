# 🚖 Bellary Travel Guide - Choose Start & Destination

routes = {
    "Railway Station to Ballari Fort": {"distance_km": 4.5, "time_min": 15, "auto_cost_rs": 70},
    "Ballari Fort to Cantonment Area": {"distance_km": 3.2, "time_min": 10, "auto_cost_rs": 50},
    "Cantonment Area to KSRTC Bus Stand": {"distance_km": 2.8, "time_min": 8, "auto_cost_rs": 40},
    "KSRTC Bus Stand to Bellary Medical College": {"distance_km": 5.0, "time_min": 15, "auto_cost_rs": 80},
    "Ballari Junction to Sandur Road": {"distance_km": 6.5, "time_min": 20, "auto_cost_rs": 100},
    "Ballari Fort to Moka Road": {"distance_km": 7.0, "time_min": 22, "auto_cost_rs": 110},
    "Parvathi Nagar to Bellary Engineering College": {"distance_km": 8.5, "time_min": 25, "auto_cost_rs": 120}
}

# Extract unique location names
locations = set()
for route in routes:
    parts = route.split(" to ")
    locations.update(parts)
locations = sorted(list(locations))

def find_route(start, end):
    key = f"{start} to {end}"
    if key in routes:
        cost = routes[key]["auto_cost_rs"]
        transport = "Taxi" if cost > 100 else "Auto"
        return {
            "distance_km": routes[key]["distance_km"],
            "time_min": routes[key]["time_min"],
            "transport": transport,
            "cost_rs": cost
        }
    else:
        return None

if __name__ == "__main__":
    print("🚖 Welcome to Bellary Travel Guide!\n")

    print("Available Locations:\n")
    for i, place in enumerate(locations, start=1):
        print(f"{i}. {place}")

    try:
        start_choice = int(input("\nEnter the number for your START location: "))
        end_choice = int(input("Enter the number for your DESTINATION: "))

        if 1 <= start_choice <= len(locations) and 1 <= end_choice <= len(locations):
            start = locations[start_choice - 1]
            end = locations[end_choice - 1]
            route_info = find_route(start, end)

            if route_info:
                print(f"\n📍 Route from {start} to {end}")
                print(f" ➤ Distance: {route_info['distance_km']} km")
                print(f" ➤ Estimated Time: {route_info['time_min']} minutes")
                print(f" ➤ Recommended Transport: {route_info['transport']}")
                print(f" ➤ Estimated Cost: ₹{route_info['cost_rs']}")
            else:
                print(f"\n❌ Sorry, no direct route available from {start} to {end}.")
        else:
            print("\n⚠️ Invalid number entered.")

    except ValueError:
        print("\n⚠️ Please enter valid numbers only.")
