import matplotlib.pyplot as plt 

def create_barplot(activity_list):
    # X-axis: Time in discrete time steps (seconds / delta_t)
    x = range(len(activity_list))

    # Y-axis: Activity values
    y = activity_list

    # Create the Bar plot
    plt.bar(x, y)

    # Set X-axis
    plt.xlabel('Time (seconds / delta_t)')

    # Set Y-axis and set the maximum
    plt.ylabel('Activity')
    plt.ylim(0, max(activity_list) * 1.1)  # Increase the maximum of the Y-axis by 10%

    # Show the plot
    plt.show()