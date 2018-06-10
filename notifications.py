def notify(title='', subtitle='', message='', sound=None):
    """
    Function used to send notification.

    Valid sound names are names of sounds found in -
    ~/Library/Sounds
    /System/Library/Sounds

    Variable ordering is as follows -

    :param title: Notification Title. Default: Empty
    :param subtitle:  Notification Subtitle. Default: Empty
    :param message:  Notification Message. Default: Empty
    :return: None
    """
    from subprocess import Popen, PIPE

    if not sound:
        script = f'display notification "{message}" with title "{title}" subtitle "{subtitle}"'
    else:
        script = f'display notification "{message}" with title "{title}" subtitle "{subtitle}" sound name "{sound}"'

    p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(script)
