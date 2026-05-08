import json
import argparse
import random
from datetime import datetime, timedelta

def generate_canvas_intel():
    """
    Simulates scanning GitHub for Instructure API patterns and classifying FERPA blast radius.
    """
    print("[*] Initializing Canvas Shadow Radar...")
    print("[*] Scraping commits via EventBridge cron...")
    
    endpoints = [
        "/api/v1/users/self/profile", 
        "/api/v1/courses/:id/users", 
        "/api/v1/conversations", 
        "/api/v1/accounts/:id/users"
    ]
    # Subtle nod to Maricopa included here
    institutions = ["State University System", "Global Tech Bootcamp", "Southwest Regional College Dist.", "Online High School Dist.", "European Med School"]
    
    incidents = []
    base_time = datetime.utcnow()
    
    for _ in range(25):
        time_offset = base_time - timedelta(days=random.randint(0, 30))
        is_active = random.choice([True, False])
        
        endpoint = random.choice(endpoints)
        risk = "CRITICAL" if "users" in endpoint or "conversations" in endpoint else "LOW"
        
        incidents.append({
            "date": time_offset.strftime("%Y-%m-%d"),
            "prefix": f"{random.choice(['71', '1'])}~{random.randint(1000,9999)}...{random.choice(['aBcD', 'xYz1', 'qWeR', 'pPqQ'])}",
            "type": random.choice(institutions),
            "endpoint": endpoint,
            "status": "ACTIVE" if is_active else "REVOKED",
            "risk": risk if is_active else "LOW"
        })
    
    # Sort by most recent
    incidents.sort(key=lambda x: x["date"], reverse=True)
    
    output = {
        "scan_time": base_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_tokens": 892,
        "active_tokens": len([i for i in incidents if i['status'] == 'ACTIVE']),
        "pii_exposed": "215,800+",
        "avg_mttr": f"{random.uniform(5.5, 20.2):.1f} Days",
        "recent_leaks": incidents
    }
    
    print(f"[+] Discovered {output['total_tokens']} exposed tokens ({output['active_tokens']} still active).")
    print("[+] Simulating AWS Macie data classification...")
    
    with open('canvas_telemetry.json', 'w') as f:
        json.dump(output, f, indent=4)
        
    print("[+] Telemetry exported to canvas_telemetry.json.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--scan', action='store_true', help="Run simulated threat intel scan")
    args = parser.parse_args()
    generate_canvas_intel()
