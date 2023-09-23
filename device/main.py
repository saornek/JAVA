import tkinter as tk
import firebase_admin
from firebase_admin import credentials, db

# Connect to database
cred = credentials.Certificate('credentials.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://java-0001-default-rtdb.firebaseio.com/'
})

# Push data to Firebase
def push_to_firebase():
    data_to_push = {
        'Bad Behaviors': [],
        'Good Behaviors': [],
        'Dog City': city_entry.get(),
        'Dog District': district_entry.get(),
        'Dog Neighborhood': neighborhood_entry.get(),
        'Dog Name': name_entry.get(),
        "Dog's tag": dogTag,
        'Food Information': "No food information has been entered yet.",
        'Water Information': "No water information has been entered yet.",
    }
    db_ref.set(data_to_push)
    status_label.config(text="Data pushed to Firebase")

# Create a GUI
window = tk.Tk()
window.title("Push Data to Firebase")

# Create input fields
name_label = tk.Label(window, text="Dog Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

city_label = tk.Label(window, text="Dog City:")
city_label.pack()
city_entry = tk.Entry(window)
city_entry.pack()

district_label = tk.Label(window, text="Dog District:")
district_label.pack()
district_entry = tk.Entry(window)
district_entry.pack()

neighborhood_label = tk.Label(window, text="Dog Neighborhood:")
neighborhood_label.pack()
neighborhood_entry = tk.Entry(window)
neighborhood_entry.pack()

dogTag = name_entry.get(), city_entry.get(), district_entry.get(), neighborhood_entry.get()
db_ref = db.reference('/Java_1/' + dogTag)

# Create a button to push data
push_button = tk.Button(window, text="Push to Firebase", command=push_to_firebase)
push_button.pack()

# Create a label to display status
status_label = tk.Label(window, text="")
status_label.pack()

window.mainloop()
