# FITGROCER - Project Planning & Scheduling (Text-Based in Python)

# Define project phases with duration in weeks
project_phases = [
    {"Phase": "Requirement Analysis", "Duration": 1, "Start_Week": 1},
    {"Phase": "Feasibility Study", "Duration": 1, "Start_Week": 1},
    {"Phase": "System Design", "Duration": 2, "Start_Week": 2},
    {"Phase": "Front-End Development", "Duration": 3, "Start_Week": 3},
    {"Phase": "Back-End Development", "Duration": 3, "Start_Week": 4},
    {"Phase": "Database Integration", "Duration": 1, "Start_Week": 6},
    {"Phase": "Module Implementation", "Duration": 2, "Start_Week": 7},
    {"Phase": "Testing & Debugging", "Duration": 1, "Start_Week": 9},
    {"Phase": "Final Testing", "Duration": 1, "Start_Week": 10},
    {"Phase": "Documentation", "Duration": 2, "Start_Week": 11},
]

TOTAL_WEEKS = 15

# Function to print schedule table
def print_schedule_table():
    print("\nFITGROCER – Project Planning & Scheduling\n")
    print("{:<30} {:<15} {:<10}".format("Phase", "Duration (Weeks)", "Start Week"))
    print("-" * 60)
    for task in project_phases:
        print("{:<30} {:<15} {:<10}".format(task["Phase"], task["Duration"], task["Start_Week"]))
    print("-" * 60)

# Function to print text-based Gantt chart
def print_gantt_chart():
    print("\nText-Based Gantt Chart (● = Work in Progress):\n")
    header = "Phase".ljust(30) + ''.join([f"W{str(i).zfill(2)} " for i in range(1, TOTAL_WEEKS + 1)])
    print(header)
    print("-" * len(header))
    
    for task in project_phases:
        line = task["Phase"].ljust(30)
        for week in range(1, TOTAL_WEEKS + 1):
            if task["Start_Week"] <= week < task["Start_Week"] + task["Duration"]:
                line += " ●  "
            else:
                line += "    "
        print(line)

# Run functions
print_schedule_table()
print_gantt_chart()
