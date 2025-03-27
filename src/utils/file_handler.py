def read_file(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")

def save_output_file(file_path: str, content: str) -> None:
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def select_file_dialog() -> str:
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(
        title="Select Text File",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )