class User:
    def __init__(self, name, age, height, weight):
        if age <= 0 or height <= 0 or weight <= 0:
            raise ValueError("Age, height and weight must be positive.")

        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        return round(self.weight / (self.height ** 2), 2)


class FitnessTracker(User):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age, height, weight)
        self.steps = 0
        self.calories = 0
        self.workouts = []

    def add_steps(self, steps):
        if steps < 0:
            raise ValueError("Steps cannot be negative.")
        self.steps += steps
        self.calories += steps * 0.04

    def add_workout(self, workout, duration):
        if duration <= 0:
            raise ValueError("Duration must be positive.")
        self.workouts.append((workout, duration))
        self.calories += duration * 5

    def save_to_file(self):
        with open("fitness_data.txt", "a") as file:
            file.write(f"Name: {self.name}\n")
            file.write(f"Age: {self.age}\n")
            file.write(f"BMI: {self.calculate_bmi()}\n")
            file.write(f"Steps: {self.steps}\n")
            file.write(f"Calories: {round(self.calories,2)}\n")
            file.write("Workouts:\n")
            for w in self.workouts:
                file.write(f"  {w[0]} - {w[1]} mins\n")
            file.write("-" * 30 + "\n")

    def read_file(self):
        try:
            with open("fitness_data.txt", "r") as file:
                print("\n--- Fitness History ---")
                print(file.read())
        except FileNotFoundError:
            print("No previous data found.")


# -------- Main Program --------
try:
    print("=== Personal Fitness Tracker ===")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kg: "))

    tracker = FitnessTracker(name, age, height, weight)

    while True:
        print("\n1. Add Steps")
        print("2. Add Workout")
        print("3. Save Data")
        print("4. View Saved Data")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            steps = int(input("Enter steps walked: "))
            tracker.add_steps(steps)
            print("Steps added successfully!")

        elif choice == "2":
            workout = input("Enter workout name: ")
            duration = int(input("Enter duration (minutes): "))
            tracker.add_workout(workout, duration)
            print("Workout added successfully!")

        elif choice == "3":
            tracker.save_to_file()
            print("Data saved successfully!")

        elif choice == "4":
            tracker.read_file()

        elif choice == "5":
            print("Thank you for using Fitness Tracker!")
            break

        else:
            print("Invalid choice. Try again.")

except ValueError as e:
    print("Input Error:", e)
except Exception as e:
    print("Unexpected Error:", e)