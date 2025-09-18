# Project Title: IoT Emergency Exit Light Simulator

## Objective
This project simulates an emergency exit light system.  
It lights up a path using LEDs (simulated with GUI labels) sequentially during an emergency.

> Example: Provides a safe exit path in buildings by guiding occupants with lights.

---

## Tools & Technologies
- **Programming Language**: Python 3.x
- **Frameworks**: Tkinter
- **Simulator**: Custom GUI
- **Dependencies**: Listed in `requirements.txt`

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/marthanjoel/IoT-Emergency-Exit-Light.git
cd IoT-Emergency-Exit-Light
2. Create Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Run the Project
bash
Copy code
python3 exit_light.py
Simulation Details
Sensors Emulated: Emergency detection (button click)

Actuators Emulated: LEDs represented as GUI labels

Logic: When emergency triggered, LEDs light sequentially and flash to indicate alert




Screenshots
Initial GUI with LEDs off

LEDs lighting sequentially (green)

Flashing alert effect (red/green)

Observations
GUI correctly simulates emergency exit path

Sequential and flashing LED effects visually demonstrate emergency scenario

Works well without actual hardware


---
Future Improvements
Export emergency log with timestamp

Add multiple paths or more LEDs

Integrate real hardware with Raspberry Pi or Arduino

