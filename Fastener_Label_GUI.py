import os
import tkinter as tk
from tkinter import filedialog, messagebox
from fastener_label_generator import FastenerLabelGenerator

BASE_DIR = os.path.abspath("fastener_label_generator/")
SCREW_DIR = os.path.join(BASE_DIR, "assets/screws")
DRIVE_DIR = os.path.join(BASE_DIR, "assets/bits")

class LabelGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fastener Label Generator")
        
        self.fields = {
            "size": tk.StringVar(),
            "screw_image": tk.StringVar(),
            "drive_image": tk.StringVar(),
            "drive_name_and_size": tk.StringVar(),
            "material": tk.StringVar(),
            "coating": tk.StringVar(),
            "strength_class": tk.StringVar(),
            "norms": tk.StringVar()
        }
        
        row = 0
        for field, var in self.fields.items():
            tk.Label(root, text=field.replace("_", " ").capitalize()).grid(row=row, column=0, padx=5, pady=5)
            entry = tk.Entry(root, textvariable=var)
            entry.grid(row=row, column=1, padx=5, pady=5)
            if "image" in field:
                tk.Button(root, text="Select", command=lambda f=field: self.select_file(f)).grid(row=row, column=2, padx=5, pady=5)
            row += 1
        
        tk.Button(root, text="Clear All", command=self.clear_all).grid(row=row, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Generate PDF", command=self.generate_pdf).grid(row=row, column=1, columnspan=2, pady=10)
        
    def select_file(self, field):
        initial_dir = SCREW_DIR if "screw" in field else DRIVE_DIR
        filepath = filedialog.askopenfilename(initialdir=initial_dir, filetypes=[("Image files", "*.svg"), ("Image files", "*.png")])
        if filepath:
            # Extract only the filename with its extension
            filename = os.path.basename(filepath)
            self.fields[field].set(filename)

    
    def clear_all(self):
        for var in self.fields.values():
            var.set("")
    
    def generate_pdf(self):
        output_filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if not output_filename:
            return
        
        fields_data = {key: var.get() for key, var in self.fields.items()}
        try:
            pdf_content = FastenerLabelGenerator.generate_pdf("main", "main", [fields_data])
            with open(output_filename, "wb") as f:
                f.write(pdf_content)
            messagebox.showinfo("Success", "PDF Generated Successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate PDF: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LabelGeneratorApp(root)
    root.mainloop()
