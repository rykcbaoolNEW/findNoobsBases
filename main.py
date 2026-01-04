import math

def compute_waypoint(x0, z0, yaw, dist):
    # Convert Minecraft yaw to standard math angle
    angle_rad = math.radians(-yaw + 90)
    
    xw = x0 + math.cos(angle_rad) * dist
    zw = z0 + math.sin(angle_rad) * dist
    
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
    print(f"Noobs waypoint is: x: {xw:.2f} z: {zw:.2f}")

if __name__ == "__main__":
    main()
main()
