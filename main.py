def generate_plant_info(plant_name):
    return {
        "description": f"{plant_name} is a beautiful and popular plant often used for indoor decoration.",
        "care": {
            "water": "Water once every 1-2 weeks",
            "light": "Indirect sunlight",
            "soil": "Well-draining soil"
        }
    }

if __name__ == "__main__":
    plant = input("Enter plant name: ")
    info = generate_plant_info(plant)

    print("\nDescription:")
    print(info["description"])

    print("\nCare Guide:")
    for key, value in info["care"].items():
        print(f"{key.capitalize()}: {value}")
