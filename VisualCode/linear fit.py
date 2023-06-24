import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot

sol_df = pd.read_csv(r"C:\Users\USER\Desktop\Omri_Yarden\VisualCode\Soulitions_Summery_with_cal_device.csv", encoding='Windows-1255')
sol_df

# Create the scatter plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=1/sol_df['Conductivity [uS/cm]'], y=sol_df['Impedance [Ohm]'], mode='markers'))
fig.add_trace(go.Scatter(x=1/sol_df['Conductivity [uS/cm]'], y=sol_df['Impedance [Ohm]'], mode='lines'))

# Perform linear regression
x = 1/sol_df['Conductivity [uS/cm]']
y = sol_df['Impedance [Ohm]']
coeffs = np.polyfit(x, y, 1)  # Perform linear regression, returns the coefficients
line = np.poly1d(coeffs)  # Create a function based on the coefficients
x_range = np.linspace(x.min(), x.max(), 100)  # Generate x values for the line
y_range = line(x_range)  # Calculate corresponding y values

# Add the regression line to the plot
fig.add_trace(go.Scatter(x=x_range, y=y_range, mode='lines', name='Linear Fit'))

# Update the layout and show the figure
fig.update_layout(title='Impedance vs 1/Conductivity [cm/uS]', xaxis_title='1/Conductivity [cm/uS]', yaxis_title='Impedance [Ohm]')
fig.show()

# Save the figures to HTML file
with open('plotly_figures.html', 'w') as f:
    f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))
