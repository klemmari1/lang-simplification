import json
import sys

import numpy as np


def lang_simplification_algorithm(
    input_points: np.ndarray, tolerance: float, look_ahead: int
) -> np.ndarray:

    if tolerance <= 0:
        raise ValueError("Tolerance must be a positive real number!")

    if len(input_points) < look_ahead:
        return points

    output_points = np.array(input_points[0])
    start_idx = 0

    while True:
        search_region = input_points[
            start_idx : start_idx + look_ahead + 1  # noqa
        ].copy()

        points_within_tolerance, points_removed = get_points_within_tolerance(
            search_region, tolerance
        )
        end_point = points_within_tolerance[-1]
        output_points = np.vstack((output_points, end_point))

        start_idx = start_idx + len(search_region) - 1 - points_removed
        if start_idx == len(input_points) - 1:
            break
    return output_points


def get_points_within_tolerance(
    input_points: np.ndarray, tolerance: float
) -> np.ndarray:
    points = input_points.copy()
    start_point = points[0]
    points_removed = 0

    while True:
        end_point = points[-1]

        intermediate_points = points[1:-1]

        if intermediate_points.size == 0:
            break

        if any(
            get_shortest_distance(start_point, end_point, intermediate_point)
            > tolerance
            for intermediate_point in intermediate_points
        ):
            points_removed += 1
            points = points[:-1]
        else:
            break

    return points, points_removed


def get_shortest_distance(
    start_point: np.ndarray,
    end_point: np.ndarray,
    intermediate_point: np.ndarray,
) -> float:
    # https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line#cite_note-GEO-4
    v = end_point - start_point
    v_hat = v / np.linalg.norm(v)
    return np.linalg.norm(
        (start_point - intermediate_point)
        - np.dot((start_point - intermediate_point), v_hat) * v_hat
    )


if __name__ == "__main__":
    points = np.array(json.loads(sys.argv[1]))
    tolerance = float(sys.argv[2])
    look_ahead = int(sys.argv[3])
    print(lang_simplification_algorithm(points, tolerance, look_ahead))
