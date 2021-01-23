import matplotlib.pyplot as plt
import numpy as np

from lang_simplification import lang_simplification_algorithm


def plot_lang(points_before: np.ndarray, points_after: np.ndarray) -> None:
    _, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    ax1.title.set_text("before")
    ax2.title.set_text("after")

    ax1.plot(*np.transpose(points_before))
    ax2.plot(*np.transpose(points_after))

    plt.savefig("example.png")


if __name__ == "__main__":
    input_points = np.array([[0, 1], [1, 12], [2, 3], [4, 5], [6, 14], [7, 12], [8, 1]])

    output_points = lang_simplification_algorithm(input_points, 2, 3)
    plot_lang(
        input_points,
        output_points,
    )
