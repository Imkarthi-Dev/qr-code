import qrcode
import os
import tkinter as tk
root = tk.Tk()
root.geometry("200x200")
qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=5
    )
name_var = tk.StringVar()
data_var = tk.StringVar()

def btn():
    data = data_var.get()
    name = name_var.get()
    while (True):
        qr.add_data(data)
        #qr.add_data(name)
        qr.make(fit=True)
        img = qr.make_image(fill='black',back_color='white')
        img.save('./QR_code/QR_code_'+str(name)+'.png')
        break

    #crating label

name_label=tk.Label(root,text='name',font=('calibre',10,'bold'))

    #creating entry

name_entry =tk.Entry(root,textvariable= name_var,font=('calibre',10,'normal'))

    #creating label

data_label= tk.Label(root,text='data',font=('calibre',10,'bold'))

    #creating entry

data_entry =tk.Entry(root,textvariable= data_var,font=('calibre',10,'normal'))

    #creating button
sub_btn=tk.Button(root,text='Generate',bg='red',command = btn)

ext_btn =tk.Button(root, text = "Exit",command = root.destroy)

    #required positin using grid

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
data_label.grid(row=1,column=0)
data_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
ext_btn.grid(row=3,column=1)

root.title('QR Code')
root.mainloop()        

#if __name__=='__main__':
      # btn()
    
    

