from matplotlib import pyplot as plt
from matplotlib import animation as anim


def visualise(algorithm, array):
    fig, ax = plt.subplots()
    # ax.set_title(title)
    bar_rec = ax.bar(range(len(array)), array, align='edge', color="g")
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    epochs = [0]
    def update_plot(array, rec, epochs):
        for rec, val in zip(rec, array):
            rec.set_height(val)
        epochs[0]+= 1
        text.set_text(f"No.of operations :{epochs[0]}")

    animate = anim.FuncAnimation(
        fig, 
        func=update_plot, 
        fargs=(bar_rec, epochs), 
        frames=algorithm, 
        interval=1, 
        repeat=False
        )

    return plt.show()
