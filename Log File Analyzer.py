def log_file_analyzer(file_path):
    total_lines = 0
    error_count = 0
    warning_count = 0

    try:
        with open(file_path, "r") as file:
            for line in file:
                total_lines += 1
                if "error" in line.lower():
                    error_count += 1
                if "warning" in line.lower():
                    warning_count += 1

        print("\n----- LOG FILE ANALYSIS -----")
        print("Total Lines:", total_lines)
        print("Error Messages:", error_count)
        print("Warning Messages:", warning_count)

    except FileNotFoundError:
        print("❌ File not found. Please check the file path.")


# Example usage
path = input("Enter log file path: ")
log_file_analyzer(path)
