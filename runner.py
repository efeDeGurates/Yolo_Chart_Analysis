import gc
import threading
import time
import mss
import numpy as np
import cv2
from ultralytics import YOLO
import tkinter as tk
from tkinter import messagebox
import queue

model = YOLO("runs/detect/train/weights/best.pt")
results_queue = queue.Queue(maxsize=1)

def screenshot():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        img = np.array(sct_img)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return img

def detection_worker():
    while True:
        img = screenshot()
        result = model(img)
        if results_queue.full():
            try:
                results_queue.get_nowait()
            except queue.Empty:
                pass
        results_queue.put(result)
        del img       #delete screenshot to free memory
        del result
        gc.collect()
        time.sleep(5)

def notification_worker(root):
    last_notification = None
    while True:
        try:
            result = results_queue.get(timeout=1)
            detected_texts = []
            for r in result:
                for box in r.boxes:
                    cls_id = int(box.cls)
                    confidence = float(box.conf)
                    label = r.names[cls_id]
                    detected_texts.append(f"{label} ({confidence:.2f})")
            # buy/sell notifications
            for text in detected_texts:
                label = text.split(" (")[0]  # only label
                if label != last_notification:
                    if label.startswith("Bearish"):
                        root.after(0, lambda msg=text: messagebox.showinfo("Suggestion", "Sell/Short: " + "\n" + msg))
                        last_notification = label
                    elif label.startswith("Bullish"):
                        root.after(0, lambda msg=text: messagebox.showinfo("Suggestion", "Buy/Long: " + "\n" + msg))
                        last_notification = label
        except queue.Empty:
            pass
        time.sleep(1)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    threading.Thread(target=detection_worker, daemon=True).start()
    threading.Thread(target=notification_worker, args=(root,), daemon=True).start()

    root.mainloop()
