from rich.traceback import install


def notification_callback1():
    from windows_toasts import Toast, WindowsToaster

    toaster = WindowsToaster("Python")
    newToast = Toast()
    newToast.text_fields = ["Hello, world!"]
    newToast.on_activated = lambda _: print("Toast clicked!")
    toaster.show_toast(newToast)


def notification_callback2():
    """Best one so far"""
    from notifypy import Notify

    notification = Notify()
    notification.application_name = "Test"
    notification.title = "Cool Title"
    notification.message = "Even cooler message."
    notification.urgency = "critical"
    notification.send()


def notification_callback3():
    from plyer import notification

    notification.notify(
        title="Here is the title",
        message="Here is the message",
        app_name="Here is the application name",
    )


def main():
    notification_callback1()
    notification_callback2()
    notification_callback3()


if __name__ == "__main__":
    # Enable rich error formatting in debug mode
    install(show_locals=True)
    main()
