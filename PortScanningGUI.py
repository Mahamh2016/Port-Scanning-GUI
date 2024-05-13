import tkinter as tk
from socket import *

def connect_scan(tgtHost, tgtPort):
    try:
        conn = socket(AF_INET, SOCK_STREAM)
        conn.settimeout(1)
        conn.connect((tgtHost, tgtPort))
        conn.close()
        return f"[+] {tgtPort}/tcp open"
    except:
        return f"[-] {tgtPort}/tcp closed"

def port_scan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        return "[-] Can't resolve host"
    
    results = []
    for tgtPort in tgtPorts:
        results.append(connect_scan(tgtHost, tgtPort))
    return results

def start_scan():
    host = entry.get()
    ports = (21,22,23,25,49,53,80,110,443,465,3389)  # You can customize the ports to scan
    results = port_scan(host, ports)
    result_text.set('\n'.join(results))

app = tk.Tk()
app.title("Port Scanner")

canvas = tk.Canvas(app, width=700, height=800)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(app, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(app, bg="#80c1ff", bd=6)
frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor='n')

entry = tk.Entry(frame, font='40')
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Search for Port", font='40', command=start_scan)
button.place(relx=0.7, relheight=1, relwidth=0.3)

result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text)
result_label.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

app.mainloop()
