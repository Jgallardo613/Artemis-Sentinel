import time      
import random    
import datetime  

# 1. THE WINGMAN LOGIC 
def witty_wingman(hr, o2):
    if hr > 110:
        return ">> [WINGMAN]: Pulse is climbing! Take a breath."
    if o2 < 95.0:
        return ">> [WINGMAN]: O2 levels low. Check tank valve."
    return ">> [WINGMAN]: Systems nominal. Looking good."

# 2. THE BLACK BOX LOGGER
def log_mission_data(hr, o2, msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] HR: {hr:.1f} | O2: {o2:.1f}% | LOG: {msg}\n"
    with open("mission_log.txt", "a") as f:
        f.write(log_entry)

# 3. THE MAIN MISSION ENGINE
def mission_start():
    print("--- ARTEMIS SENTINEL: MISSION TELEMETRY START ---")
    print("Status: Edge-Computing Active | Blackout Protocol: ENABLED")
    
    oxygen = 98.5        
    heart_rate = 72      
    
    try:
        while True:
            heart_rate += random.uniform(-1, 1.5)
            oxygen -= random.uniform(0, 0.01)
            
            status_update = witty_wingman(heart_rate, oxygen)
            log_mission_data(heart_rate, oxygen, status_update)
            
            # THE FIX: ': <70' pads the line with spaces to clear old text
            # 'flush=True' makes sure the Mac terminal updates immediately
            print(f" [BIO] HR: {heart_rate:.1f} | O2: {oxygen:.1f}% | {status_update: <70}", end="\r", flush=True)
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n--- MISSION LOG SAVED TO mission_log.txt ---")

if __name__ == "__main__":
    mission_start()