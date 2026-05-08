import json
import argparse
import random
from datetime import datetime, timedelta

def generate_canvas_intel():
    """
    Generates a massive dataset of simulated Canvas API leaks for the portfolio frontend.
    Outputs to a .js file so the static React app can ingest it easily.
    """
    print("[*] Initializing Canvas Shadow Radar Engine...")
    
    endpoints = [
        "/api/v1/users/self/profile", 
        "/api/v1/courses/:id/users", 
        "/api/v1/conversations", 
        "/api/v1/accounts/:id/users",
        "/api/v1/courses/:id/assignments",
        "/api/v1/accounts/:account_id/courses"
    ]
    
    # Expanded list to make the search bar highly functional
    institutions = [
        "Maricopa Community Colleges", "Glendale Community College", "Arizona State University",
        "University of Central Florida", "Penn State University", "Ohio State University",
        "Texas A&M University", "University of Washington", "Rutgers University",
        "University of Florida", "Michigan State University", "Indiana University",
        "University of Minnesota", "University of Texas at Austin", "University of Wisconsin-Madison",
        "Harvard University", "Stanford University", "MIT", "Yale University", "Princeton University",
        "Global Tech Bootcamp", "Online High School Dist.", "European Med School", "State University System",
        "Los Angeles Community College District", "Miami Dade College", "Lone Star College System",
        "Ivy Tech Community College", "Houston Community College", "Northern Virginia Community College",
        "City University of New York (CUNY)", "State University of New York (SUNY)", "University of California System"
    ]
    
    incidents = []
    base_time = datetime.utcnow()
    total_generated = random.randint(580, 750)
    
    print(f"[*] Simulating EventBridge scraping... Generating {total_generated} records.")
    
    for _ in range(total_generated):
        time_offset = base_time - timedelta(days=random.randint(0, 30), hours=random.randint(0,23))
        is_active = random.choice([True, False, False]) # 33% chance of being active
        
        endpoint = random.choice(endpoints)
        risk = "CRITICAL" if "users" in endpoint or "conversations" in endpoint else ("HIGH" if "assignments" in endpoint else "LOW")
        
        # Ensure Maricopa and Glendale show up heavily for your specific audience
        inst = random.choice(institutions)
        if random.random() < 0.15: 
            inst = random.choice(["Maricopa Community Colleges", "Glendale Community College"])
            
        incidents.append({
            "date": time_offset.strftime("%Y-%m-%d"),
            "prefix": f"{random.choice(['71', '1'])}~{random.randint(1000,9999)}...{random.choice(['aBcD', 'xYz1', 'qWeR', 'pPqQ', 'mNbV', 'jKkL'])}",
            "type": inst,
            "endpoint": endpoint,
            "status": "ACTIVE" if is_active else "REVOKED",
            "risk": risk if is_active else "LOW"
        })
    
    incidents.sort(key=lambda x: x["date"], reverse=True)
    
    active_count = len([i for i in incidents if i['status'] == 'ACTIVE'])
    
    output = {
        "scan_time": base_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_tokens": total_generated,
        "active_tokens": active_count,
        "pii_exposed": f"{active_count * random.randint(800, 1500):,}+",
        "avg_mttr": f"{random.uniform(12.5, 24.2):.1f} Days",
        "recent_leaks": incidents
    }
    
    # Write to a JS file so the static HTML can load it without CORS/fetch issues
    with open('canvas_data.js', 'w') as f:
        f.write(f"window.canvasThreatData = {json.dumps(output, indent=4)};")
        
    print("[+] Exported heavy dataset to canvas_data.js")
    print("[+] Open index.html to view the populated dashboard.")

if __name__ == "__main__":
    generate_canvas_intel()
