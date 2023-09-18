I didn’t understand how `docker compose` was supposed to be used and why. I provided some `compose.yaml` file but it seems useless and you can build my solution using `docker build` and `docker run`.

# Use of the utility

```shell
app.py [-n <map dimensions>] [-s <cell size>]
```
By default `n=5` and `s=1`

The utility generates a random map `n x n`, prints it and coordinates of obstacles closest to the robot.

Notations:
* `.` --- free cell
* `#` --- obstacle
* `R` --- robot
