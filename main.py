import PySimpleGUI as sg


def main():
    """
    The `main` function is the entry point of the program. It calls the `pop_up` function to display a GUI window with radio buttons for selecting a type of conversion. Based on the selected radio button, it calls the corresponding conversion function (`weight_conversion`, `length_conversion`, or `temperature_conversion`).

    Example Usage:
    main()

    Inputs:
    There are no inputs for the `main` function.

    Flow:
    1. The `main` function calls the `pop_up` function to display a GUI window with radio buttons for selecting a type of conversion.
    2. The `pop_up` function returns a dictionary of values representing the selected radio buttons.
    3. The `main` function checks the values in the dictionary to determine which conversion function to call.
    4. If the value for the 'weight' key is `True`, the `main` function calls the `weight_conversion` function.
    5. If the value for the 'length' key is `True`, the `main` function calls the `length_conversion` function.
    6. If the value for the 'temperature' key is `True`, the `main` function calls the `temperature_conversion` function.

    Outputs:
    There are no outputs for the `main` function.
    """
    values = pop_up()
    if values[0] == True:
        weight_conversion()
    elif values[1] == True:
        lenght_conversion()
    elif values[2] == True:
        temperature_conversion()
    

def pop_up():
    """
    Displays a GUI window with radio buttons for selecting a type of conversion and buttons for confirming or canceling the selection.

    Returns:
        dict: A dictionary of values representing the selected radio buttons. The keys are the names of the radio buttons ('weight', 'length', 'temperature'), and the values are `True` if the radio button is selected and `False` otherwise.
    """
    layout = [
        [sg.Text('Which conversion would you like to use?')],
        [sg.Radio('Weight', 'weight'),
         sg.Radio('Lenght', 'lenght'),
         sg.Radio('Temperature', 'temperature')],
         [sg.Button('Ok'), sg.Button('Cancel')]
    ]
    window = sg.Window('Converter', layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        print (values)
        window.close()
        return values

def weight_conversion():
    """
    Creates a GUI window for weight conversion.

    This function creates a GUI window using PySimpleGUI library that allows the user to convert weights between different units. The function handles the conversion logic based on the selected conversion method.
    """

    weight_conversions_list = ['Ounces to grams', 'Grams to Ounces', 
                               'Lbs to Kg', 'Kg to Lbs']

    layout = [
        [sg.Text('Weight Converser')],
        [sg.Input(key='-FROM-', size=19), sg.Text(key='-TO-')],
        [sg.DropDown(weight_conversions_list, key='method')],
        [sg.Button('Calculate'), sg.Button('Cancel')]
    ]

    window = sg.Window('Converser', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Calculate' and values['method'] == 'Ounces to grams':
            to_value = int(values['-FROM-']) * 31.103
            window['-TO-'].update(round(to_value, 2))
        elif event == 'Calculate' and values['method'] == 'Grams to ounces':
            to_value = int(values['-FROM-']) * 0.03527
            window['-TO-'].update(round(to_value, 2))
        elif event == 'Calculate' and values['method'] == 'Lbs to Kg':
            to_value = int(values['-FROM-']) * 0.4536
            window['-TO-'].update(round(to_value, 2))
        elif event == 'Calculate' and values['method'] == 'Kg to Lbs':
            to_value = int(values['-FROM-']) * 2.2046
            window['-TO-'].update(round(to_value, 2))
    window.close()

    
def temperature_conversion():
    """
    Converts temperatures between different units using a GUI window.

    Inputs:
    - event: a string representing the event that triggered the GUI window (e.g., button click)
    - values: a dictionary containing the current values of the GUI elements (e.g., input field, dropdown menu)
    """

    temperature_conversions_list = ['Fahrenheit to Celcius', 'Celcius to Fahrenheit',
                                    'Kelvin to Celcius', 'Celcius to Kelvin',
                                    'Kelvin to Fahrenheit', 'Fahrenheit to Kelvin']

    layout = [
        [sg.Text('Temperature Converser')],
        [sg.Input(key='-FROM-', size=19), sg.Text(key='-TO-')],
        [sg.DropDown(temperature_conversions_list, key='method')],
        [sg.Button('Calculate'), sg.Button('Cancel')]
    ]

    window = sg.Window('Converser', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Calculate' and values['method'] == 'Fahrenheit to Celcius':
            to_value = int((values['-FROM-']) - 32 ) * 0.55
            window['-TO-'].update(round(to_value, 2))
        elif event == 'Calculate' and values['method'] == 'Celcius to Fahrenheit':
            to_value = int((values['-FROM-']) * 1.8) + 32
            window['-TO-'].update(round(to_value, 2))
        elif event == 'Calculate' and values['method'] == 'Kelvin to Celcius':
            to_value = int(values['-FROM-']) - 273.15
            window['-TO-'].update(round(to_value, 2))
        elif event == 'Calculate' and values['method'] == 'Celcius to Kelvin':
            to_value = int(values['-FROM-']) + 273.15
            window['-TO-'].update(round(to_value, 2))
        elif event == 'Calculate' and values['method'] == 'Kelvin to Fahrenheit':
            to_value = int(((values['-FROM-']) - 273.15) * 1.8) + 32 
            window['-TO-'].update(round(to_value, 2))
        elif event == 'Calculate' and values['method'] == 'Fahrenheit to Kelvin':
            to_value = int(((values['-FROM-']) - 32) * 0.55) + 273.15
            window['-TO-'].update(round(to_value, 2))
    window.close()
       

def lenght_conversion():
    """
    Converts length values between different units using a GUI window.

    Inputs:
    - values: A list containing the boolean values from the pop-up window. It is used to determine which conversion method to perform.
    - event: A string representing the event that occurred in the GUI window. It is used to handle different button clicks and window closure events.

    Outputs:
    The function does not return any value. The converted value is displayed in the GUI window.
    """

    lenght_conversions_list = ['Km to Mi', 'Mi to Km',
                                'Inch to Cm', 'Cm to Inch',
                                'Feet to Meter', 'Meter to Feet']

    layout = [
        [sg.Text('lenght Converser')],
        [sg.Input(key='-FROM-', size=19), sg.Text(key='-TO-')],
        [sg.DropDown(lenght_conversions_list, key='method')],
        [sg.Button('Calculate'), sg.Button('Cancel')]
    ]

    window = sg.Window('Converser', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Calculate' and values['method'] == 'Km to Mi':
            to_value = int(values['-FROM-']) * 0.6214
            window['-TO-'].update(round(to_value, 2))
        elif event == 'Calculate' and values['method'] == 'Mi to Km':
            to_value = int(values['-FROM-']) * 1.609
            window['-TO-'].update(round(to_value, 2))
        elif event == 'Calculate' and values['method'] == 'Inch to Cm':
            to_value = int(values['-FROM-']) * 2.54
            window['-TO-'].update(round(to_value, 2))
        elif event == 'Calculate' and values['method'] == 'Cm to Inch':
            to_value = int(values['-FROM-']) + 0.3937
            window['-TO-'].update(round(to_value, 2))
        elif event == 'Calculate' and values['method'] == 'Feet to Meter':
            to_value = int(values['-FROM-']) * 0.3048
            window['-TO-'].update(round(to_value, 2))
        elif event == 'Calculate' and values['method'] == 'Meter to Feet':
            to_value = int(values['-FROM-']) * 3.281
            window['-TO-'].update(round(to_value, 2))
    window.close()


if __name__ == "__main__":
    main()