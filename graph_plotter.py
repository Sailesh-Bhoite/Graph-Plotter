import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def line_plot():
    line_window = tk.Toplevel()
    line_window.title("Line Graph")
    line_window.geometry(inner_window_dimension)

    def plot_line_graph():
        values = x_values_entry.get()
        vl = values.split(',')
        value_list = [int(x) for x in vl]
        names = y_values_entry.get()
        nl = names.split(',')
        name_list = [int(x) for x in nl]

        # Clear the previous plot
        for widget in output_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots()
        fig.patch.set_facecolor('#808080')
        ax.plot(value_list, name_list, color="green")
        ax.set_title(graph_title.get(), fontsize=25, fontweight='bold')
        ax.set_xlabel(x_name.get())
        ax.set_ylabel(y_name.get())
        line_canvas = FigureCanvasTkAgg(fig, master=output_frame)
        line_canvas.draw()
        line_canvas.get_tk_widget().pack(pady=40)

        save_as_name = ttk.Entry(output_frame)
        save_as_name.pack(pady=3)
        save_btn = ttk.Button(output_frame, text="Save as PNG", padding=10,
                              command=lambda: save_figures(fig, save_as_name), style="btn.TButton")
        save_btn.pack(pady=10)

    def save_figures(fig, save_as_name):
        if save_as_name.get() == "":
            messagebox.showerror("Error!!!", "Please enter a name to save")
        else:
            fig.savefig(f"{save_as_name.get()}.png")
            messagebox.showinfo("Figure Saved", f"Figure saved as \"{save_as_name.get()}.png\"")

    line_style = ttk.Style()
    line_style.configure("l_input.TFrame", background="#4f4f4f")
    line_style.configure("l_output.TFrame", background="#383838")
    line_style.configure("l_content.TLabel", background="#4f4f4f", font=8)
    line_style.configure("btn.TButton", font=10)

    # Input frame and widgets
    input_frame = ttk.Frame(line_window, style="l_input.TFrame")
    input_frame.pack(side="left", fill="both")

    title = ttk.Label(input_frame, text="Line Graph", font=("Arial", 50), background="#4f4f4f", padding=20)
    title.pack(padx=60, pady=50)

    graph_title_label = ttk.Label(input_frame, text="Enter Graph Title:", style="l_content.TLabel")
    graph_title_label.pack()
    graph_title = ttk.Entry(input_frame)
    graph_title.pack(pady=15)

    x_name_label = ttk.Label(input_frame, text="Enter the X axis name:", style="l_content.TLabel")
    x_name_label.pack()
    x_name = ttk.Entry(input_frame, width=20)
    x_name.pack(pady=15)

    y_name_label = ttk.Label(input_frame, text="Enter the Y axis name:", style="l_content.TLabel")
    y_name_label.pack()
    y_name = ttk.Entry(input_frame, width=20)
    y_name.pack(pady=15)

    x_value_label = ttk.Label(input_frame, text="Enter comma-separated X co-ordinates:", style="l_content.TLabel")
    x_value_label.pack()

    x_values_entry = ttk.Entry(input_frame, width=40)
    x_values_entry.pack(pady=15)

    y_values_label = ttk.Label(input_frame, text="Enter comma-separated Y co-ordinates:", style="l_content.TLabel")
    y_values_label.pack()

    y_values_entry = ttk.Entry(input_frame, width=40)
    y_values_entry.pack(pady=15)

    # Output frame and matplotlib plot
    output_frame = ttk.Frame(line_window, style="l_output.TFrame")
    output_frame.pack(side="right", fill="both", expand=True)

    # Button to trigger plot
    btn = ttk.Button(input_frame, text="Plot", command=plot_line_graph, padding=10, style="btn.TButton")
    btn.pack(pady=15)


def area_plot():
    area_window = tk.Toplevel()
    area_window.title("Area Graph")
    area_window.geometry(inner_window_dimension)

    def plot_area_graph():
        values = x_values_entry.get()
        vl = values.split(',')
        value_list = [int(x) for x in vl]
        names = y_values_entry.get()
        nl = names.split(',')
        name_list = [int(x) for x in nl]

        # Clear the previous plot
        for widget in output_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots()
        fig.patch.set_facecolor('#89cff0')
        ax.fill_between(value_list, name_list, color="green", alpha=0.6)
        ax.set_title(graph_title.get(), fontsize=25, fontweight='bold')
        ax.set_xlabel(x_name.get())
        ax.set_ylabel(y_name.get())
        area_canvas = FigureCanvasTkAgg(fig, master=output_frame)
        area_canvas.draw()
        area_canvas.get_tk_widget().pack(pady=40)

        save_as_name = ttk.Entry(output_frame)
        save_as_name.pack(pady=3)
        save_btn = ttk.Button(output_frame, text="Save as PNG", padding=10, command=lambda: save_figures(fig, save_as_name), style="btn.TButton")
        save_btn.pack(pady=10)

    def save_figures(fig, save_as_name):
        if save_as_name.get() == "":
            messagebox.showerror("Error!!!", "Please enter a name to save")
        else:
            fig.savefig(f"{save_as_name.get()}.png")
            messagebox.showinfo("Figure Saved", f"Figure saved as \"{save_as_name.get()}.png\"")

    area_style = ttk.Style()
    area_style.configure("a_input.TFrame", background="#1b7ced")
    area_style.configure("a_output.TFrame", background="#104abe")
    area_style.configure("a_content.TLabel", background="#1b7ced", font=8)
    area_style.configure("btn.TButton", font=10)

    # Input frame and widgets
    input_frame = ttk.Frame(area_window, style="a_input.TFrame")
    input_frame.pack(side="left", fill="both")

    title = ttk.Label(input_frame, text="Area Graph", font=("Arial", 50), background="#1b7ced", padding=20)
    title.pack(padx=60, pady=50)

    graph_title_label = ttk.Label(input_frame, text="Enter Graph Title:", style="a_content.TLabel")
    graph_title_label.pack()
    graph_title = ttk.Entry(input_frame)
    graph_title.pack(pady=15)

    x_name_label = ttk.Label(input_frame, text="Enter the X axis name:", style="a_content.TLabel")
    x_name_label.pack()
    x_name = ttk.Entry(input_frame, width=20)
    x_name.pack(pady=15)

    y_name_label = ttk.Label(input_frame, text="Enter the Y axis name:", style="a_content.TLabel")
    y_name_label.pack()
    y_name = ttk.Entry(input_frame, width=20)
    y_name.pack(pady=15)

    x_value_label = ttk.Label(input_frame, text="Enter comma-separated X co-ordinates:", style="a_content.TLabel")
    x_value_label.pack()

    x_values_entry = ttk.Entry(input_frame, width=40)
    x_values_entry.pack(pady=15)

    y_values_label = ttk.Label(input_frame, text="Enter comma-separated Y co-ordinates:", style="a_content.TLabel")
    y_values_label.pack()

    y_values_entry = ttk.Entry(input_frame, width=40)
    y_values_entry.pack(pady=15)

    # Output frame and matplotlib plot
    output_frame = ttk.Frame(area_window, style="a_output.TFrame")
    output_frame.pack(side="right", fill="both", expand=True)

    # Button to trigger plot
    btn = ttk.Button(input_frame, text="Plot", command=plot_area_graph, padding=10, style="btn.TButton")
    btn.pack(pady=15)


def v_bar_chart():
    v_bar_window = tk.Toplevel()
    v_bar_window.title("Vertical Bar Chart")
    v_bar_window.geometry(inner_window_dimension)

    def plot_v_bar_graph():
        values = values_entry.get()
        vl = values.split(',')
        value_list = [int(x) for x in vl]
        names = names_entry.get()
        nl = names.split(',')
        name_list = [x.strip() for x in nl]

        # Clear the previous plot
        for widget in output_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots()
        fig.patch.set_facecolor('#ffb7c5')
        ax.bar(name_list, value_list, color="#ff6e00")
        ax.set_title(graph_title.get(), fontsize=25, fontweight='bold')
        ax.set_xlabel(x_name.get())
        ax.set_ylabel(y_name.get())
        bar_canvas = FigureCanvasTkAgg(fig, master=output_frame)
        bar_canvas.draw()
        bar_canvas.get_tk_widget().pack(pady=40)

        save_as_name = ttk.Entry(output_frame)
        save_as_name.pack(pady=3)
        save_btn = ttk.Button(output_frame, text="Save as PNG", padding=10, command=lambda: save_figures(fig, save_as_name), style="contents.TButton")
        save_btn.pack()

    def save_figures(fig, save_as_name):
        if save_as_name.get() == "":
            messagebox.showerror("Error!!!", "Please enter a name")
        else:
            fig.savefig(f"{save_as_name.get()}.png")
            messagebox.showinfo("Figure Saved", f"Figure saved as {save_as_name.get()}")

    # Styling Objects
    bar_style = ttk.Style()
    bar_style.configure("vb_input.TFrame", background="#ff5ccd")
    bar_style.configure("vb_output.TFrame", background="#ff028d")
    bar_style.configure("vb_content.TLabel", background="#ff5ccd", font=8)

    # Input frame and widgets
    input_frame = ttk.Frame(v_bar_window, style="vb_input.TFrame")
    input_frame.pack(side="left", fill="both")

    title = ttk.Label(input_frame, text="Vertical\nBar Plot", font=("Arial", 50), background="#ff5ccd", padding=(20, 5))
    title.pack(padx=60, pady=50)

    graph_title_label = ttk.Label(input_frame, text="Enter Graph Title:", style="vb_content.TLabel")
    graph_title_label.pack()
    graph_title = ttk.Entry(input_frame)
    graph_title.pack(pady=10)

    x_name_label = ttk.Label(input_frame, text="Enter the X axis name:", style="vb_content.TLabel")
    x_name_label.pack()
    x_name = ttk.Entry(input_frame, width=20)
    x_name.pack(pady=10)

    y_name_label = ttk.Label(input_frame, text="Enter the Y axis name:", style="vb_content.TLabel")
    y_name_label.pack()
    y_name = ttk.Entry(input_frame, width=20)
    y_name.pack(pady=10)

    value_label = ttk.Label(input_frame, text="Enter Values:", style="vb_content.TLabel")
    value_label.pack()

    values_entry = ttk.Entry(input_frame, width=40)
    values_entry.pack(pady=10)

    names_label = ttk.Label(input_frame, text="Enter Corresponding Names:", style="vb_content.TLabel")
    names_label.pack()

    names_entry = ttk.Entry(input_frame, width=40)
    names_entry.pack(pady=10)

    # Output frame and matplotlib plot
    output_frame = ttk.Frame(v_bar_window, style="vb_output.TFrame")
    output_frame.pack(side="right", fill="both", expand=True)

    # Button to trigger plot
    btn = ttk.Button(input_frame, text="Plot", padding=10, command=plot_v_bar_graph, style="contents.TButton")
    btn.pack(pady=15)


def h_bar_chart():
    h_bar_window = tk.Toplevel()
    h_bar_window.title("Horizontal Bar Chart")
    h_bar_window.geometry(inner_window_dimension)

    def plot_h_bar_graph():
        values = values_entry.get()
        vl = values.split(',')
        value_list = [int(x) for x in vl]
        names = names_entry.get()
        nl = names.split(',')
        name_list = [x.strip() for x in nl]

        # Clear the previous plot
        for widget in output_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots()
        fig.patch.set_facecolor('#ffffe0')
        ax.barh(name_list, value_list, color="#ff6e00")
        ax.set_title(graph_title.get(), fontsize=25, fontweight='bold')
        ax.set_xlabel(x_name.get())
        ax.set_ylabel(y_name.get())
        bar_canvas = FigureCanvasTkAgg(fig, master=output_frame)
        bar_canvas.draw()
        bar_canvas.get_tk_widget().pack(pady=40)

        save_as_name = ttk.Entry(output_frame)
        save_as_name.pack(pady=3)
        save_btn = ttk.Button(output_frame, text="Save as PNG", padding=10, command=lambda: save_figures(fig, save_as_name), style="contents.TButton")
        save_btn.pack()

    def save_figures(fig, save_as_name):
        if save_as_name.get() == "":
            messagebox.showerror("Error!!!", "Please enter a name")
        else:
            fig.savefig(f"{save_as_name.get()}.png")
            messagebox.showinfo("Figure Saved", f"Figure saved as {save_as_name.get()}")

    # Styling Objects
    bar_style = ttk.Style()
    bar_style.configure("hb_input.TFrame", background="light yellow")
    bar_style.configure("hb_output.TFrame", background="yellow")
    bar_style.configure("hb_content.TLabel", background="light yellow", font=8)

    # Input frame and widgets
    input_frame = ttk.Frame(h_bar_window, style="hb_input.TFrame")
    input_frame.pack(side="left", fill="both")

    title = ttk.Label(input_frame, text="Horizontal\nBar Plot", font=("Arial", 50), background="light yellow", padding=(20, 5))
    title.pack(padx=60, pady=50)

    graph_title_label = ttk.Label(input_frame, text="Enter Graph Title:", style="hb_content.TLabel")
    graph_title_label.pack()
    graph_title = ttk.Entry(input_frame)
    graph_title.pack(pady=10)

    x_name_label = ttk.Label(input_frame, text="Enter the X axis name:", style="hb_content.TLabel")
    x_name_label.pack()
    x_name = ttk.Entry(input_frame, width=20)
    x_name.pack(pady=10)

    y_name_label = ttk.Label(input_frame, text="Enter the Y axis name:", style="hb_content.TLabel")
    y_name_label.pack()
    y_name = ttk.Entry(input_frame, width=20)
    y_name.pack(pady=10)

    value_label = ttk.Label(input_frame, text="Enter Values:", style="hb_content.TLabel")
    value_label.pack()

    values_entry = ttk.Entry(input_frame, width=40)
    values_entry.pack(pady=10)

    names_label = ttk.Label(input_frame, text="Enter Corresponding Names:", style="hb_content.TLabel")
    names_label.pack()

    names_entry = ttk.Entry(input_frame, width=40)
    names_entry.pack(pady=10)

    # Output frame and matplotlib plot
    output_frame = ttk.Frame(h_bar_window, style="hb_output.TFrame")
    output_frame.pack(side="right", fill="both", expand=True)

    # Button to trigger plot
    btn = ttk.Button(input_frame, text="Plot", padding=10, command=plot_h_bar_graph, style="contents.TButton")
    btn.pack(pady=15)


def scatter_plot():
    scatter_window = tk.Toplevel()
    scatter_window.title("Histogram Chart")
    scatter_window.geometry(inner_window_dimension)

    def plot_scatter_graph():
        values = x_values_entry.get()
        vl = values.split(',')
        value_list = [int(x) for x in vl]
        names = y_values_entry.get()
        nl = names.split(',')
        name_list = [int(x) for x in nl]

        # Clear the previous plot
        for widget in output_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots()
        fig.patch.set_facecolor('#f6cafe')
        ax.scatter(name_list, value_list)
        ax.set_title(graph_title.get(), fontsize=25, fontweight='bold')
        ax.set_xlabel(x_name.get())
        ax.set_ylabel(y_name.get())
        bar_canvas = FigureCanvasTkAgg(fig, master=output_frame)
        bar_canvas.draw()
        bar_canvas.get_tk_widget().pack(pady=40)

        save_as_name = ttk.Entry(output_frame)
        save_as_name.pack(pady=3)
        save_btn = ttk.Button(output_frame, text="Save as PNG", padding=10,
                              command=lambda: save_figures(fig, save_as_name), style="contents.TButton")
        save_btn.pack(pady=10)

    def save_figures(fig, save_as_name):
        if save_as_name.get() == "":
            messagebox.showerror("Error!!!", "Please enter a name to save")
        else:
            fig.savefig(f"{save_as_name.get()}.png")
            messagebox.showinfo("Figure Saved", f"Figure saved as \"{save_as_name.get()}.png\"")

    scatter_style = ttk.Style()
    scatter_style.configure("s_input.TFrame", background="#e142fc")
    scatter_style.configure("s_output.TFrame", background="#b303d0")
    scatter_style.configure("s_content.TLabel", background="#e142fc", font=8)

    # Input frame and widgets
    input_frame = ttk.Frame(scatter_window, style="s_input.TFrame")
    input_frame.pack(side="left", fill="both")

    title = ttk.Label(input_frame, text="Scatter Plot", font=("Arial", 50), background="#e142fc", padding=20)
    title.pack(padx=60, pady=50)

    graph_title_label = ttk.Label(input_frame, text="Enter Graph Title:", style="s_content.TLabel")
    graph_title_label.pack()
    graph_title = ttk.Entry(input_frame)
    graph_title.pack(pady=15)

    x_name_label = ttk.Label(input_frame, text="Enter the X axis name:", style="s_content.TLabel")
    x_name_label.pack()
    x_name = ttk.Entry(input_frame, width=20)
    x_name.pack(pady=15)

    y_name_label = ttk.Label(input_frame, text="Enter the Y axis name:", style="s_content.TLabel")
    y_name_label.pack()
    y_name = ttk.Entry(input_frame, width=20)
    y_name.pack(pady=15)

    x_value_label = ttk.Label(input_frame, text="Enter comma-separated X co-ordinates:", style="s_content.TLabel")
    x_value_label.pack()

    x_values_entry = ttk.Entry(input_frame, width=40)
    x_values_entry.pack(pady=15)

    y_values_label = ttk.Label(input_frame, text="Enter comma-separated Y co-ordinates:", style="s_content.TLabel")
    y_values_label.pack()

    y_values_entry = ttk.Entry(input_frame, width=40)
    y_values_entry.pack(pady=15)

    # Output frame and matplotlib plot
    output_frame = ttk.Frame(scatter_window, style="s_output.TFrame")
    output_frame.pack(side="right", fill="both", expand=True)

    # Button to trigger plot
    btn = ttk.Button(input_frame, text="Plot", command=plot_scatter_graph, padding=10, style="contents.TButton")
    btn.pack(pady=15)


def histogram_plot():
    hist_window = tk.Toplevel()
    hist_window.title("Histogram Chart")
    hist_window.geometry(inner_window_dimension)

    def plot_histogram_graph():
        values = values_entry.get()
        vl = values.split(',')
        value_list = [int(x) for x in vl]
        number_of_bins = int(bins_entry.get())

        # Clear the previous plot
        for widget in output_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots()
        fig.patch.set_facecolor('#f09796')
        ax.hist(value_list, bins=number_of_bins, edgecolor='black', color="#4cc9f0")
        ax.set_title(graph_title.get(), fontsize=25, fontweight='bold')
        ax.set_xlabel("Values")
        ax.set_ylabel("Frequencies")
        hist_canvas = FigureCanvasTkAgg(fig, master=output_frame)
        hist_canvas.draw()
        hist_canvas.get_tk_widget().pack(pady=40)

        save_as_name = ttk.Entry(output_frame)
        save_as_name.pack(pady=3)
        save_btn = ttk.Button(output_frame, text="Save as PNG", padding=10,
                              command=lambda: save_figures(fig, save_as_name), style="contents.TButton")
        save_btn.pack()

    def save_figures(fig, save_as_name):
        if save_as_name.get() == "":
            messagebox.showerror("Error!!!", "Please enter a name")
        else:
            fig.savefig(f"{save_as_name.get()}.png")
            messagebox.showinfo("Figure Saved", f"Figure saved as {save_as_name.get()}")

    # Styling Objects
    hist_style = ttk.Style()
    hist_style.configure("h_input.TFrame", background="#ea3b52")
    hist_style.configure("h_output.TFrame", background="#b30000")
    hist_style.configure("h_content.TLabel", background="#ea3b52", font=8)

    # Input frame and widgets
    input_frame = ttk.Frame(hist_window, style="h_input.TFrame")
    input_frame.pack(side="left", fill="both")

    title = ttk.Label(input_frame, text="Histogram", font=("Arial", 50), background="#ea3b52", padding=20)
    title.pack(padx=60, pady=50)

    graph_title_label = ttk.Label(input_frame, text="Enter Graph Title:", style="h_content.TLabel")
    graph_title_label.pack()
    graph_title = ttk.Entry(input_frame)
    graph_title.pack(pady=10)

    value_label = ttk.Label(input_frame, text="Enter Values:", style="h_content.TLabel")
    value_label.pack()

    values_entry = ttk.Entry(input_frame, width=40)
    values_entry.pack(pady=10)

    bins_label = ttk.Label(input_frame, text="Enter bins:", style="h_content.TLabel")
    bins_label.pack()

    bins_entry = ttk.Entry(input_frame, width=40)
    bins_entry.pack(pady=10)

    # Output frame and matplotlib plot
    output_frame = ttk.Frame(hist_window, style="h_output.TFrame")
    output_frame.pack(side="right", fill="both", expand=True)

    # Button to trigger plot
    btn = ttk.Button(input_frame, text="Plot", padding=10, command=plot_histogram_graph, style="contents.TButton")
    btn.pack(pady=15)


def pie_chart():
    pie_window = tk.Toplevel()
    pie_window.title("Pie Chart")
    pie_window.geometry(inner_window_dimension)

    def plot_pie_chart():
        values = values_entry.get()
        vl = values.split(',')
        value_list = [int(x) for x in vl]
        names = names_entry.get()
        nl = names.split(',')
        name_list = [x.strip() for x in nl]
        display_list = value_list
        if pie_selection.get() == "percentage":
            total = sum(value_list)
            xlist = [f"{x/total*100:.2f}%" for x in value_list]
            display_list = xlist

        # Clear the previous plot
        for widget in output_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots()
        fig.patch.set_facecolor('#abf7b1')
        ax.pie(value_list, labels=display_list)
        ax.set_title(graph_title.get(), fontsize=25, fontweight='bold')
        ax.legend(name_list, title="Labels", loc="lower left", bbox_to_anchor=(-0.38, -0.14))
        pie_canvas = FigureCanvasTkAgg(fig, master=output_frame)
        pie_canvas.draw()
        pie_canvas.get_tk_widget().pack(pady=40)

        save_as_name = ttk.Entry(output_frame)
        save_as_name.pack(pady=3)
        save_btn = ttk.Button(output_frame, text="Save as PNG", padding=10,
                              command=lambda: save_figures(fig, save_as_name), style="contents.TButton")
        save_btn.pack(pady=10)

    def save_figures(fig, save_as_name):
        if save_as_name.get() == "":
            messagebox.showerror("Error!!!", "Please enter a name")
        else:
            fig.savefig(f"{save_as_name.get()}.png")
            messagebox.showinfo("Figure Saved", f"Figure saved as {save_as_name.get()}")

    # Styling Objects
    pie_style = ttk.Style()
    pie_style.configure("p_input.TFrame", background="light green")
    pie_style.configure("p_output.TFrame", background="green")
    pie_style.configure("p_content.TLabel", background="light green", font=8)

    # Input frame and widgets
    input_frame = ttk.Frame(pie_window, style="p_input.TFrame")
    input_frame.pack(side="left", fill="both")

    title = ttk.Label(input_frame, text="Pie Chart", font=("Arial", 50), background="light green", padding=20)
    title.pack(padx=60, pady=50)

    graph_title_label = ttk.Label(input_frame, text="Enter Graph Title:", style="p_content.TLabel")
    graph_title_label.pack()

    graph_title = ttk.Entry(input_frame)
    graph_title.pack(pady=10)

    value_label = ttk.Label(input_frame, text="Enter Values:", style="p_content.TLabel")
    value_label.pack()

    values_entry = ttk.Entry(input_frame, width=40)
    values_entry.pack(pady=10)

    names_label = ttk.Label(input_frame, text="Enter Corresponding Names:", style="p_content.TLabel")
    names_label.pack()

    names_entry = ttk.Entry(input_frame, width=40)
    names_entry.pack(pady=10)

    vop_label = ttk.Label(input_frame, text="Show:", style="p_content.TLabel")
    vop_label.pack()

    pie_selection = tk.StringVar()
    pie_selection.set("value")
    opt1 = tk.Radiobutton(input_frame, text="Values", variable=pie_selection, value="value", background="light green", font=8)
    opt2 = tk.Radiobutton(input_frame, text="Percentage", variable=pie_selection, value="percentage", background="light green", font=8)
    opt1.pack()
    opt2.pack()

    # Button to trigger plot
    btn = ttk.Button(input_frame, text="Plot", command=plot_pie_chart, style="contents.TButton", padding=10)
    btn.pack(pady=50)

    # Output frame and matplotlib plot
    output_frame = ttk.Frame(pie_window, style="p_output.TFrame")
    output_frame.pack(side="right", fill="both", expand=True)


def doughnut_chart():
    doughnut_window = tk.Toplevel()
    doughnut_window.title("Doughnut Chart")
    doughnut_window.geometry(inner_window_dimension)

    def plot_doughnut_graph():
        values = values_entry.get()
        vl = values.split(',')
        value_list = [int(x) for x in vl]
        names = names_entry.get()
        nl = names.split(',')
        name_list = [x.strip() for x in nl]
        display_list = value_list
        if selection.get() == "percentage":
            total = sum(value_list)
            xlist = [f"{x/total*100:.2f}%" for x in value_list]
            display_list = xlist

        # Clear the previous plot
        for widget in output_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots()
        fig.patch.set_facecolor('#ffc9a9')
        ax.pie(value_list, labels=display_list, wedgeprops=dict(width=0.4))
        ax.set_title(graph_title.get(), fontsize=25, fontweight='bold')
        ax.legend(name_list, title="Labels", loc="lower left", bbox_to_anchor=(-0.39, -0.14))
        pie_canvas = FigureCanvasTkAgg(fig, master=output_frame)
        pie_canvas.draw()
        pie_canvas.get_tk_widget().pack(pady=40)

        save_as_name = ttk.Entry(output_frame)
        save_as_name.pack(pady=3)
        save_btn = ttk.Button(output_frame, text="Save as PNG", padding=10, command=lambda: save_figures(fig, save_as_name), style="contents.TButton")
        save_btn.pack()

    def save_figures(fig, save_as_name):
        if save_as_name.get() == "":
            messagebox.showerror("Error!!!", "Please enter a name")
        else:
            fig.savefig(f"{save_as_name.get()}.png")
            messagebox.showinfo("Figure Saved", f"Figure saved as {save_as_name.get()}")

    doughnut_style = ttk.Style()
    doughnut_style.configure("d_input.TFrame", background="#ffaf7a")
    doughnut_style.configure("d_output.TFrame", background="#ff6e00")
    doughnut_style.configure("d_content.TLabel", background="#ffaf7a", font=8)

    # Input frame and widgets
    input_frame = ttk.Frame(doughnut_window, style="d_input.TFrame")
    input_frame.pack(side="left", fill="both")

    title = ttk.Label(input_frame, text="Doughnut Chart", font=("Arial", 50), background="#ffaf7a", padding=20)
    title.pack(padx=30, pady=50)

    graph_title_label = ttk.Label(input_frame, text="Enter Graph Title:", style="d_content.TLabel")
    graph_title_label.pack()

    graph_title = ttk.Entry(input_frame)
    graph_title.pack(pady=10)

    value_label = ttk.Label(input_frame, text="Enter Values:", style="d_content.TLabel")
    value_label.pack()

    values_entry = ttk.Entry(input_frame, width=40)
    values_entry.pack(pady=10)

    names_label = ttk.Label(input_frame, text="Enter Corresponding Names:", style="d_content.TLabel")
    names_label.pack()

    names_entry = ttk.Entry(input_frame, width=40)
    names_entry.pack(pady=10)

    vop_label = ttk.Label(input_frame, text="Show:", style="d_content.TLabel")
    vop_label.pack()

    selection = tk.StringVar()
    selection.set("value")
    rad1 = tk.Radiobutton(input_frame, text="Values", variable=selection, value="value", background="#ffaf7a", font=8)
    rad2 = tk.Radiobutton(input_frame, text="Percentage", variable=selection, value="percentage", background="#ffaf7a", font=8)
    rad1.pack()
    rad2.pack()

    # Button to trigger plot
    btn = ttk.Button(input_frame, text="Plot", command=plot_doughnut_graph, style="contents.TButton", padding=10)
    btn.pack(pady=50)

    # Output frame and matplotlib plot
    output_frame = ttk.Frame(doughnut_window, style="d_output.TFrame")
    output_frame.pack(side="right", fill="both", expand=True)


root = tk.Tk()
root.title("Graph Plotter")
root.geometry("800x600+20+20")  # Set the size of the window
inner_window_dimension = "800x500+100+100"

# Create a style for the modern look
style = ttk.Style()
style.configure("graph_plotter.TLabel", font=("Helvetica", 66, "bold"))
style.configure("options.TButton", font=("Helvetica", 42), padding=(30, 25))
style.configure("contents.TButton", font=10)

# Create a frame to hold all widgets
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Add a label with "Graph Plotter" text
label = ttk.Label(main_frame, text="Graph Plotter", style="graph_plotter.TLabel")
label.pack(pady=10)  # Add some padding around the label

# Add six buttons aligned properly
buttons_frame = ttk.Frame(main_frame)
buttons_frame.pack(pady=20)  # Add some padding around the buttons frame

# Create and pack buttons
line_plot_btn = ttk.Button(buttons_frame, text="Line Plot", style="options.TButton", command=line_plot)
scatter_plot_btn = ttk.Button(buttons_frame, text="Scatter Plot", style="options.TButton", command=scatter_plot)
v_bar_chart_btn = ttk.Button(buttons_frame, text="V Bar Chart", style="options.TButton", command=v_bar_chart)
h_bar_chart_btn = ttk.Button(buttons_frame, text="H Bar Chart", style="options.TButton", command=h_bar_chart)
histogram_btn = ttk.Button(buttons_frame, text="Histogram", style="options.TButton", command=histogram_plot)
area_graph_btn = ttk.Button(buttons_frame, text="Area Plot", style="options.TButton", command=area_plot)
pie_chart_btn = ttk.Button(buttons_frame, text="Pie Chart", style="options.TButton", command=pie_chart)
doughnut_chart_btn = ttk.Button(buttons_frame, text="Doughnut", style="options.TButton", command=doughnut_chart)

line_plot_btn.grid(row=0, column=0)
area_graph_btn.grid(row=0, column=1)
v_bar_chart_btn.grid(row=1, column=0)
h_bar_chart_btn.grid(row=1, column=1)
histogram_btn.grid(row=2, column=0)
scatter_plot_btn.grid(row=2, column=1)
pie_chart_btn.grid(row=3, column=0)
doughnut_chart_btn.grid(row=3, column=1)

root.mainloop()
