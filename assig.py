# Task 1: Grade Calculation with Validation
def letter_grade(score):
    if not (0 <= score <= 100):
        raise ValueError(f"Invalid score encountered: {score}. Scores must be between 0 and 100.")
        
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# Task 2: Analyze Student Data
def analyse(students):
    results = {}
    for name, score in students.items():
        results[name] = {
            "score": score,
            "grade": letter_grade(score)
        }
    return results


# Task 3: Summary Statistics and Clean Reporting
def summary(results):
    if not results:
        print("\nNo student data available to summarize.")
        return

    print("\n" + "=" * 10 + " FINAL REPORT " + "=" * 10)
    # 1. Print individual results
    for name, data in results.items():
        print(f"{name:<10}: {data['score']} → {data['grade']}")
    
    print("\n" + "-" * 30 + "\n")

    # 2. Compute Class Average
    total_score = sum(data["score"] for data in results.values())
    average = total_score / len(results)
    print(f"Class Average : {average:.2f}")

    # 3. Find Highest and Lowest Scorers
    highest_student = max(results, key=lambda k: results[k]["score"])
    lowest_student = min(results, key=lambda k: results[k]["score"])
    
    print(f"Highest Score : {highest_student} ({results[highest_student]['score']})")
    print(f"Lowest Score  : {lowest_student} ({results[lowest_student]['score']})")

    # 4. Count Grade Distribution
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for data in results.values():
        g = data["grade"]
        grade_counts[g] = grade_counts.get(g, 0) + 1

    count_str = "  ".join(f"{g}={grade_counts[g]}" for g in sorted(grade_counts.keys()))
    print(f"Grade Counts  : {count_str}")


# Task 4: Interactive Input Collection & Exception Handling Wrapper
def run_grading_tool():
    students = {}
    print("--- Student Grade Reporting Tool ---")
    print("Enter student names and scores. Type 'done' as the name to finish.\n")
    
    while True:
        name_input = input("Enter student name: ").strip()
        if name_input.lower() == 'done':
            break
        if not name_input:
            print("Name cannot be empty. Please try again.")
            continue
            
        score_input = input(f"Enter score for {name_input}: ").strip()
        
        # Validate that the input is an actual number before saving
        try:
            score = float(score_input)
            # We instantly check the score range using Task 1's validation rules
            letter_grade(score) 
            students[name_input] = score
        except ValueError as e:
            # Captures letters/symbols typed as scores OR scores outside 0-100
            print(f"🚨 Invalid Input: {e}")
            print("This student was not added. Please re-enter them with a valid score.\n")

    # Once data gathering is done, analyze and print the summary
    try:
        analyzed_data = analyse(students)
        summary(analyzed_data)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# --- Run the Program ---
if __name__ == "__main__":
    run_grading_tool()