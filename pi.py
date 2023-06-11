import random
from tkinter import *
# import turtle

window = Tk()
window.title("Estimate pi")
window.config(height=400, width=400, padx=50, pady=50)

canvas = Canvas(width=360, height=360, highlightthickness=0)
pi_img = PhotoImage(file="pi.png")
canvas.create_image(180, 145, image=pi_img)
canvas.grid(column=1, row=0)

iteration_cell = Entry(width=25)
iteration_cell.insert(0, 0)
iteration_cell.focus()
iteration_cell.grid(column=1, row=2)

# pi_mechanism
def pi_value():
  number_of_dots = int(iteration_cell.get())
  point_in_circle = 0
  point_total = 0
  for _ in range(number_of_dots):
    x_dis = random.uniform(0, 1)
    y_dis = random.uniform(0, 1)
    distance = x_dis**2 + y_dis**2
    if distance <= 1:
      point_in_circle += 1
    point_total += 1
  pi = 4 * point_in_circle/point_total
  pi_lbl.config(text=pi)

iteration_lbl = Label(text="Number of dots")
iteration_lbl.grid(column=1, row=1)

calculate_btn = Button(text="Calculate Pi", command=pi_value)
calculate_btn.grid(column=1, row=3)

pi_lbl = Label(text="0.0000", font=("Arial", 20, "normal"))
pi_lbl.grid(column=1, row=4)


window.mainloop()