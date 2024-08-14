import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.ui_setup import setup_main_window

def on_exit():
    root.destroy()

if __name__ == "__main__":
    root, entry_uniprot_id = setup_main_window(on_exit)
    root.mainloop()

