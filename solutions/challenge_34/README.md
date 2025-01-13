# Euclidean Distance Function

This repository contains a Python implementation of the **Euclidean distance** function,
along with a set of unit tests to verify its correctness. The Euclidean
distance is a measure of the straight-line distance between two points in Euclidean
space. It is widely used in various fields like geometry, machine learning, and
data analysis.

## Description

The `euclidean_distance` function calculates the distance between two points in a
multi-dimensional space. It is based on the formula:

$$
\text{distance} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + \dots + (z_2 - z_1)^2}
$$

The function works with points in any dimension (e.g., 2D, 3D) and returns the
Euclidean distance between them.

## Features

- Supports 2D and 3D points.
- Handles cases with negative coordinates.
- Throws an error when points with different dimensions are provided.

## Requirements

- Python 3.x
- `unittest` (Standard Python library for testing)
