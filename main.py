import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark Application")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")
        
        self.image = None
        self.image_path = None
        
        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.upload_button.pack(pady=20)
        
        self.watermark_label = tk.Label(root, text="Enter Watermark Text:", bg="#f0f0f0", font=("Arial", 12))
        self.watermark_label.pack(pady=5)
        
        self.watermark_text = tk.Entry(root, font=("Arial", 12))
        self.watermark_text.pack(pady=5)
        
        self.add_watermark_button = tk.Button(root, text="Add Watermark", command=self.add_watermark, bg="#2196F3", fg="white", font=("Arial", 12))
        self.add_watermark_button.pack(pady=20)
        
        self.save_button = tk.Button(root, text="Save Image", command=self.save_image, bg="#FF5722", fg="white", font=("Arial", 12))
        self.save_button.pack(pady=10)

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if self.image_path:
            self.image = Image.open(self.image_path)
            messagebox.showinfo("Success", "Image uploaded successfully!")

    def add_watermark(self):
        if not self.image:
            messagebox.showerror("Error", "No image uploaded!")
            return
        
        watermark_text = self.watermark_text.get()
        if not watermark_text:
            messagebox.showerror("Error", "Watermark text is empty!")
            return
        
        image_copy = self.image.copy()
        draw = ImageDraw.Draw(image_copy)
        
        try:
            font = ImageFont.truetype("arial.ttf", 36)
        except IOError:
            font = ImageFont.load_default()
        
        text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        width, height = image_copy.size
        x = width - text_width - 10
        y = height - text_height - 10
        
        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))
        
        self.image = image_copy
        messagebox.showinfo("Success", "Watermark added successfully!")

    def save_image(self):
        if not self.image:
            messagebox.showerror("Error", "No image to save!")
            return
        
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg")])
        
        if save_path:
            self.image.save(save_path)
            messagebox.showinfo("Success", f"Image saved successfully at {save_path}!")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
