import tkinter
import tkinter.messagebox	

root = tkinter.Tk()


root.geometry("600x350")
root.configure(bg="#cdcdcd", padx=20, pady=20)
root.title("ToDo List")

tasks = []


def update_listbox():	
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)


def clear_listbox():
    lb_tasks.delete(0, "end")


def add_task():
    task = txt_input.get()
    if task != "":
        tasks.append(task)
        update_listbox()
    else:
        lbl_display["text"] = "Please enter a task!"
        txt_input.delete(0, "end")


def del_all():
    confirmed = tkinter.messagebox.askyesno(
        "Please Confirm", "Do you really want to delete all of the tasks?"
        )
    if confirmed is True:
        global tasks
        tasks = []
        update_listbox()


def del_one():
    task = lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
        update_listbox()


def show_number_of_tasks():
    number_of_tasks = len(tasks)

    msg = "Number of tasks: %s" % number_of_tasks
    lbl_display["text"] = msg


lbl_display = tkinter.Label(root,
                            text="Azamat Baizhanov's ToDo List",
                            bg="teal", fg="white",
                            font=('Arial', 13, 'bold')
                            )
lbl_display.grid(row=0, column=1)

txt_input = tkinter.Entry(root, width=35, font=('Courier New', 12, 'bold'))
txt_input.grid(row=1, column=1)

btn_add_task = tkinter.Button(
                            root,
                            text="Add Task",
                            fg="white", bg="green", width=15,
                            command=add_task,
                            font=('Arial', 10, 'bold')
                            )
btn_add_task.grid(row=1, column=0, padx=20, pady=(0, 15))

btn_del_all = tkinter.Button(
                            root,
                            text="Delete All",
                            fg="white", bg="teal", width=15,
                            command=del_all,
                            font=('Arial', 10, 'bold')
                            )
btn_del_all.grid(row=2, column=0)

btn_del_one = tkinter.Button(
                            root,
                            text="Delete Selected",
                            fg="white", bg="teal", width=15,
                            command=del_one,
                            font=('Arial', 10, 'bold')
                            )
btn_del_one.grid(row=4, column=0, pady=(0, 15))

lb_tasks = tkinter.Listbox(root, width=35, font=('Arial', 12, 'bold'))
lb_tasks.grid(row=2, column=1, rowspan=10)

btn_number_of_tasks = tkinter.Button(
                                    root,
                                    text="Number of Tasks",
                                    fg="white", bg="teal", width=15,
                                    command=show_number_of_tasks,
                                    font=('Arial', 10, 'bold')
                                    )
btn_number_of_tasks.grid(row=5, column=0)

btn_exit = tkinter.Button(
                        root,
                        text="Exit",
                        fg="white", bg="red", width=15,
                        command=exit,
                        font=('Arial', 10, 'bold')
                        )
btn_exit.grid(row=8, column=0, pady=(15, 0))

root.mainloop()