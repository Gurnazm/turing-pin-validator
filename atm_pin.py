import tkinter as tk
from tkinter import messagebox
def control():
    userpin = "".join(entry.get() for entry in entries)
    systempin = "1234"
    if len(userpin) == 0:
        messagebox.showerror("Hata", "Lütfen PIN alanını boş bırakmayınız.")
        return
    elif len(userpin) != 4:
        messagebox.showerror("Hata", "Lütfen 4 haneli bir PIN giriniz.")
        for e in entries:
                e.delete(0, tk.END)
                entries[0].focus_set()
        return
    
    bant = ["#"] + list(userpin) + ["#"] + list(systempin) + ["#"]
    pointer = 1
    syspoint = bant.index("#", pointer) + 1
    print("Başlangıç Bandı:", "".join(bant))

    while bant[pointer] != "#":
        userchar = bant[pointer]
        syschar = bant[syspoint + (pointer - 1)]

        print(f"\nAdım {pointer}:")
        print(f"Kullanıcı karakteri: {userchar} | Sistem karakteri: {syschar}")
        
        if userchar == syschar:
            bant[pointer] = "X"
            bant[syspoint + (pointer-1)] = "X"
            print("Eşleşti → Bant güncellendi:", "".join(bant))
            
        else:
            print("Eşleşmedi → Bant güncellendi:", "".join(bant))
            messagebox.showerror("Hata", "Şifre hatalı ❌\nŞifreyi tekrar deneyin.")
            for e in entries:
                e.delete(0, tk.END)
            entries[0].focus_set()
            return
        
        pointer += 1
    print("\nTüm karakterler eşleşti → Son Bant:", "".join(bant))
    messagebox.showinfo("Başarılı", "Şifre doğru ✅")
    for e in entries:
        e.delete(0, tk.END)
    entries[0].focus_set()

def onedigit(P):
    return (P.isdigit() or P == "") and len(P) <= 1

def jump(event, index):
    if event.keysym == "BackSpace":
        if entries[index].get() == "" and index > 0:
            entries[index-1].focus_set()
    else:
        if entries[index].get() != "" and index < 3:
            entries[index+1].focus_set()
        elif index == 3 and entries[index].get() != "":
            control()
def toggle_show():
    global show_pin
    show_pin = not show_pin
    for e in entries:
        if show_pin:
            e.config(show="*")
        else:   
            e.config(show="")
root = tk.Tk()
root.title("ATM PIN Kontrol")
root.geometry("350x140")
root.bind("<Return>", lambda event: control())

label = tk.Label(root, text="4 Haneli PIN kodunuzu girin:")
label.pack(pady=10)

vcmd = root.register(onedigit)

frame = tk.Frame(root)
frame.pack()

entries = []
for i in range(4):
    e = tk.Entry(frame, width=2, font=("Arial", 24), justify="center", validate="key",
                 validatecommand=(vcmd, "%P"), show="*")
    e.pack(side="left", padx=5)
    e.bind("<KeyRelease>", lambda event, idx=i: jump(event, idx))
    entries.append(e)
    entries[0].focus_set()

eye_button = tk.Button(frame, text="👁‍🗨", command=toggle_show, font=("Arial", 15))
eye_button.pack(side="right", padx=10, pady=(0, 10))

control_button = tk.Button(root, text="Kontrol Et", command=control, font=("Arial", 14))
control_button.pack(pady=10)

show_pin = False

root.mainloop()