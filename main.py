import math

def compute_waypoint(x0, z0, yaw, dist):
    # Convert yaw to angle from +X axis
    angle = abs(yaw + 90)
    rad = math.radians(angle)

    dx = dist * math.cos(rad)
    dz = dist * math.sin(rad)

    # Determine signs
    # Minecraft yaw: -90 East, -180 South, -270/90 West, 0 North
    sx = 1 if -180 < yaw < 0 else -1
    sz = 1 if yaw < -90 and yaw > -270 else -1

    xw = x0 + sx * dx
    zw = z0 + sz * dz

    return xw, zw

def main():
    print("Waypoint Calculator")
    print("CODED AND MATH DONE BY RYK_COOL")
    x0 = float(input("Enter player X: "))
    z0 = float(input("Enter player Z: "))
    yaw = float(input("Enter yaw (Minecraft): "))
    dist = float(input("Enter distance to waypoint: "))

    xw, zw = compute_waypoint(x0, z0, yaw, dist)

    print("\n=== Result ===")
    print(f"Waypoint X: {xw:.2f}")
    print(f"Waypoint Z: {zw:.2f}")

if __name__ == "__main__":
    main()
