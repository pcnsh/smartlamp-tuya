# Smart Zinnia Control / Tuya Device - README

## 📌 Prerequisites
Before using, configure your Tuya credentials in the code:
```python
ACCESS_ID = "your_access_id"  # Replace with your Client ID
ACCESS_KEY = "your_access_key"  # Replace with your Client Secret
API_ENDPOINT = "https://openapi.tuyaus.com"  # Change region if needed
DEVICE_ID = "your_device_id"  # Device ID from Tuya
```
Here's how to obtain each required credential for the Tuya API:

---

### **1. Obtaining ACCESS_ID (Client ID) and ACCESS_KEY (Client Secret)**
**Step-by-Step Guide:**

1. **Log in** to the [Tuya IoT Platform](https://iot.tuya.com/)
2. Go to **Cloud** → **Development** → **Create Project**
   - Project Name: Your project name
   - Industry: Select "Smart Home"
   - Development Method: Select "Custom Development"
   - Data Center: Select your region (important for API_ENDPOINT)
3. After creation, go to **Project** → **Overview**
4. Under **Authorization Key**, you'll find:
   - `Access ID/Client ID` → Your `ACCESS_ID`
   - `Access Secret/Client Secret` → Your `ACCESS_KEY`

**Note:** These credentials are created per project, not per device.

---

### **2. Determining API_ENDPOINT**
The endpoint depends on your server location:

| Region | API Endpoint |
|--------|--------------|
| China | `https://openapi.tuyacn.com` |
| Western America | `https://openapi.tuyaus.com` |
| Eastern America | `https://openapi-ueaz.tuyaus.com` |
| Europe | `https://openapi.tuyaeu.com` |
| India | `https://openapi.tuyain.com` |

**Tip:** This should match the region you selected during project creation.

---

### **3. Finding DEVICE_ID**
**Method 1: Using Tuya IoT Platform**
1. Go to **Devices** → **Device Management**
2. Find your device and copy the **Device ID**

**Method 2: Using Tuya Smart App**
1. Open the device in the app
2. Go to **Device Settings** → **Device Information**
3. Find the **Device ID** (sometimes labeled "Virtual ID")

**Method 3: Using TinyTuya (Local Network)**
Run in terminal:
```bash
python -m tinytuya scan
```
Look for your device's `id` in the output.

---

### **4. Additional Setup**
After obtaining credentials:
1. **Link your device** to the project:
   - Go to **Devices** → **Link Device by App Account**
   - Scan the QR code from your Tuya Smart app

2. **Enable API Services**:
   - Go to **Cloud** → **Permissions**
   - Enable:
     - Device Management
     - Device Control
     - Device Status Notification

---

### **Troubleshooting**
If you get authorization errors:
1. Verify you've **linked devices** to the project
2. Check your **project's data center** matches API_ENDPOINT
3. Ensure **API permissions** are enabled
4. For new projects, wait ~15 minutes after creation for credentials to activate

**Security Note:** Never commit these credentials to public repositories. Use environment variables for production:
```python
import os
ACCESS_ID = os.getenv('TUYA_ACCESS_ID')
ACCESS_KEY = os.getenv('TUYA_ACCESS_KEY')
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
