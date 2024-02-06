import json

class OctoPrintUSBControlPlugin:
    def __init__(self, usb_handler, octoprint_api, config_file):
        self.usb_handler = usb_handler
        self.octoprint_api = octoprint_api
        self.config_file = config_file
        self.key_gcode_mapping = self.load_mapping()

    def load_mapping(self):
        # Load the key-G-code mapping from the configuration file
        try:
            with open(self.config_file, 'r') as file:
                mapping = json.load(file)
            return mapping
        except Exception as e:
            print(f"Error loading configuration file: {e}")
            return {}

    def run(self):
        while True:
            key = self.usb_handler.read_key()
            if key:
                # Convert the key input to a G-code command
                gcode = self.key_gcode_mapping.get(key)
                if gcode:
                    # Send the G-code command to the 3D printer
                    self.octoprint_api.send_gcode(gcode)

# Example usage
# usb_handler = USBKeyboardHandler()
# octoprint_api = OctoPrintAPIHandler(api_key="YOUR_API_KEY")
# plugin = OctoPrintUSBControlPlugin(usb_handler, octoprint_api, "config.json")
# plugin.run()

# Note: The configuration file should be in the same directory as the script or provide the full path to the file.
# The user can modify the configuration file to change the key-G-code mapping as needed.

