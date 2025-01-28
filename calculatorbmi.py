import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox

def display_bmi_circular_scale(bmi):
    # Set up the circular scale
    categories = ['Underweight', 'Normal weight', 'Overweight', 'Obesity Class I', 'Obesity Class II']
    thresholds = [0, 18.5, 24.9, 29.9, 34.9, 40]  # Define BMI thresholds
    angles = np.linspace(0, 2 * np.pi, len(thresholds), endpoint=False)

    # Extend the angles to close the circular plot
    angles = np.append(angles, angles[0])
    thresholds = np.append(thresholds, thresholds[0])

    # Create a circular figure
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection': 'polar'})
    ax.set_theta_direction(-1)
    ax.set_theta_offset(np.pi / 2)

    # Plot the BMI scale
    for i in range(len(categories)):
        ax.fill_between(angles[i:i+2], 0, thresholds[i+1], 
                        color=['blue', 'green', 'yellow', 'orange', 'red'][i], alpha=0.5, label=categories[i])

    # Calculate the BMI angle
    bmi_angle = np.interp(bmi, thresholds[:-1], angles[:-1])

    # Initialize the pointer
    pointer, = ax.plot([0, 0], [0, max(thresholds)], color='purple', linewidth=2, label=f'Your BMI: {bmi:.2f}')

    # Add labels and legend
    ax.set_yticks([])  # Remove radial ticks
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    ax.set_title('BMI Circular Scale', va='bottom')

    # Animate the pointer movement
    num_steps = 100
    for step in range(num_steps + 1):
        current_angle = step / num_steps * bmi_angle
        pointer.set_data([0, current_angle], [0, max(thresholds)])
        plt.pause(0.02)  # Pause to create animation effect

    # Hold the final plot
    plt.show()

def calculate_bmi(weight, height):
    # Calculate BMI
    bmi = weight / (height ** 2)

    # Determine the BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    elif 30 <= bmi < 34.9:
        category = "Obesity Class I"
    else:
        category = "Obesity Class II"

    # Show BMI and category in a message box
    messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}\nCategory: {category}")

    # Display BMI circular scale
    display_bmi_circular_scale(bmi)

def on_submit():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            raise ValueError
        calculate_bmi(weight, height)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid positive numbers for weight and height.")

# Create the GUI window
root = tk.Tk()
root.title("BMI Calculator")

# Add form elements
tk.Label(root, text="Enter your weight (kg):", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root, font=("Arial", 12))
weight_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter your height (m):", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(root, font=("Arial", 12))
height_entry.grid(row=1, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Calculate BMI", font=("Arial", 12), command=on_submit)
submit_button.grid(row=2, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()