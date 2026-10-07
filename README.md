This program simulates holding the right mouse button (RMB) for more ergonomic control in games which do not already support a "mouse look lock" toggle.

- Press or hold <kb>caps lock</kb> to simulate the RMB temporarily
- Press <kb>alt + shift</kb> to toggle the RMB
- This assumes you have configured your <kb>caps lock</kb> key to act as a modifier like <kb>ctrl</kb>
- The assigned keys are easily changed at the top of `src/main.py`

## Requirements
- python > 3.10
- python-pynput >= 1.8.0

## Usage
```
$ python mouselock.py
Press <alt>+<shift>: toggle rmb
Hold <caps_lock>: press or release rmb
```
<kb>ctrl + c</kb> to quit
