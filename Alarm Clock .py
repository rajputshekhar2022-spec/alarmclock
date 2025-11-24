# Input fields for HH MM SS
hour_input = widgets.Text(description='Hour (0-23):', value='00', style={'description_width': 'initial'})
minute_input = widgets.Text(description='Minute (0-59):', value='00', style={'description_width': 'initial'})
second_input = widgets.Text(description='Second (0-59):', value='00', style={'description_width': 'initial'})

add_button = widgets.Button(description='Add Alarm')
add_button.on_click(add_alarm_handler)

# Dropdown to select alarm to delete
delete_selector = widgets.Dropdown(options=[], description='Select Alarm to Delete:')
delete_button = widgets.Button(description='Delete Selected Alarm')
delete_button.on_click(delete_alarm_handler)

# Arrange widgets
input_widgets = widgets.HBox([hour_input, minute_input, second_input])
add_section = widgets.VBox([input_widgets, add_button])
delete_section = widgets.VBox([delete_selector, delete_button])

display(add_section, delete_section, alarm_output)

# Initial display update
update_list()

# Start the alarm checking thread
alarm_thread = threading.Thread(target=check_alarms, daemon=True)
alarm_thread.start()

