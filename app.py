import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import matplotlib
matplotlib.use('TkAgg')  # Use the TkAgg backend for GUI support

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class TowelDataVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Towel Data Visualizer")
        self.root.geometry("500x400")

        self.file_path = None
        self.data = None

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Don't Panic! Select a CSV file to visualize.")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(self.root, text="Browse CSV", command=self.browse_file)
        self.browse_button.pack(pady=5)

        self.plot_options_frame = tk.Frame(self.root)
        self.plot_options_frame.pack(pady=10)

        self.plot_type_label = tk.Label(self.plot_options_frame, text="Select Plot Type:")
        self.plot_type_label.grid(row=0, column=0, padx=5, pady=5)

        self.plot_type_var = tk.StringVar()
        self.plot_type_combobox = ttk.Combobox(
            self.plot_options_frame, textvariable=self.plot_type_var, state='readonly'
        )
        self.plot_type_combobox['values'] = (
            'Histogram', 'Scatter Plot', 'Box Plot', 'Correlation Heatmap'
        )
        self.plot_type_combobox.current(0)
        self.plot_type_combobox.grid(row=0, column=1, padx=5, pady=5)

        self.x_axis_label = tk.Label(self.plot_options_frame, text="X-axis:")
        self.x_axis_label.grid(row=1, column=0, padx=5, pady=5)
        self.x_axis_var = tk.StringVar()
        self.x_axis_combobox = ttk.Combobox(
            self.plot_options_frame, textvariable=self.x_axis_var, state='disabled'
        )
        self.x_axis_combobox.grid(row=1, column=1, padx=5, pady=5)

        self.y_axis_label = tk.Label(self.plot_options_frame, text="Y-axis:")
        self.y_axis_label.grid(row=2, column=0, padx=5, pady=5)
        self.y_axis_var = tk.StringVar()
        self.y_axis_combobox = ttk.Combobox(
            self.plot_options_frame, textvariable=self.y_axis_var, state='disabled'
        )
        self.y_axis_combobox.grid(row=2, column=1, padx=5, pady=5)

        self.plot_button = tk.Button(
            self.root, text="Plot Data", command=self.plot_data, state=tk.DISABLED
        )
        self.plot_button.pack(pady=5)

        self.plot_type_combobox.bind("<<ComboboxSelected>>", self.on_plot_type_change)

    def browse_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.file_path:
            try:
                self.data = pd.read_csv(self.file_path)
                messagebox.showinfo("Success", "CSV file loaded successfully!")
                self.plot_button.config(state=tk.NORMAL)

                columns = self.data.columns.tolist()
                self.x_axis_combobox['values'] = columns
                self.y_axis_combobox['values'] = columns
                self.x_axis_combobox.config(state='readonly')
                self.y_axis_combobox.config(state='readonly')
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load CSV file.\n{e}")
                self.plot_button.config(state=tk.DISABLED)

    def on_plot_type_change(self, event):
        plot_type = self.plot_type_var.get()
        if plot_type in ['Histogram', 'Box Plot']:
            self.x_axis_label.config(text="Column:")
            self.y_axis_label.grid_remove()
            self.y_axis_combobox.grid_remove()
            self.x_axis_label.grid()
            self.x_axis_combobox.grid()
        elif plot_type == 'Scatter Plot':
            self.x_axis_label.config(text="X-axis:")
            self.y_axis_label.grid()
            self.y_axis_combobox.grid()
            self.x_axis_label.grid()
            self.x_axis_combobox.grid()
        elif plot_type == 'Correlation Heatmap':
            self.x_axis_label.grid_remove()
            self.x_axis_combobox.grid_remove()
            self.y_axis_label.grid_remove()
            self.y_axis_combobox.grid_remove()

    def plot_data(self):
        if self.data is not None:
            plot_type = self.plot_type_var.get()
            if plot_type == 'Histogram':
                column = self.x_axis_var.get()
                if column:
                    plt.figure()
                    self.data[column].hist(bins=20)
                    plt.title(f'Histogram of {column}')
                    plt.xlabel(column)
                    plt.ylabel('Frequency')
                    plt.show()
                else:
                    messagebox.showwarning("No Column Selected", "Please select a column for the histogram.")
            elif plot_type == 'Scatter Plot':
                x_col = self.x_axis_var.get()
                y_col = self.y_axis_var.get()
                if x_col and y_col:
                    plt.figure()
                    plt.scatter(self.data[x_col], self.data[y_col])
                    plt.title(f'Scatter Plot of {y_col} vs {x_col}')
                    plt.xlabel(x_col)
                    plt.ylabel(y_col)
                    plt.show()
                else:
                    messagebox.showwarning("Columns Not Selected", "Please select columns for X and Y axes.")
            elif plot_type == 'Box Plot':
                column = self.x_axis_var.get()
                if column:
                    plt.figure()
                    sns.boxplot(y=self.data[column])
                    plt.title(f'Box Plot of {column}')
                    plt.ylabel(column)
                    plt.show()
                else:
                    messagebox.showwarning("No Column Selected", "Please select a column for the box plot.")
            elif plot_type == 'Correlation Heatmap':
                numeric_columns = self.data.select_dtypes(include=['number']).columns
                if len(numeric_columns) < 2:
                    messagebox.showwarning(
                        "Not Enough Data",
                        "The dataset does not have enough numeric columns to plot a correlation heatmap."
                    )
                    return
                correlation_matrix = self.data[numeric_columns].corr()
                plt.figure(figsize=(10, 8))
                sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
                plt.title('Correlation Heatmap')
                plt.show()
        else:
            messagebox.showwarning("No Data", "Please load a CSV file first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TowelDataVisualizer(root)
    root.mainloop()
