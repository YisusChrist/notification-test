This Python script demonstrates three different methods for displaying notifications on a Windows system. Each notification method utilizes a different third-party library to showcase various options for creating and customizing notifications.

# Prerequisites

- This script is designed to run on a Windows system.
- Make sure you have Python installed on your machine.

# Installation

Install the required third-party libraries using the following commands:

```sh
pip install rich windows-toasts notify-py plyer
```

# Usage

Run the script by executing the following command:

```sh
python notification_script.py
```

The script will display three different notifications using different libraries, showcasing their unique features and customization options.

# Notification Methods

## Method 1: Windows Toasts

- Uses the `windows-toasts` library.
- Displays a simple "Hello, world!" toast notification.
- Clicking on the toast will print "Toast clicked!".

## Method 2: Notifypy

- Uses the `notifypy` library.
- Shows a notification with a custom title, message, and urgency level.
- Designed to be a critical notification.

## Method 3: Plyer

- Uses the `plyer` library.
- Sends a notification with a specified title, message, and application name.

# Additional Notes

- The script can be extended or modified to use a specific notification method based on the requirements of your application.
- Rich error formatting is enabled in debug mode to provide detailed information in case of any issues.

Feel free to explore and customize the script based on your needs.
