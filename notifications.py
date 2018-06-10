def notify(title='', subtitle='', message=''):
    """
    Function used to send notification.
    Variable ordering is as follows -

    :param title: Notification Title. Default: Empty
    :param subtitle:  Notification Subtitle. Default: Empty
    :param message:  Notification Message. Default: Empty
    :return: None
    """
    from subprocess import Popen, PIPE

    script = f'display notification "{message}" with title "{title}" subtitle "{subtitle}"'
    print(script)
    p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(script)
