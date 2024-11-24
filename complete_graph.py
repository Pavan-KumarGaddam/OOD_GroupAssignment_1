import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace 'your_file.csv' with the actual filename)
file_path = 'openhab-addons_class.csv'  # Replace with your actual CSV file path
data = pd.read_csv(file_path)

# Filter relevant columns and drop missing values
data = data[['class', 'type', 'loc', 'wmc', 'lcom']].dropna()

# Convert metrics to numeric
data['loc'] = pd.to_numeric(data['loc'], errors='coerce')
data['wmc'] = pd.to_numeric(data['wmc'], errors='coerce')
data['lcom'] = pd.to_numeric(data['lcom'], errors='coerce')

# Categorize class sizes based on loc (No averages, each class should be its own category)
bins = [0, 200, 500, float('inf')]  # Define size categories
labels = ['Small', 'Medium', 'Large']
data['size_category'] = pd.cut(data['loc'], bins=bins, labels=labels)

# Compute Complexity per Line (WMC per LoC)
data['complexity_per_line'] = data['wmc'] / data['loc']

# Identify unmaintainable classes based on thresholds
data['high_wmc'] = data['wmc'] > 10  # WMC > 10 is considered unmaintainable
data['low_cohesion'] = data['lcom'] > 0.8  # LCOM > 0.8 is considered unmaintainable

# --- Visualizations ---

# Scatter Plot: LoC vs WMC (Per Class)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='loc', y='wmc', hue='size_category', data=data)
plt.title('Class Size (LOC) vs Complexity (WMC)')
plt.xlabel('Lines of Code (LOC)')
plt.ylabel('Weighted Methods per Class (WMC)')
plt.legend(title='Class Size')
plt.grid(True)
plt.show()

# Scatter Plot: LoC vs LCOM (Per Class)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='loc', y='lcom', hue='size_category', data=data)
plt.title('Class Size (LOC) vs Lack of Cohesion (LCOM)')
plt.xlabel('Lines of Code (LOC)')
plt.ylabel('Lack of Cohesion in Methods (LCOM)')
plt.legend(title='Class Size')
plt.grid(True)
plt.show()

# Box Plot: WMC by Class Size (Per Class)
plt.figure(figsize=(8, 6))
sns.boxplot(x='size_category', y='wmc', data=data)
plt.title('Complexity (WMC) by Class Size')
plt.xlabel('Class Size Category')
plt.ylabel('Weighted Methods per Class (WMC)')
plt.grid(True)
plt.show()

# Box Plot: LCOM by Class Size (Per Class)
plt.figure(figsize=(8, 6))
sns.boxplot(x='size_category', y='lcom', data=data)
plt.title('Lack of Cohesion (LCOM) by Class Size')
plt.xlabel('Class Size Category')
plt.ylabel('Lack of Cohesion in Methods (LCOM)')
plt.grid(True)
plt.show()

# Scatter Plot: Complexity per Line (Per Class)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='loc', y='complexity_per_line', hue='size_category', data=data)
plt.title('Complexity per Line vs Class Size')
plt.xlabel('Lines of Code (LOC)')
plt.ylabel('Complexity per Line (WMC / LOC)')
plt.legend(title='Class Size')
plt.grid(True)
plt.show()

# Bar Plot: Count of Unmaintainable Classes (Per Class)
unmaintainable_counts = data[['high_wmc', 'low_cohesion']].sum()
unmaintainable_counts.plot(kind='bar', figsize=(8, 6), color=['skyblue', 'salmon'])
plt.title('Count of Unmaintainable Classes')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# --- Additional Analysis: Correlation Between WMC and LCOM for Each Class Size Category ---
# Scatter Plot: WMC vs LCOM (Per Class) for Each Size Category
plt.figure(figsize=(8, 6))
sns.scatterplot(x='wmc', y='lcom', hue='size_category', data=data)
plt.title('WMC vs LCOM by Class Size')
plt.xlabel('Weighted Methods per Class (WMC)')
plt.ylabel('Lack of Cohesion in Methods (LCOM)')
plt.legend(title='Class Size')
plt.grid(True)
plt.show()

# Optional: Comparing Projects: WMC and LCOM Across Projects (Per Class Level)
plt.figure(figsize=(8, 6))
sns.boxplot(x='type', y='wmc', data=data)
plt.title('WMC by Project Type (Per Class)')
plt.xlabel('Project')
plt.ylabel('Weighted Methods per Class (WMC)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='type', y='lcom', data=data)
plt.title('LCOM by Project Type (Per Class)')
plt.xlabel('Project')
plt.ylabel('Lack of Cohesion in Methods (LCOM)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

