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
3. **Modeling:** Briefly explain the algorithms used (e.g., Reinforcement Learning for traffic light optimization, clustering for behavioral patterns, or computer vision for real-time tracking).
4. **Optimization:** How the model outputs recommendations to improve the flow.

## 🛠️ Tech Stack
* **Data Processing & ML:** [e.g., Pandas, Scikit-learn, TensorFlow/PyTorch]
* **Frontend:** [e.g., React, Streamlit]

## 🚀 Getting Started
### Prerequisites
* List any required software (e.g., Python 3.9, Node.js)

### Installation
1. Clone the repository: `git clone https://github.com/triumphkin/ClearWayAI.git`
2. Install dependencies: `pip install -r requirements.txt`
3. 

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

### Running the Application
1. [Add your step to run the server/app...]
2. [Add your step to access the UI...]

## 📊 Results & Impact
* **Efficiency Gain:** Demonstrated a projected `X%` decrease in bottleneck wait times in simulations.
* **Throughput:** Increased vehicle throughput by `Y%` during peak congestion scenarios.

## 🔮 Future Scalability
* **Real-time IoT Integration:** Connecting the model to smart city infrastructure (smart traffic lights, dynamic speed limit signs).
* **Edge Computing:** Deploying lightweight inference models directly to traffic cameras for localized, low-latency decision making.

## ScreenShot of Project
<img width="2556" height="1597" alt="image" src="https://github.com/user-attachments/assets/b370088d-7ddf-4de6-8e60-1c7ba48b05fc" />
<img width="2556" height="1597" alt="image" src="https://github.com/user-attachments/assets/35c35ef1-4bf2-4f51-891c-577d3f4f535c" />



## 👥 The Team
* **Arjun Singh**
* **Mahi Agrawal**
