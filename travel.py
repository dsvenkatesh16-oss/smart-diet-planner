#travial 
routes = {
    "Railway Station to Ballari Fort": {"distance_km": 4.5, "time_min": 15, "auto_cost_rs": 70},
    "Ballari Fort to Cantonment Area": {"distance_km": 3.2, "time_min": 10, "auto_cost_rs": 50},
    "Cantonment Area to KSRTC Bus Stand": {"distance_km": 2.8, "time_min": 8, "auto_cost_rs": 40},
    "KSRTC Bus Stand to Bellary Medical College": {"distance_km": 5.0, "time_min": 15, "auto_cost_rs": 80},
    "Ballari Junction to Sandur Road": {"distance_km": 6.5, "time_min": 20, "auto_cost_rs": 100},
    "Ballari Fort to Moka Road": {"distance_km": 7.0, "time_min": 22, "auto_cost_rs": 110},
    "Parvathi Nagar to Bellary Engineering College": {"distance_km": 8.5, "time_min": 25, "auto_cost_rs": 120}
}
def get_route_info(start,end):
    key=f"{start} to {end}"
    if key in routes:
        if routes[key]["auto_cost_rs"]>100:
            transport="Taxi"
        else:
            transport="auto"
            return {
                    "distance_km":routes[key]["distance_km"],
                    "time_min":routes[key]["time_min"],
                    "transport":transport,
                    "cost_rs":routes[key]["auto_cost_rs"]
                    }  
    else:
        return None
    
if __name__=="__main__":
    print("Welcome to Ballari Travel Guide!")
    print("Available Routes:")
    for route in routes:
        print(" -",route)
    start=input("Enter starting point: ")   
    end=input("Enter destination: ")
    info=get_route_info(start,end)
    if info:
        print(f"\nRoute from {start} to {end}:")
        print(f" Distance: {info['distance_km']} km")
        print(f" Estimated Time: {info['time_min']} minutes")
        print(f" Recommended Transport: {info['transport']}")
        print(f" Estimated Cost: ₹{info['cost_rs']}")
    else:
        print("Sorry, route information not available.")
        