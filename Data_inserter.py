import pandas as pd

# Define the initial dataset (previously extracted workouts)
previous_workout_data = [
    ["Week 5 S1", "Freestyle", "Warm-up", "Easy", "400m", 1, "None", "None", "Loosen up"],
    ["Week 5 S1", "IM", "Main Set", "Aerobic", "200m", 1, "None", "None", "Focus on technique"],
    ["Week 5 S2", "Backstroke", "Endurance", "Moderate", "6x100m", 6, "30s", "Paddles", "Maintain stroke count"],
    ["Week 5 S3", "Freestyle", "Sprint", "High", "6x25m", 6, "60s", "Sponge", "Max effort"],
]

# Define the newly extracted workouts from Week 6 & 7
new_workout_data = [
    ["Week 6 S1", "Freestyle", "Warm-up", "Easy", "600m", 1, "None", "None", "SKPS drill"],
    ["Week 6 S1", "Freestyle", "Main Set", "Moderate", "6x100m", 6, "1:30", "None", "Descend pace"],
    ["Week 6 S2", "IM", "Endurance", "High", "5x200m", 5, "30s", "Sponge & Fins", "Kick/Swim mix"],
    ["Week 6 S3", "Backstroke", "Drills", "Aerobic", "6x50m", 6, "1:15", "Snorkel", "Descend by kick intensity"],
    ["Week 6 S4", "Sprint", "Speed", "Max Effort", "6x25m", 6, "1:30", "Loofah", "Resistance sprint"],
    ["Week 7 S1", "Freestyle", "Warm-up", "Easy", "800m", 1, "None", "Snorkel", "Focus on technique"],
    ["Week 7 S2", "Freestyle", "Race Pace", "High", "20x25m", 20, "35s", "Loofah", "Max effort resistance"],
    ["Week 7 S4", "Sprint", "Speed", "Maximum", "4x100m", 4, "2:30", "Resistance Sox", "All-out kicking"],
]

# Combine previous and new data into a DataFrame
combined_workouts = previous_workout_data + new_workout_data
df = pd.DataFrame(combined_workouts, columns=["Session", "Stroke", "Training Type", "Intensity", "Distance", "Reps", "Rest Time", "Equipment", "Notes"])

# Save final dataset
csv_filename = "/mnt/data/swim_workout_data.csv"
df.to_csv(csv_filename, index=False)

# Provide download link
csv_filename
