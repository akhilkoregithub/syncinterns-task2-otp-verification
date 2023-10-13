import tkinter as tk
import random
import smtplib
from tkinter import messagebox
import threading

# generate a random 6-digit OTP
def generate_otp():
    otp = random.randint(100000, 999999)
    return str(otp)

#  send OTP via email
def send_otp_email_thread(email, otp):
    try:
        smtp_server = 'smtp.gmail.com'  
        smtp_port = 587 
        sender_email = 'koreakhil47@gmail.com'  
        sender_password = 'ltgh dskg iipk wauc' 

        message = f"Your OTP is: {otp}"
        subject = "OTP Verification"

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Compose and send the email
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, email, email_message)

        # Close the connection
        server.quit()
        messagebox.showinfo("OTP Sent", "OTP sent successfully to your email!")

        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


# send OTP via email
def send_otp_email(email, otp):
    email_thread = threading.Thread(target=send_otp_email_thread, args=(email, otp))
    email_thread.start()


# verify OTP
def verify_otp():
    user_otp = otp_entry.get()
    if user_otp == current_otp:
        messagebox.showinfo("OTP Verification", "OTP is valid. You are verified!")
    else:
        messagebox.showerror("OTP Verification", "Invalid OTP. Please try again.")
        
# Function to resend OTP
def resend_otp():
    global current_otp
    current_otp = generate_otp()
    email = email_entry.get()
    if send_otp_email(email, current_otp):
        messagebox.showinfo("Resend OTP", "New OTP sent successfully!")
    else:
        messagebox.showerror("Resend OTP", "Failed to resend OTP. Please try again.")

#  main window
root = tk.Tk()
root.title("OTP Verification")

# Create and configure widgets
title_label = tk.Label(root, text="OTP Verification", font=("Arial", 16))  # Title label
label = tk.Label(root, text="Enter OTP:", font=("Arial", 10))
otp_entry = tk.Entry(root, width=30)  # Increased width
verify_button = tk.Button(root, text="Verify OTP", command=verify_otp, width=10, bg="lightgreen")  # Added background color
email_label = tk.Label(root, text="Enter your email:", font=("Arial", 10))
email_entry = tk.Entry(root, width=30)  # Increased width
send_email_button = tk.Button(root, text="Send OTP", command=lambda: send_otp_email(email_entry.get(), current_otp), width=10, bg="lightblue")  # Added background color
resend_button = tk.Button(root, text="Resend OTP", command=resend_otp, width=10, bg="lightcoral")

# widgets using grid layout
title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=5)  # Title label
email_label.grid(row=1, column=0, padx=10, pady=15)
email_entry.grid(row=1, column=1, padx=10, pady=15)
send_email_button.grid(row=1, column=2, padx=10, pady=5)
label.grid(row=2, column=0, padx=10, pady=5)
otp_entry.grid(row=2, column=1, padx=10, pady=5)
verify_button.grid(row=2, column=2, padx=10, pady=5)
resend_button.grid(row=3, column=1, padx=10, pady=5)

# Generate a random OTP when the program starts
current_otp = generate_otp()

#  Tkinter main loop
root.mainloop()
