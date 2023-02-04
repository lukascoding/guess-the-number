import random
import tkinter as tk

def start_game():
    global secret_number
    secret_number = random.randint(1, 100)
    input_number.delete(0, tk.END)
    result_label.config(text='')

def check_number():
    try:
        number=int(input_number.get())
        if number == secret_number:
            result_label.config(text='correct! you won.')
        elif number < secret_number:
            result_label.config(text='Too low. try again.')
        else:
            result_label.config(text='high. try again.')
    except ValueError:
        result_label.config(text='Invalid input. try again.')



# main window
root = tk.Tk()
root.title('guess the number')
root.geometry('300x150')


#secret number 
secret_number = None

#input field
input_number = tk.Entry(root, width=5)
input_number.pack()


# button
button = tk.Button(root, text="Check", command=check_number)
button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()


# Start game
start_game()

# Run main loop
root.mainloop()
