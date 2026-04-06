# ==============================
# ACTIVITY 5 - FILE HANDLING
# Surname: Esteban
# ==============================

from pathlib import Path
from datetime import datetime
import shutil

# STEP 1: SET YOUR CUSTOM FOLDER
backup_dir = Path.home() / "Documents" / "Esteban_Activity_5"
backup_dir.mkdir(exist_ok=True)

# STEP 2: FILE MANAGER FUNCTION
def file_manager():
    file_name = input("Enter filename (e.g., notes.txt): ")
    file_path = backup_dir / file_name

    while True:
        print("\n--- MENU ---")
        print("1. Write to file")
        print("2. Append to file")
        print("3. Read file")
        print("4. Backup file")
        print("5. Exit")
        print("6. List backup files")  # Added option

        choice = input("Choose an option (1-6): ")

        # OPTION 1: WRITE
        if choice == "1":
            content = input("Enter content to write:\n")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("File written successfully.")

        # OPTION 2: APPEND
        elif choice == "2":
            more = input("Enter content to append:\n")
            with open(file_path, "a", encoding="utf-8") as f:
                f.write("\n" + more)
            print("Content appended.")

        # OPTION 3: READ
        elif choice == "3":
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    print("\nFile Content:\n", f.read())
            else:
                print("File not found.")

        # OPTION 4: BACKUP
        elif choice == "4":
            if file_path.exists():
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_file = file_path.with_name(
                    f"{file_path.stem}_Esteban_backup_{timestamp}{file_path.suffix}"
                )
                shutil.copy2(file_path, backup_file)
                print(f"Backup created: {backup_file.name}")
            else:
                print("Cannot backup. File does not exist.")

        # OPTION 5: EXIT
        elif choice == "5":
            print("Exiting the file manager.")
            break

        # OPTION 6: LIST BACKUPS
        elif choice == "6":
            print("\nBackup files:")
            found = False
            for file in backup_dir.glob("*backup*"):
                print("-", file.name)
                found = True
            if not found:
                print("No backup files found.")

        else:
            print("Invalid choice. Please try again.")

# STEP 3: RUN PROGRAM
if __name__ == "__main__":
    file_manager()

    