from setuptools import setup

setup(
    name="OctoPrint-USBControl",
    version="0.1.0",
    description="Control 3D printer using USB keyboard inputs",
    author="Midori",
    author_email="faransansj@gmail.com",
    url="https://github.com/faransansj/3D_printer_HID_system/tree/main/plugin",
    packages=["octoprint_usbcontrol"],
    install_requires=["pyusb", "requests"],
    entry_points={
        "octoprint.plugin": [
            "usbcontrol = octoprint_usbcontrol"
        ]
    }
)
