import tkinter as tk
from tkinter import messagebox
import mysql.connector

# MySQL database connection
def db_connect():
    return mysql.connector.connect(
        host="localhost",        
        user="root",             
        password="Yeasrif",       
        database="cs_project_cbse" 
    )

# Main application class
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("400x500")
        
        # Start with the login screen
        self.show_login_screen()

    def show_login_screen(self):
        # Clear the window for login screen
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=20)
        
        tk.Label(self.root, text="Username:").pack()
        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack(pady=5)

        tk.Label(self.root, text="Password:").pack()
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack(pady=5)

        tk.Button(self.root, text="Login", command=self.handle_login).pack(pady=20)

    def handle_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Allow any credentials for simplicity
        if username and password:
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Please enter both username and password!")

    def show_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Library Management System", font=("Arial", 16)).pack(pady=20)
        
        tk.Button(self.root, text="Insert Book", command=self.insert_book).pack(pady=10)
        tk.Button(self.root, text="Insert Student", command=self.insert_student).pack(pady=10)
        tk.Button(self.root, text="Issue Book", command=self.issue_book).pack(pady=10)
        tk.Button(self.root, text="Return Book", command=self.return_book).pack(pady=10)
        tk.Button(self.root, text="Search Issued Books", command=self.search_issued).pack(pady=10)
        tk.Button(self.root, text="Remove Student", command=self.remove_student).pack(pady=10)

    def insert_book(self):
        self.clear_window()
        
        tk.Label(self.root, text="Insert Book", font=("Arial", 16)).pack(pady=20)

        tk.Label(self.root, text="Book Name:").pack()
        book_name_entry = tk.Entry(self.root)
        book_name_entry.pack(pady=5)

        tk.Label(self.root, text="Publication Date (YYYY-MM-DD):").pack()
        pub_date_entry = tk.Entry(self.root)
        pub_date_entry.pack(pady=5)

        tk.Label(self.root, text="Author Name:").pack()
        author_entry = tk.Entry(self.root)
        author_entry.pack(pady=5)

        tk.Label(self.root, text="Publisher:").pack()
        publisher_entry = tk.Entry(self.root)
        publisher_entry.pack(pady=5)

        tk.Label(self.root, text="Price:").pack()
        price_entry = tk.Entry(self.root)
        price_entry.pack(pady=5)

        tk.Label(self.root, text="Book Type:").pack()
        book_type_entry = tk.Entry(self.root)
        book_type_entry.pack(pady=5)

        tk.Label(self.root, text="Quantity:").pack()
        quantity_entry = tk.Entry(self.root)
        quantity_entry.pack(pady=5)

        tk.Button(self.root, text="Insert", command=lambda: self.insert_book_to_db(book_name_entry.get(), pub_date_entry.get(), author_entry.get(), publisher_entry.get(), price_entry.get(), book_type_entry.get(), quantity_entry.get())).pack(pady=20)

    def insert_book_to_db(self, book_name, pub_date, author, publisher, price, book_type, quantity):
        db = db_connect()
        cursor = db.cursor()
        try:
            cursor.execute("""
                INSERT INTO books (book_name, pub_date, author_name, publisher, price, book_type, quantity)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (book_name, pub_date, author, publisher, price, book_type, quantity))
            db.commit()
            messagebox.showinfo("Success", "Book inserted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error inserting book: {err}")
        finally:
            cursor.close()
            db.close()
            self.show_main_menu()  # Go back to main menu

    def insert_student(self):
        self.clear_window()
        
        tk.Label(self.root, text="Insert Student", font=("Arial", 16)).pack(pady=20)

        tk.Label(self.root, text="Student Name:").pack()
        student_name_entry = tk.Entry(self.root)
        student_name_entry.pack(pady=5)

        tk.Label(self.root, text="Class:").pack()
        class_entry = tk.Entry(self.root)
        class_entry.pack(pady=5)

        tk.Label(self.root, text="Roll No:").pack()
        roll_no_entry = tk.Entry(self.root)
        roll_no_entry.pack(pady=5)

        tk.Button(self.root, text="Insert", command=lambda: self.insert_student_to_db(student_name_entry.get(), class_entry.get(), roll_no_entry.get())).pack(pady=20)

    def insert_student_to_db(self, student_name, class_name, roll_no):
        db = db_connect()
        cursor = db.cursor()
        try:
            cursor.execute("""
                INSERT INTO students (student_name, class, roll_no)
                VALUES (%s, %s, %s)
            """, (student_name, class_name, roll_no))
            db.commit()
            messagebox.showinfo("Success", "Student inserted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error inserting student: {err}")
        finally:
            cursor.close()
            db.close()
            self.show_main_menu()  # Go back to main menu

    def issue_book(self):
        self.clear_window()
        
        tk.Label(self.root, text="Issue Book", font=("Arial", 16)).pack(pady=20)

        tk.Label(self.root, text="Book ID:").pack()
        book_id_entry = tk.Entry(self.root)
        book_id_entry.pack(pady=5)

        tk.Label(self.root, text="Student ID:").pack()
        student_id_entry = tk.Entry(self.root)
        student_id_entry.pack(pady=5)

        tk.Button(self.root, text="Issue", command=lambda: self.issue_book_to_db(book_id_entry.get(), student_id_entry.get())).pack(pady=20)

    def issue_book_to_db(self, book_id, student_id):
        db = db_connect()
        cursor = db.cursor()
        try:
            cursor.execute("""
                INSERT INTO issued_books (book_id, student_id, issue_date)
                VALUES (%s, %s, CURDATE())
            """, (book_id, student_id))
            db.commit()
            messagebox.showinfo("Success", "Book issued successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error issuing book: {err}")
        finally:
            cursor.close()
            db.close()
            self.show_main_menu()  # Go back to main menu

    def return_book(self):
        self.clear_window()
        
        tk.Label(self.root, text="Return Book", font=("Arial", 16)).pack(pady=20)

        tk.Label(self.root, text="Issue ID:").pack()
        issue_id_entry = tk.Entry(self.root)
        issue_id_entry.pack(pady=5)

        tk.Button(self.root, text="Return", command=lambda: self.return_book_to_db(issue_id_entry.get())).pack(pady=20)

    def return_book_to_db(self, issue_id):
        db = db_connect()
        cursor = db.cursor()
        try:
            cursor.execute("""
                UPDATE issued_books
                SET return_date = CURDATE()
                WHERE issue_id = %s
            """, (issue_id,))
            db.commit()
            messagebox.showinfo("Success", "Book returned successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error returning book: {err}")
        finally:
            cursor.close()
            db.close()
            self.show_main_menu()  # Go back to main menu

    def search_issued(self):
        self.clear_window()

        tk.Label(self.root, text="Search Issued Books", font=("Arial", 16)).pack(pady=20)

        tk.Label(self.root, text="Student ID:").pack()
        student_id_entry = tk.Entry(self.root)
        student_id_entry.pack(pady=5)

        tk.Button(self.root, text="Search", command=lambda: self.fetch_issued_books(student_id_entry.get())).pack(pady=20)

    def fetch_issued_books(self, student_id):
        db = db_connect()
        cursor = db.cursor()
        try:
            cursor.execute("""
                SELECT b.book_name, ib.issue_date, ib.return_date
                FROM issued_books ib
                JOIN books b ON ib.book_id = b.book_id
                WHERE ib.student_id = %s
            """, (student_id,))
            results = cursor.fetchall()
            if results:
                messagebox.showinfo("Issued Books", "\n".join([f"Book: {row[0]}, Issued on: {row[1]}, Returned on: {row[2] or 'Not Returned'}" for row in results]))
            else:
                messagebox.showinfo("Issued Books", "No books issued to this student.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error fetching issued books: {err}")
        finally:
            cursor.close()
            db.close()
            self.show_main_menu()  # Go back to main menu

    def remove_student(self):
        self.clear_window()
        
        tk.Label(self.root, text="Remove Student", font=("Arial", 16)).pack(pady=20)

        tk.Label(self.root, text="Student ID:").pack()
        student_id_entry = tk.Entry(self.root)
        student_id_entry.pack(pady=5)

        tk.Button(self.root, text="Remove", command=lambda: self.remove_student_from_db(student_id_entry.get())).pack(pady=20)

    def remove_student_from_db(self, student_id):
        db = db_connect()
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
            db.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "Student removed successfully!")
            else:
                messagebox.showinfo("Error", "Student ID not found.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error removing student: {err}")
        finally:
            cursor.close()
            db.close()
            self.show_main_menu()  # Go back to main menu

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
