import csv
import tkinter as tk
from tkinter import messagebox
from sklearn.tree import DecisionTreeClassifier

place_data = []
with open('Bali Popular Destination for Tourist 2022 - Sheet1.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        place_data.append(row)

def clean_cost_value(cost_text):
    cost_text = cost_text.replace(',', '')
    if 'USD' in cost_text:
        cost = cost_text.split()[0]
        if cost.isdigit():
            return float(cost)
        else:
            return 0.0
    else:
        return 0.0

def create_decision_tree():
    X_train = []
    y_train = []

    for data in place_data:
        rating = float(data[3])
        reviews = float(data[4])
        cost_text = data[7]

        cost = clean_cost_value(cost_text)

        X_train.append([rating, reviews, cost])
        y_train.append(data[0])

    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    return clf

def select_place():
    rating_pref = rating_input.get()
    reviews_pref = reviews_input.get()
    cost_pref = cost_input.get()

    if not rating_pref or not reviews_pref or not cost_pref:
        messagebox.showwarning("Peringatan", "Mohon isi semua input.")
        return

    rating_valid = True
    reviews_valid = True
    cost_valid = True

    if rating_pref != "Semua":
        try:
            rating = float(rating_pref)
            if rating < 0 or rating > 5:
                rating_valid = False
        except ValueError:
            rating_valid = False

    if reviews_pref != "Semua":
        try:
            reviews = float(reviews_pref)
            if reviews < 0:
                reviews_valid = False
        except ValueError:
            reviews_valid = False

    if cost_pref != "Semua":
        try:
            cost = float(cost_pref)
            if cost < 0:
                cost_valid = False
        except ValueError:
            cost_valid = False

    if not rating_valid or not reviews_valid or not cost_valid:
        messagebox.showwarning("Peringatan", "Mohon masukkan nilai yang valid.")
        return

    filtered_places = []
    for data in place_data:
        rating = float(data[3])
        reviews = float(data[4])
        cost_text = data[7]

        cost = clean_cost_value(cost_text)

        if (rating_pref == "Semua" or (rating_pref != "Semua" and rating >= float(rating_pref))) \
                and (reviews_pref == "Semua" or (reviews_pref != "Semua" and reviews >= float(reviews_pref))) \
                and (cost_pref == "Semua" or (cost_pref != "Semua" and cost <= float(cost_pref))):
            filtered_places.append(data)

    if filtered_places:
        clf = create_decision_tree()

        predictions = clf.predict([[float(rating_pref), float(reviews_pref), float(cost_pref)]])

        result_text = "Tempat Wisata yang Direkomendasikan:\n\n"
        for place in filtered_places:
            result_text += f"Nama Tempat: {place[0]}\n"
            result_text += f"Lokasi: {place[1]}\n"
            result_text += f"Koordinat: {place[2]}\n"
            result_text += f"Rating Google Maps: {str(place[3])}\n"
            result_text += f"Jumlah Ulasan Google: {str(place[4])}\n"
            result_text += f"Sumber: {place[5]}\n"
            result_text += f"Deskripsi: {place[6]}\n"
            result_text += f"Biaya Kunjungan (USD): {place[7]}\n"
            result_text += "--------------------------------------\n\n"

        result_textbox.configure(state='normal')
        result_textbox.delete('1.0', tk.END)
        result_textbox.insert(tk.END, result_text)
        result_textbox.configure(state='disabled')
    else:
        result_textbox.configure(state='normal')
        result_textbox.delete('1.0', tk.END)
        result_textbox.insert(tk.END, "Tidak ada tempat wisata yang memenuhi preferensi.")
        result_textbox.configure(state='disabled')

root = tk.Tk()
root.title("Rekomendasi Tempat Wisata Di Bali")
root.geometry("550x420")

rating_label = tk.Label(root, text="Rating Google Maps:")
rating_label.place(x=50, y=50)

rating_input = tk.Entry(root)
rating_input.place(x=200, y=50)

reviews_label = tk.Label(root, text="Jumlah Ulasan Google:")
reviews_label.place(x=50, y=100)

reviews_input = tk.Entry(root)
reviews_input.place(x=200, y=100)

cost_label = tk.Label(root, text="Biaya Kunjungan (USD):")
cost_label.place(x=50, y=150)

cost_input = tk.Entry(root)
cost_input.place(x=200, y=150)

select_button = tk.Button(root, text="Pilih", command=select_place)
select_button.place(x=200, y=200)

result_textbox = tk.Text(root, height=8, width=56, state='disabled')
result_textbox.place(x=50, y=250)

root.mainloop()
