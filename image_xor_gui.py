import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def xor_image(file_path, key, mode):
    try:
        img = Image.open(file_path)
        img = img.convert("RGB")
        pixels = img.load()

        width, height = img.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                if mode == "Encrypt":
                    pixels[x, y] = (r ^ key, g ^ key, b ^ key)
                elif mode == "Decrypt":
                    pixels[x, y] = (r ^ key, g ^ key, b ^ key)

        output_path = file_path.rsplit(".", 1)[0] + f"_{mode.lower()}.png"
        img.save(output_path)
        return output_path
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")
        return None

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)

def run_xor():
    file_path = entry_file_path.get()
    key_str = entry_key.get()
    mode = mode_var.get()

    if not file_path or not key_str:
        messagebox.showwarning("Input Error", "Please select an image and enter a key.")
        return

    try:
        key = int(key_str)
        if not (0 <= key <= 255):
            raise ValueError
    except ValueError:
        messagebox.showerror("Key Error", "Key must be an integer between 0 and 255.")
        return

    output_path = xor_image(file_path, key, mode)
    if output_path:
        messagebox.showinfo("Success", f"{mode}ion complete!\nSaved as:\n{output_path}")

# GUI Setup
root = tk.Tk()
root.title("Image Encryptor/Decryptor (XOR) - Prodigy InfoTech")
root.geometry("500x250")
root.resizable(False, False)

tk.Label(root, text="Select Image:").pack(pady=(10, 0))
entry_file_path = tk.Entry(root, width=60)
entry_file_path.pack()
tk.Button(root, text="Browse", command=browse_file).pack(pady=5)

tk.Label(root, text="Secret Key (0-255):").pack()
entry_key = tk.Entry(root, width=10)
entry_key.pack()

mode_var = tk.StringVar(value="Encrypt")
tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="Encrypt").pack()
tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="Decrypt").pack()

tk.Button(root, text="Run", command=run_xor, width=15).pack(pady=15)

root.mainloop()
