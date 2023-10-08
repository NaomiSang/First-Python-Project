import tkinter as tk 


#create the main window widget
main_window = tk.Tk()
#adding a title and background color to the mainwindow
main_window.title("Calculator & Display BMI Category")
main_window.configure(bg="#F0F8FF")

#creating and customizing the patient entry and label widget
patient_name_label = tk.Label(main_window, text="Enter patient name:", bg="green", font=("Arial", 12))
patient_name_entry = tk.Entry(main_window, font=("Calibri", 12))

#we pack the widgets
patient_name_label.pack(pady=12)
patient_name_entry.pack()

#creating label and radio buttons for selecting the weight unit of choice
#first we create the IntVar object to use with the buttons
weight_unit_choice = tk.StringVar()
#we set it to lbs
weight_unit_choice.set("lbs")

#create choose weight unit label
weight_unit_label = tk.Label(main_window, text="Choose weight unit:", bg="green", font=("Arial", 12))

#create the two radio buttons to choose from 
lbs_radio = tk.Radiobutton(main_window, text="Pounds (lbs)", variable=weight_unit_choice, value="lbs", bg="white", font=("Arial", 12))
kgs_radio = tk.Radiobutton(main_window, text="Kilograms (kgs)", variable=weight_unit_choice, value="kgs", bg="white", font=("Arial", 12))

#pack the label widget and radio buttons
weight_unit_label.pack(pady=12)
kgs_radio.pack()
lbs_radio.pack()

#creating and customizing the patient weight entry and label
patient_weight_label = tk.Label(main_window, text="Enter patient weight (kgs or lbs):", bg="green", font=("Arial", 12))
patient_weight_entry = tk.Entry(main_window, font=("Arial", 12))

#pack the label and entry widgets
patient_weight_label.pack(pady=12)
patient_weight_entry.pack()

# Creating and customizing the patient height label and entry
patient_height_label = tk.Label(main_window, text="Enter height (ms or ins):", bg="green", font=("Arial", 12))
patient_height_entry = tk.Entry(main_window, font=("Arial", 14))

#we pack the widgets
patient_height_label.pack(pady=12)
patient_height_entry.pack()

#create the function for calculating patient's BMI
def calculate_patient_BMI():
    name = patient_name_entry.get()
    weight = float(patient_weight_entry.get())
    height = float(patient_height_entry.get())
    unit = weight_unit_choice.get()

#convert weight to kg if using lbs; this allows the use of both lbs and kgs in this calculator
    if unit == "lbs":
        weight *= 0.453592

    #define the formula to calculate the BMI
    BMI = weight / (height ** 2)

    #here we define categories to be displayed depending on the value of the resulting BMI. We use the if-elif-else statement here
    if BMI < 18.5:
        BMI_category = "Underweight👎"
    elif BMI >= 18.5 and BMI < 25:
        BMI_category = "Normal👍"
    elif BMI >= 25 and BMI < 30:
        BMI_category = "Overweight😞"
    else:
        BMI_category = "Obese🛑"

    # here we display the results including patient name, BMI value and the BMI category
    BMI_label.config(text="{}'s BMI is: {:.2f} ({})".format(name, BMI, BMI_category))

#creating a button and label to calculate and display the patient BMI
calculate_button = tk.Button(main_window, text="Calculate patient BMI", command=calculate_patient_BMI, bg="white", fg="green", font=("Arial", 14, "bold"))
BMI_label = tk.Label(main_window, text="", bg="#F0F8FF", font=("Arial", 14))

#pack the button and label
calculate_button.pack(pady=12)
BMI_label.pack(pady=12)

#Enter the Tkinter main loop
tk.mainloop()