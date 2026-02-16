import time
import random

def calculate_eta(distance, velocity):
    # Time = Distance / Velocity
    if velocity <= 0:
        return 0
    return distance / velocity

def start_navigation():
    print("--- ARTEMIS SENTINEL: NAVIGATION & RESCUE TRACKER ---")
    
    # Starting coordinates (Distance in km, Velocity in km/s)
    dist_to_gateway = 5000.0  
    velocity = 1.02 # Average orbital speed
    
    try:
        while dist_to_gateway > 0:
            # Simulate orbital mechanics: gravity increases speed as you get closer
            velocity += random.uniform(0.001, 0.005)
            dist_to_gateway -= velocity
            
            # Calculate ETA in minutes
            seconds_left = calculate_eta(dist_to_gateway, velocity)
            minutes_left = seconds_left / 60
            
            # The HUD Display
            print(f" [NAV] DIST: {dist_to_gateway:.2f} km | VEL: {velocity:.3f} km/s | ETA: {minutes_left:.1f} min", end="\r")
            
            time.sleep(1)
            
        print("\n>> [SYSTEM]: DOCKING MANEUVER COMPLETE. WELCOME TO GATEWAY.")
            
    except KeyboardInterrupt:
        print("\n--- NAVIGATION PAUSED ---")

if __name__ == "__main__":
    start_navigation()