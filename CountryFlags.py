from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Country Flags")
root.geometry("600x400")
root.configure(background="lightblue")

get_input = Entry(root)
show_label = label(root)

india_map = ImageTk.PhototImage(Image.open ("India.jpg"))
america_map = ImageTk.PhototImage(Image.open ("America.jpg"))
australia_map = ImageTk.PhototImage(Image.open ("Australia.png"))
philippines_map = ImageTk.PhototImage(Image.open ("Philippines.png"))
japan_map = ImageTk.PhototImage(Image.open ("Japan.jpg"))

maps_dictionary = { "India" : india_map ,
                   "America" : america_map ,
                   "Australia" : australia_map ,
                   "Philippines" : philippnes_map,
                   "Japan" : japan_map,}

def showMaps():
    try:
        map_name = get_input.get()
        print(map_name)
        show_label['image'] = maps_dictionary[map_name]
    except:
        messagebox.showinfo("Error","Sorry! This country flag is not present in our system")

btn = Button(root, text="Show Map", bg="green", command=showMaps)
get_input.place(relx=0.5, rely=0.1, anchor=CENTER)
btn.place(relx=0.5, rely=0.2, anchor=CENTER)
show_label.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()