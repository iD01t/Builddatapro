import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox


def build_command(script_path: str, output_dir: str, *, onefile: bool = True,
                  windowed: bool = True, icon: str | None = None, additional: str = "") -> list[str]:
    """Construct the pyinstaller command for building an executable."""
    cmd = ["pyinstaller", script_path, f"--distpath={output_dir}"]
    if onefile:
        cmd.append("--onefile")
    if windowed:
        cmd.append("--noconsole")
    if icon:
        cmd.append(f"--icon={icon}")
    if additional:
        cmd.extend(additional.split())
    return cmd


def build_exe(*args, **kwargs) -> subprocess.CompletedProcess:
    """Run PyInstaller with the given options and return the CompletedProcess."""
    cmd = build_command(*args, **kwargs)
    return subprocess.run(cmd, capture_output=True, text=True)


class BuilderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EXE Builder")
        self.geometry("500x300")

        # Script selection
        tk.Label(self, text="Python Script:").pack(anchor="w", padx=10, pady=(10, 0))
        frame1 = tk.Frame(self)
        frame1.pack(fill="x", padx=10)
        self.script_var = tk.StringVar()
        tk.Entry(frame1, textvariable=self.script_var).pack(side="left", fill="x", expand=True)
        tk.Button(frame1, text="Browse", command=self.select_script).pack(side="left", padx=5)

        # Output dir
        tk.Label(self, text="Output Directory:").pack(anchor="w", padx=10, pady=(10, 0))
        frame2 = tk.Frame(self)
        frame2.pack(fill="x", padx=10)
        self.output_var = tk.StringVar(value=os.getcwd())
        tk.Entry(frame2, textvariable=self.output_var).pack(side="left", fill="x", expand=True)
        tk.Button(frame2, text="Browse", command=self.select_output).pack(side="left", padx=5)

        # Icon file
        tk.Label(self, text="Icon (optional):").pack(anchor="w", padx=10, pady=(10, 0))
        frame3 = tk.Frame(self)
        frame3.pack(fill="x", padx=10)
        self.icon_var = tk.StringVar()
        tk.Entry(frame3, textvariable=self.icon_var).pack(side="left", fill="x", expand=True)
        tk.Button(frame3, text="Browse", command=self.select_icon).pack(side="left", padx=5)

        # Options
        self.onefile_var = tk.BooleanVar(value=True)
        self.windowed_var = tk.BooleanVar(value=True)
        tk.Checkbutton(self, text="One File", variable=self.onefile_var).pack(anchor="w", padx=10)
        tk.Checkbutton(self, text="Windowed (no console)", variable=self.windowed_var).pack(anchor="w", padx=10)

        tk.Label(self, text="Additional Args:").pack(anchor="w", padx=10)
        self.additional_var = tk.StringVar()
        tk.Entry(self, textvariable=self.additional_var).pack(fill="x", padx=10)

        tk.Button(self, text="Build", command=self.run_build).pack(pady=15)

    def select_script(self):
        path = filedialog.askopenfilename(filetypes=[("Python files", "*.py"), ("All files", "*.*")])
        if path:
            self.script_var.set(path)

    def select_output(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_var.set(directory)

    def select_icon(self):
        path = filedialog.askopenfilename(filetypes=[("Icon files", "*.ico"), ("All files", "*.*")])
        if path:
            self.icon_var.set(path)

    def run_build(self):
        script = self.script_var.get()
        output = self.output_var.get()
        icon = self.icon_var.get() or None
        try:
            result = build_exe(script, output, onefile=self.onefile_var.get(),
                               windowed=self.windowed_var.get(), icon=icon,
                               additional=self.additional_var.get())
            if result.returncode == 0:
                messagebox.showinfo("Success", "Build completed successfully!")
            else:
                messagebox.showerror("Error", result.stderr)
        except Exception as e:
            messagebox.showerror("Error", str(e))


def main():
    app = BuilderApp()
    app.mainloop()


if __name__ == "__main__":
    main()
