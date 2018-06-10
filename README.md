# MacNotifications

A package for sending MacOS notifications from within a Python program. This is currently in Beta - if you have any suggestions, just create a new Issue!

___

## Getting Started

### Installation

The easiest way to install MacNotifications is using `pip`

`pip install macnotifications`

### Usage

The following example ought to be helpful -

```python
from macnotifications import notify

notify(title='Bananas', subtitle='Yellow', message='Great Source of Potassium')
```
