from visualisations.visualisation_approche_naive import visualisation_approche_naive
from visualisations.visualisation_approche_optimise import visualisation_approche_optimise

def main():
    while True:
        print("Select the version of the algorithm to run:")
        print("1. Visualisation Approach Naive")
        print("2. Visualisation Approach Optimise")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            visualisation_approche_naive()
        elif choice == '2':
            visualisation_approche_optimise() 
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break  # Exit the loop and program
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()  # Run the main function

