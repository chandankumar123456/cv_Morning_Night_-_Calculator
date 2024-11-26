# 🌅 Morning & Night Percentage Calculator 🌃

## 🔍 Project Overview
As part of my exploration into **computer vision** and **image processing**, I developed a script to analyze RGB videos, convert them to HSV color space, and classify each frame as either "Morning" or "Night" based on brightness levels. This project provides a brightness distribution analysis, calculating the percentage of frames that fall into each category, and generates a **heatmap visualization** of brightness across frames.
## 🚀 Key Features
- **🎨 RGB to HSV Conversion**: Converts each frame from RGB to HSV color space, allowing brightness analysis via the **Value** channel.
- **☀️ Brightness Classification**: Classifies frames as "Morning" or "Night" based on a brightness threshold applied to the Value channel.
- **📊 Percentage Calculation**: Calculates and displays the percentage of frames classified as "Morning" or "Night," offering insights into the overall brightness distribution.
- **🔥 Heatmap Visualization**: Generates a heatmap of brightness levels over time, showing brightness fluctuations across the video intuitively.
## ⚙️ Getting Started

### Prerequisites
To run this project, ensure you have the following installed:
- **Python 3.x**
- **OpenCV**
- **Matplotlib**
- **NumPy**

Install libraries using:
```bash
pip install opencv-python matplotlib numpy

```markdown
### Usage
1. **Prepare Video**: Place your video file in the project directory, update the filename in the script, or pass it as an argument.
2. **Run the Script**:
   ```bash
   python script_name.py
3. **View Results**: The script displays each frame in HSV color space. After processing, you’ll see a heatmap of brightness levels and a summary of "Morning" vs. "Night" frame percentages.

```markdown
### 📸 Example Output
- **HSV Frame Conversion**: Example of a video frame converted to HSV color space.
- **Brightness Heatmap**: A heatmap representing brightness levels across frames, giving a visual summary of brightness variations throughout the video.
## 🧩 Code Structure
- **`rgb_to_hsv(video_path)`**: Converts frames to HSV and extracts the H, S, and V channels.
- **`average_and_round_hsv(H, S, V)`**: Computes the average HSV values across frames.
- **`classify_brightness(value)`**: Classifies brightness as "Morning" or "Night" based on the Value threshold.
- **`classify_time_of_day(video_path)`**: Main function to process frames, calculate brightness percentages, and generate the heatmap.
## 🤝 Contributing
I'm open to **collaborations**! Feel free to open issues, submit pull requests, or suggest features that could enhance the accuracy, efficiency, or user experience of this project.
