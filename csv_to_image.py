import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

# Load your CSV file
csv_file = 'nutrients.csv'  # Make sure to provide the correct path
df = pd.read_csv(csv_file)

# Replace NaN with empty strings (handle mixed data types)
df = df.map(lambda x: '' if pd.isna(x) else x)

# Set a modern-looking font
plt.rcParams["font.family"] = "sans-serif"

# Set the figure size and plot the table
plt.figure(figsize=(20, 10))
ax = plt.subplot(111, frame_on=False)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# Create the table with specific modifications
col_widths = [0.1] + [0.05] * (len(df.columns) - 1)
tbl = table(ax, df, loc='center', cellLoc='center', colWidths=col_widths, rowLoc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(12)
tbl.scale(1.2, 1.4)  # Increase the second value to increase cell height

# Apply gray background to specific rows and first column
categories = ['Vegetables', 'Tubers', 'Legumes', 'Nuts', 'Fruits', 'Grains', 'Meat']
for position, cell in tbl.get_celld().items():
    if position[0] == 0 or (position[0] > 0 and df.iloc[position[0] - 1, 0] in categories) or position[1] == 0:
        cell.set_facecolor('lightgray')
    cell.set_text_props(fontsize=10)

# Save the figure
plt.savefig('table_image.png', bbox_inches='tight', dpi=300)

# Display the plot
plt.show()

