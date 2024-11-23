import matplotlib.pyplot as plt
import numpy as np

# Example stock data (dates and prices)
dates = np.array(['2024-10-01', '2024-10-02', '2024-10-03', '2024-10-04', '2024-10-05'])
prices = np.array([100, 102, 98, 105, 110])

# Corresponding news headlines
news = {
    '2024-10-01': "Company A releases new product.",
    '2024-10-02': "Stock dips after earnings report.",
    '2024-10-03': "CEO announces resignation.",
    '2024-10-04': "Market rallies, stock price increases.",
    '2024-10-05': "New partnership boosts company’s outlook."
}

# Convert date strings to a format matplotlib can handle (optional if using datetime)
x = np.arange(len(dates))  # Simple index for x-axis

# Create a figure and axis
fig, ax = plt.subplots()
sc = ax.scatter(x, prices)

# Annotate point (tooltip-like)
annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

# Update annotation with the correct data
def update_annot(ind):
    idx = ind["ind"][0]
    annot.xy = (x[idx], prices[idx])
    text = f"{dates[idx]}: {news[dates[idx]]}"
    annot.set_text(text)

# Event handler for hovering
def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

# Connect the hover event
fig.canvas.mpl_connect("motion_notify_event", hover)

# Show the plot
plt.show()
