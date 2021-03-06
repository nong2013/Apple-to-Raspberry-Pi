#image_button_01

#Steven Lipton 04-26-14
#Demonstration of buttons and check buttons


from tkinter import *

#make the window
root=Tk()
root.title("Steve's Button Sampler")

#make the frame
frame = Frame(root)
frame.grid(row=0, column=0)

# --- event handlers go here when we add them in 


# --- Add the buttons
           
#button 1 -- basic button
button_1 = Button(frame, text = 'Ok')
button_1.grid(column = 0 , row = 0)

#button_2 -- basic flat button
button_2 = Button(frame, text = 'Ok',relief = FLAT)
button_2.grid(column = 1 , row = 0)
button_2.configure(fg='blue',font=('Sans','18','bold'))

#button 3 -- bitmap button
button_3 = Button(frame, text = 'Ok')
button_3.grid(column = 2 , row = 0)
button_3.configure(bitmap = 'info')

#button 4 -- image button (round button)
button_4 = Button(frame, text = 'Ok')
button_4.grid(column = 3 , row = 0) 
button_Image = PhotoImage(file = 'button_3.gif')
button_4.configure(image = button_Image)

#button 5 -- image button (round rect)
button_5 = Button(frame, text = 'Ok')
button_5.grid(column = 3 , row = 0) 
button_Image = PhotoImage(file = 'button_3.gif')
button_5.configure(image = button_Image)

#button 6 -- a special gift
button_5 = Button(frame, text = 'Ok')
button_5.grid(column = 4 , row = 0) 
button_Image_2 = PhotoImage(file = 'glossy button.gif')
button_5.configure(image = button_Image_2)

# --- main loop

mainloop()
