#Import and Use os Module
import os
import shutil

# Question 1: Show current working directory
print("📌 Current Working Directory:", os.getcwd())

# Question 2 & 3: Check/create reports directory
reports_dir = "reports"
if not os.path.exists(reports_dir):
    os.mkdir(reports_dir)
    print(f"✅ Created folder: {reports_dir}")
else:
    print(f"📁 Folder '{reports_dir}' already exists.")

# Question 4: Find all .txt files in current directory
txt_files = [f for f in os.listdir() if f.endswith('.txt') and os.path.isfile(f)]

print("📄 .txt files found:")
for file in txt_files:
    print(" -", file)

# Question 5: Move files to reports folder
for file in txt_files:
    shutil.move(file, os.path.join(reports_dir, file))
    print(f"✅ Moved: {file} → {reports_dir}/")

print("🎉 All .txt files processed.")
