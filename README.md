# Project Title: IoT Emergency Exit Light Simulator

## Objective
This project simulates an **emergency exit light system**.  
It lights up a path using LEDs (simulated with GUI labels) sequentially during an emergency.

> **Example:** Provides a safe exit path in buildings by guiding occupants with lights.

---

## Tools & Technologies
- **Programming Language**: Python 3.x  
- **Framework**: Tkinter  
- **Simulator**: Custom GUI  
- **Dependencies**: Listed in `requirements.txt`  

---

## Setup Instructions

### 1. Clone the Repository
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

Logic: When emergency is triggered, LEDs light sequentially and flash to indicate alert

--

Screenshots
Initial Interface
<img width="677" height="740" alt="Screenshot from 2025-09-18 05-19-58" src="https://github.com/user-attachments/assets/14970ba6-2742-4c0f-8055-153a6365c093" />

LEDs Lighting Sequentially
<img width="677" height="740" alt="Screenshot from 2025-09-18 05-21-04" src="https://github.com/user-attachments/assets/cce1baf6-a985-45a8-a238-95df252868b5" />

Flashing Alert Effect
<img width="677" height="740" alt="Screenshot from 2025-09-18 05-22-19" src="https://github.com/user-attachments/assets/48b01490-7bb9-4ed1-878b-c1e9ead88cda" />

---

Observations
GUI correctly simulates emergency exit path

Sequential and flashing LED effects visually demonstrate emergency scenario

Works well without actual hardware

---

Future Improvements
Export emergency log with timestamp

Add multiple paths or more LEDs

Integrate real hardware with Raspberry Pi or Arduino

