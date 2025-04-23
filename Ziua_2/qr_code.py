import pyqrcode
import tkinter as tk


def generate_qr_code(url, file_name):
        print("Generating QR Code...")
        qrcode = pyqrcode.create(url)
        img = qrcode.png(file_name+".png", scale=5)
        return img

def main():
    root = tk.Tk()
    root.title("QR Code Generator")
    root.geometry("300x200")
    url_label = tk.Label(root, text="Enter URL:")
    url_label.pack()
    url_entry = tk.Entry(root)
    url_entry.pack()

    # generate name for the file
    # generate entry for the file name
    file_name_label = tk.Label(root, text="Enter File Name:")
    file_name_label.pack()
    file_name_entry = tk.Entry(root)
    file_name_entry.pack()
    # autocomplete the file name with the url domain name
    file_name_entry.insert(0, url_entry.get().split("/")[-1])

    # vreau autocomplete cand se schimba url-ul: sa se stearga existenta si sa se adauge noua
    url_entry.bind("<KeyRelease>", lambda event:  file_name_entry.insert(0, url_entry.get().split("/")[-1]))


    generate_button = tk.Button(root, text="Generate QR Code", command=lambda: generate_qr_code(url_entry.get(), file_name_entry.get()))
    generate_button.pack()
 

    root.mainloop()

main()