# 🚦 [ARMA FLOW]: Intelligent Bottleneck Management

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
> **Transforming unstructured urban traffic into optimized, data-driven flow.**

---

## 🚨 The Challenge: Background
In many urban environments, traffic congestion does not arise solely from high vehicle density, but from unstructured human behaviour in constrained spaces.

A wide road narrows into a bottleneck — such as a lane reduction, railway crossing, or intersection. Vehicles approaching the bottleneck often abandon lane discipline, spread across available space, and attempt to merge aggressively. When the constraint clears, conflicting movements — especially diagonal merging and late lane shifts — lead to inefficiencies, delays, and sometimes complete gridlocks.

## 🎯 Our Objective
Design a data-driven system to model, analyze, and improve traffic flow at such bottlenecks. Your solution should aim to: understand and represent traffic behaviour, identify causes of inefficiency, and propose strategies to optimize flow and reduce congestion.

---

## ✨ Why This Solution Stands Out (Key Innovations)
* **Behavioral Modeling over Simple Density:** Instead of just counting cars, our system models *human driving behavior* (e.g., aggressive merging, lane abandonment).
* **Predictive Bottleneck Analysis:** Anticipates gridlock before it happens using historical and real-time data inputs.
* **Actionable Optimization Strategies:** Generates concrete interventions (e.g., dynamic lane signalling, phased merging zones) to proactively ease constraints.

## 🧠 Methodology & Data Pipeline
1. **Data Ingestion:** How are you getting the data? (e.g., CCTV feeds, simulated traffic data, GPS datasets).
2. **Feature Extraction:** Identifying key metrics like vehicle velocity, merging angles, and lane deviation.
3. **Modeling:** Briefly explain the algorithms used RandomForest Supervised Algorithm.
## 🛠️ Tech Stack
* **Data Processing & ML:** [e.g., Pandas, Scikit-learn]
* **Frontend:** [ Streamlit]

## 🚀 Getting Started
### Prerequisites
* List any required software (e.g., Python 3.9, Streamlit)

### Installation
This is the perfect way to package up a project. Providing both Docker and non-Docker instructions ensures that absolutely anyone can run your simulation, regardless of their technical setup.

You can copy and paste these exact instructions directly into your `README.md` file on GitHub. 

### **Method 1: The Easy Way (Using Docker)**

**For Linux Users:**
```bash
# 1. Download the code
git clone https://github.com/triumphkin/ARMA-Flow.git
cd ARMA-Flow

# 2. Build the Docker image
sudo docker build -t arma-flow .

# 3. Run the container and map the port
sudo docker run -p 8501:8501 arma-flow
```

**For Windows Users (Using PowerShell or Command Prompt):**

first install docker desktop and run the docker engine.
then open the terminal
```powershell
# 1. Download the code
git clone https://github.com/triumphkin/ARMA-Flow.git
cd ARMA-Flow

# 2. Build the Docker image
docker build -t arma-flow .

# 3. Run the container and map the port
docker run -p 8501:8501 arma-flow
```
**Viewing the Dashboard:** Once the container is running, open a web browser and go to `http://localhost:8501`.

---

### **Method 2: The Manual Way (Without Docker)**
If the user does not have Docker, they will need to have **Python (3.10 to 3.12)** installed on their machine. Using a virtual environment is highly recommended so your project doesn't conflict with other Python projects on their computer.

**For Linux Users:**
```bash
# 1. Download the code
git clone https://github.com/triumphkin/ARMA-Flow.git
cd ARMA-Flow

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install the required libraries
pip install -r requirements.txt

# 4. Run the Streamlit dashboard
streamlit run app.py
```
*(If your main Python file is named `app.py`, they should run `streamlit run app.py` instead).*

**For Windows Users (Using PowerShell or Command Prompt):**
```powershell
# 1. Download the code
git clone https://github.com/triumphkin/ARMA-Flow.git
cd ARMA-Flow

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate

# 3. Install the required libraries
pip install -r requirements.txt

# 4. Run the Streamlit dashboard from app.py
streamlit run app.py
```

**Viewing the Dashboard:** Streamlit will automatically attempt to open a new tab in their default web browser. If it doesn't, they can manually navigate to `http://localhost:8501`.

### Understraing the application
## 🛑 The Bottleneck Problem & Causes of Inefficiency
We created a custom traffic simulation environment where vehicles from Lane 1 and Lane 3 merge into Lane 2 randomly, inevitably leading to high-congestion scenarios. Through this simulation, we identified five primary causes of bottleneck inefficiency:

* **Unpredictable Human Behavior:** Aggression, impatience, and erratic speeds.
* **Hard Braking:** Causing shockwaves that travel backward through traffic.
* **Static Speed Limits:** A lack of variable speed limits that adapt to real-time traffic conditions.
* **Frequent Lane Changes:** Weaving in and out of lanes unnecessarily.
* **Early Lane Changes:** Attempting to merge far before the designated merge point, wasting available lane space.

---

## ⚙️ Our Approach & Architecture
Our system is split into two primary modules to contrast unstructured traffic with a data-driven solution:

### 1️⃣ Unoptimized Simulation (`core_engine.py`)
This script simulates raw, unoptimized traffic behavior. It serves as our baseline and is used to generate highly realistic, chaotic simulation data for our model to learn from.

### 2️⃣ The Optimization Engine (`optimized_core_engine.py`)
This is the core of our predictive and corrective system. 

#### 🧠 Predictive Modeling (Random Forest)
To predict congestion before it happens, we calculate a custom metric called `system_pressure` using the following formula:
```python
system_pressure = densities[1] + densities[2] + (densities[3] * 0.4) + \
                  (speed_variance * 1.5) + weather_penalty + \
                  (footpath_count * 25) + time_penalty + behavior_penalty
```
Using this pressure metric, we generate a `seconds_to_gridlock` target variable. We then trained a **Random Forest supervised learning model** to predict this exact time-to-gridlock based on live input features from our test data, including:
* `Weather_Condition`, `Hour_Of_Day`
* `Density_Lane1`, `Density_Lane3`, `Total_Throughput`
* `Global_Speed_Variance`, `Global_Avg_Speed`
* `Aggression_Profile`, `Compliance_Profile`, `Current_Impatience`

#### 🚦 Active Optimization Strategies
When the model predicts an impending bottleneck (specifically, when `predicted_seconds < 120`), the engine automatically triggers interventions:

1. **Dynamic Variable Speed Limits:** The system actively decreases the speed limit of a specific lane as its density increases, smoothing the flow of traffic before the merge point.
2. **The Batch Zipper Method:**
   > **Definition:** The batched zipper method is a merging technique where vehicles enter the merge point in grouped batches from each lane in an alternating manner. This ensures smooth, mathematically controlled traffic flow rather than a chaotic free-for-all.

---

## 🛣️ Future Roadmap
We are actively working to implement the following features to make the system fully viable for real-world deployment:
* **🚑 Emergency Vehicle Priority:** Dynamic lane clearing and signal overrides for ambulances and fire trucks.
* **📸 Automated E-Challan System:** Automatic penalization for rule-breakers (e.g., vehicles exceeding the dynamic lane speed limit or driving on the footpath).


## 📊 Results & Impact
* **No. of Violations:** decrease driving violation on footpath (To be Fixed).
* **Reduction in collision:** Decreasing changes of hard braking. 
* **Throughput:** Increased vehicle throughput by `Y%` during peak congestion scenarios.

## 🔮 Future Scalability
* **Real-time IoT Integration:** Connecting the model to smart city infrastructure (smart traffic lights, dynamic speed limit signs).
* **Edge Computing:** Deploying lightweight inference models directly to traffic cameras for localized, low-latency decision making.
* **Computer Vision**

## ScreenShot of Project
<img width="2556" height="1597" alt="image" src="https://github.com/user-attachments/assets/b6ec17c3-847f-4d7f-b5a2-55f2570f1c72" />
<img width="2556" height="1597" alt="image" src="https://github.com/user-attachments/assets/db99b1c4-5da6-470c-b725-ff625691a21c" />

## Current Progress of Project(Video Demo)
Google Drive Link: https://drive.google.com/file/d/164K2o10tKjXAEEYlUP88xgiy1rigA6Eq/view?usp=sharing



## 👥 The Team
* **Arjun Singh**
* **Mahi Agrawal**
