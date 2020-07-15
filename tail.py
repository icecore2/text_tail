import subprocess
import time
import os

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer


dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

def powershell_script():
    p = subprocess.Popen(["powershell.exe",
                          fr"{dir_path}\tail.ps1"])

if __name__ == "__main__":
    patterns = "*.txt"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    powershell_script()

def on_created(event):
    print(f"New file {event.src_path} has been created!")
    powershell_script()

my_event_handler.on_created = on_created


path = "C:\Text_files"  # Change this path to where you need.
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=True)


my_observer.start()
try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
