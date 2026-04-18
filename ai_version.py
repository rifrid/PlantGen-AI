import os

def generate_plant_prompt(plant_name):
    return f"""
Generate a detailed plant description and care guide for {plant_name}.

Include:
- Description
- Watering needs
- Sunlight requirements
- Soil type
"""

def main():
    plant = input("Enter plant name: ")
    prompt = generate_plant_prompt(plant)

    print("\n--- AI Prompt ---")
    print(prompt)
    print("\n(Note: Connect this with Claude or OpenAI API for real output)")

if __name__ == "__main__":
    main()
