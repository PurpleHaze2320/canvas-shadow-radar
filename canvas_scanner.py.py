import json
import argparse
import random
from datetime import datetime, timedelta

def generate_canvas_intel():
    """
    Simulates parsing GitHub for exposed Canvas LMS API Tokens
    and mapping the potential blast radius (FERPA/PII risks).
    """
    print("[*] Initializing Canvas Shadow Radar...")
    print("[*] Scanning public commits for Instructure API patterns (71~ / 1~)...")
    
    # Simulated threat intelligence data
    endpoints = [
        "/api/v1/users/self/profile", 
        "/api/v1/courses", 
        "/api/v1/conversations", 
        "/api/v1/users/self/files"
    ]
    institutions = ["State University System", "Global Tech Bootcamp", "Ivy League Network", "Online High School Dist.", "European Med School"]
    
    incidents = []
    base_time = datetime.utcnow()
    
    for i in range(12):
        time_offset = base_time - timedelta(minutes=random.randint(5, 2880))
        is_active = random.choice([True, True, False]) # Weight toward active
        incidents.append({
            "timestamp": time_offset.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "token_prefix": f"71~{random.randint(1000,9999)}...{random.choice(['aBcD', 'xYz1', 'qWeR'])}",
            "institution_type": random.choice(institutions),
            "exposed_endpoint": random.choice(endpoints),
            "status": "ACTIVE - PII AT RISK" if is_active else "REVOKED",
            "ferpa_risk": "HIGH" if is_active else "LOW"
        })
    
    # Sort by most recent
    incidents.sort(key=lambda x: x["timestamp"], reverse=True)
    
    output = {
        "scan_time": base_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_tokens_found": 342,
        "active_tokens": 128,
        "pii_records_exposed": "85,400+",
        "recent_leaks": incidents
    }
    
    print(f"[+] Discovered {output['total_tokens_found']} exposed tokens ({output['active_tokens']} still active).")
    print("[+] Exporting telemetry to dashboard JSON...")
    
    with open('canvas_telemetry.json', 'w') as f:
        json.dump(output, f, indent=4)
        
    print("[+] Done. Shadow Radar analysis complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Canvas LMS API Token Scanner")
    parser.add_argument('--scan', action='store_true', help="Run OSINT scan for leaked tokens")
    args = parser.parse_args()
    
    generate_canvas_intel()