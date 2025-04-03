# Smart Zinnia Control / Tuya Device - README

## 📌 Prerequisites
Before using, configure your Tuya credentials in the code:
```python
ACCESS_ID = "your_access_id"  # Replace with your Client ID
ACCESS_KEY = "your_access_key"  # Replace with your Client Secret
API_ENDPOINT = "https://openapi.tuyaus.com"  # Change region if needed
DEVICE_ID = "your_device_id"  # Device ID from Tuya
```

## 📋 Available Commands

### 💻 Command Line Mode
```bash
# Turn on
python control_zinnia.py on

# Turn on with specific brightness (0-100%)
python control_zinnia.py on 75

# Turn off
python control_zinnia.py off

# Set brightness (0-100%)
python control_zinnia.py 50

# Start morning routine
python control_zinnia.py routine

# Toggle state
python control_zinnia.py toggle
```

### 🖱 Interactive Mode
Run without arguments:
```bash
python control_zinnia.py
```

Menu:
```
1. Turn On
2. Turn Off
3. Maximum Brightness (100%)
4. Medium Brightness (50%)
5. Minimum Brightness (10%)
6. Custom Brightness
7. Automatic Routine
8. Toggle State
9. Exit
```

## 🔧 Features

### 💡 Basic Control
- `turn_on()`: Powers on the light
- `turn_off()`: Powers off the light
- `toggle()`: Toggles current state

### 🌈 Brightness Control
- `set_brightness(percent)`: Adjusts brightness (0-100%)
- Supports different scales (0-1000 or 0-255)

### ⏰ Morning Routine
- Gradual brightness increase (10% → 100% in 10 steps)
- Configurable interval (default: 30 seconds)

## ⚠️ Troubleshooting
1. **Connection Errors**:
   - Verify `ACCESS_ID` and `ACCESS_KEY`
   - Check correct region in `API_ENDPOINT`

2. **Unresponsive Commands**:
   ```python
   TUYA_LOGGER.setLevel(logging.DEBUG)  # Enable detailed logs
   ```

3. **Brightness Not Working**:
   - Verify `BRIGHTNESS_CODE` matches your model
   - Try alternative codes: `brightness`, `dimmer`

## 📦 Dependencies
Install with:
```bash
pip install tuya-connector-python
```

## 💡 Tips
- For automations, import `ZinniaController` class in other scripts
- Use `time.sleep()` between commands for slow devices
- Check `TUYA_LOGGER` for detailed communication logs

## 📄 License
MIT License - Free for use and modification
