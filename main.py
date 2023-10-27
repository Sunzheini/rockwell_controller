from time import sleep

from pywinauto.application import Application
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard
import pyautogui


# global variables
exe_path = r"C:\Program Files (x86)\Rockwell Software\Studio 5000\Logix Designer\ENU\v32\Bin\LogixDesigner.exe"
project_path = r"C:\Appl\Projects\Rockwell\OPC_UA_Server.ACD"
coordinates_of_communications_tab = (354, 42)
coordinates_of_go_online = (435, 153)
coordinates_of_ok_button = (905, 558)
coordinates_of_x_button = (1898, 15)


# print the coordinates of the mouse position
def print_mouse_coordinates():
    while 1:
        x, y = pyautogui.position()
        print(x, y)
        sleep(1)


def sequence():
    app = Application(backend="uia")

    try:
        app.start(exe_path)
    except Exception as e:
        print("Error starting:", e)

    main_window = app.top_window()
    main_window.wait('visible', timeout=30)

    main_window.print_control_identifiers()     # Print the control identifiers of the main window
    # Click the "File" menu (assuming you have already defined 'main_window')
    # file_menu = main_window.child_window(title="File", control_type="MenuItem")
    # file_menu.click_input()

    sleep(1)
    main_window.set_focus()                     # puts the app window to focus (foreground)

    sleep(2)
    main_window.type_keys("^o")                 # sends ctrl+o   (open)

    sleep(2)
    keyboard.send_keys(project_path)            # enter project path

    sleep(2)
    keyboard.send_keys("{ENTER}")               # send enter

    sleep(2)
    mouse.click(button='left', coords=coordinates_of_communications_tab)    # click on communications tab

    sleep(2)
    mouse.click(button='left', coords=coordinates_of_go_online)             # click on go online

    sleep(2)
    mouse.click(button='left', coords=coordinates_of_ok_button)             # click on ok button

    # main_window is not working anymore after clicking, so need this:
    sleep(2)
    main_window = app.top_window()
    main_window.wait('visible', timeout=30)
    main_window.print_control_identifiers()     # output is different!

    # close software
    sleep(2)
    keyboard.send_keys("%{F4}")                 # send alt+F4

    # other options for closing the software:
    # keyboard.send_keys("^x")                    # send ctrl+x
    # main_window.close()                       # close main window
    # mouse.click(button='left', coords=coordinates_of_x_button)              # click on x button


sequence()
