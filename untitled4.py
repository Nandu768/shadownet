import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Generate time and traffic arrays
time = np.arange(0, 100, 1)
traffic = np.random.randint(0, 100, len(time))

# Add a zig-zag pattern (simulate alternating increase and decrease in traffic)
for i in range(1, len(traffic)):
    if i % 2 == 0:
        traffic[i] = traffic[i-1] + np.random.randint(1, 10)  # Increase
    else:
        traffic[i] = traffic[i-1] - np.random.randint(1, 10)  # Decrease

# Initialize line object
line, = ax.plot([], [], label="Network Traffic", color='b', marker='o')

# Set up plot limits
ax.set_xlim(0, len(time))
ax.set_ylim(min(traffic)-10, max(traffic)+10)

# Function to update the plot
def update(frame):
    line.set_data(time[:frame], traffic[:frame])
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(time), interval=100, blit=True)

# Save the animation as a GIF
ani.save("network_traffic_zigzag.gif", writer='pillow', fps=10)

# Show the plot if you need
plt.close(fig)






import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_pdf import PdfPages

# Generate time and traffic arrays
time = np.arange(0, 100, 1)
traffic = np.random.randint(0, 100, len(time))

# Add a zig-zag pattern (simulate alternating increase and decrease in traffic)
for i in range(1, len(traffic)):
    if i % 2 == 0:
        traffic[i] = traffic[i-1] + np.random.randint(1, 10)  # Increase
    else:
        traffic[i] = traffic[i-1] - np.random.randint(1, 10)  # Decrease

# Define a threshold for high traffic
threshold = 60  # You can adjust this threshold value

# Create a figure for plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Separate high and normal traffic
high_traffic = traffic > threshold
normal_traffic = ~high_traffic

# Plot the traffic with different colors based on thresholds
ax.plot(time[normal_traffic], traffic[normal_traffic], label="Normal Traffic", color='b', marker='o')
ax.plot(time[high_traffic], traffic[high_traffic], label="High Traffic", color='r', marker='o')

# Customize plot labels and title
ax.set_title('Network Traffic Analysis (Zig-Zag Pattern)')
ax.set_xlabel('Time')
ax.set_ylabel('Traffic')
ax.legend()

# Save the plot into a PDF
with PdfPages('network_traffic_analysis.pdf') as pdf:
    pdf.savefig(fig)  # Saves the current figure into a PDF file
    plt.close(fig)    # Close the figure to release memory

print("PDF has been saved as 'network_traffic_analysis.pdf'.")











import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_pdf import PdfPages

# Generate time and traffic arrays
time = np.arange(0, 40, 1)
traffic = np.random.randint(0, 25, len(time))

# Add a zig-zag pattern (simulate alternating increase and decrease in traffic)
for i in range(1, len(traffic)):
    if i % 2 == 0:
        traffic[i] = traffic[i-1] + np.random.randint(1, 10)  # Increase
    else:
        traffic[i] = traffic[i-1] - np.random.randint(1, 10)  # Decrease

# Define a threshold for high traffic
threshold = 15  # You can adjust this threshold value

# Create a figure for plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Separate high and normal traffic
high_traffic = traffic > threshold
normal_traffic = ~high_traffic

# Plot the traffic with different colors based on thresholds
line_normal, = ax.plot([], [], label="Normal Traffic", color='b', marker='o')
line_high, = ax.plot([], [], label="High Traffic", color='r', marker='o')

# Customize plot labels and title
ax.set_title('Network Traffic Analysis (Zig-Zag Pattern)')
ax.set_xlabel('Time')
ax.set_ylabel('Traffic')
ax.legend()
ax.set_xlim(0, len(time))
ax.set_ylim(min(traffic)-10, max(traffic)+10)

# Function to update the plot for animation
def update(frame):
    # Update the data for normal and high traffic lines
    line_normal.set_data(time[:frame][normal_traffic[:frame]], traffic[:frame][normal_traffic[:frame]])
    line_high.set_data(time[:frame][high_traffic[:frame]], traffic[:frame][high_traffic[:frame]])
    return line_normal, line_high

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(time), interval=100, blit=True)

# Save the animation as a GIF
ani.save("network_traffic_zigzag.gif", writer='pillow', fps=10)

# Save the final plot as a PDF
with PdfPages('network_traffic_analysis.pdf') as pdf:
    pdf.savefig(fig)  # Save the final frame of the plot to the PDF
    plt.close(fig)    # Close the figure to release memory

print("GIF has been saved as 'network_traffic_zigzag.gif'.")
print("PDF has been saved as 'network_traffic_analysis.pdf'.")




















