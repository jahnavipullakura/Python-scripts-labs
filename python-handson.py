import os

# Folder paths
input_dir = "data_input"
output_dir = "data_output"

# Step 1: Create data_input folder if missing
if not os.path.exists(input_dir):
    os.mkdir(input_dir)
    print(f"📂 Created folder: {input_dir}")
    print("📥 Please add .txt files to the data_input folder and rerun the script.")
    exit()

# Step 2: Create data_output folder
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Step 3: Process .txt files
summary_lines = []

for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        filepath = os.path.join(input_dir, filename)
        with open(filepath, 'r') as f:
            lines = f.readlines()

        processed_lines = []
        line_count = 0
        word_count = 0

        for line in lines:
            if line.strip().startswith('#'):
                continue
            line_count += 1
            word_count += len(line.split())
            processed_lines.append(line.replace("temp", "permanent"))

        output_path = os.path.join(output_dir, filename)
        with open(output_path, 'w') as f:
            f.writelines(processed_lines)

        summary_lines.append(f"{filename} | Lines: {line_count} | Words: {word_count}")

# Step 4: Write summary
summary_path = os.path.join(output_dir, "summary.txt")
with open(summary_path, 'w') as f:
    f.write("Summary Report\n")
    f.write("====================\n")
    for line in summary_lines:
        f.write(line + "\n")

print("✅ All files processed. Check 'data_output' folder for results.")
