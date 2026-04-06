from pathlib import Path
from pathlib import Path

student_id = "254781"   
student_name = "Andrei Zachary V. Esteban"  

output_dir = Path.home() / "Documents" / "Esteban_Activity_5"
output_dir.mkdir(exist_ok=True)

file_path = output_dir / "Act5_example.txt"

with open(file_path, "w", encoding="utf-8") as file:
    file.write("Hello, Welcome to Python Programming!\n")
    file.write("File saved safely with pathlib.\n")
    file.write("Python makes file handling easy!")
    
print(f"File saved to: {file_path.resolve()}")

if file_path.exists():
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    print("\nFile content:\n", content)

with open(file_path, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        if "Python" in line:
            print(line.strip())
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        words = line.split()
        print(f"{line.strip()} → {len(words)} words")
with open(file_path, "a", encoding="utf-8") as file:
    file.write("\nThis line was added!")

print("Data appended successfully.")


lines = ["Another line 1", "Another line 2"]

with open(file_path, "a", encoding="utf-8") as file:
    for line in lines:
        file.write("\n" + line)
user_text = input("Enter something to add: ")

with open(file_path, "a", encoding="utf-8") as file:
    file.write("\n" + user_text)

from datetime import datetime
import shutil
backup_dir = Path.home() / "Documents" / "Esteban_Activity_5"
backup_dir.mkdir(exist_ok=True)

def write_with_backup(filename, content):
    file_path = backup_dir / filename

    if file_path.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        backup_path = file_path.with_name(
            f"{file_path.stem}_Esteban_backup_{timestamp}{file_path.suffix}"
        )

        shutil.copy2(file_path, backup_path)
        print(f"Backup saved: {backup_path.name}")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
        print(f"File saved: {file_path.name}")

def read_file(filename):
    file_path = backup_dir / filename

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
print("=== File Operations Demo ===")

print("\n1. Creating new file:")
write_with_backup("demo.txt", "Initial content")

print("\n2. Updating file (with backup):")
write_with_backup("demo.txt", "Updated content")

print("\n3. Reading file:")
print(read_file("demo.txt"))

print("\n4. Listing backups:")
for backup in backup_dir.glob("*backup*"):
    print("-", backup.name)

def show_menu():
    print("\n=== FILE MANAGER ===")
    print("1. Create/Write File")
    print("2. Read File")
    print("3. Append File")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        filename = input("Enter filename: ")
        content = input("Enter content: ")
        write_with_backup(filename, content)

    elif choice == "2":
        filename = input("Enter filename: ")
        try:
            print("\nFile Content:")
            print(read_file(filename))
        except FileNotFoundError:
            print("File not found.")

    elif choice == "3":
        filename = input("Enter filename: ")
        text = input("Enter text to append: ")

        file_path = backup_dir / filename
        with open(file_path, "a", encoding="utf-8") as file:
            file.write("\n" + text)

        print("Text appended successfully.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")