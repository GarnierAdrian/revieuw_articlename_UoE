import random
from math import floor
import sys


def main():
    if len(sys.argv) < 2:
        filename = "default_data"

    else:
        filename = sys.argv[1]

    print(f"Using filename: {filename}.dat")

    if len(sys.argv) < 3:
        print("Using default seed: 42")
        random.seed(42)

    else:
        print(f"Using argument seed: {sys.argv[2]}")
        random.seed(int(sys.argv[2]))

    TIMESTEPS = 30
    ORDERS = 50
    OU = 10
    MAX_ORDER_DURATION = 20
    MIN_ORDER_DURATION = 5
    FREEZE_PERCETNAGE = 0
    RESOURCE_TYPES = 2
    MINIMUM_RESOURCE_UNIT = 100
    MAXIMUM_RESOURCE_UNIT = 300    
    MINIMUM_RESOURCE_COST = 500
    MAXIMUM_RESOURCE_COST = 900
    MIN_VOLUME = 300
    MAX_VOLUME = 400

    f = open(f"{filename}.dat", "w")

    f.write(f"Timesteps: {TIMESTEPS}\n")
    f.write(f"Orders: {ORDERS}\n")
    f.write(f"OU: {OU}\n")
    f.write(f"ResourceTypes: {RESOURCE_TYPES}\n")

    volumes = [random.randint(MIN_VOLUME,MAX_VOLUME) for _ in range(ORDERS)]

    f.write(f"Volumes: [{' '.join(map(str, volumes))}]\n")

    order_start = [random.randint(0,TIMESTEPS-MAX_ORDER_DURATION) for _ in range(ORDERS)]

    f.write(f"OrderRelease: [{' '.join(map(str, order_start))}]\n")

    order_ends = [start + random.randint(MIN_ORDER_DURATION, MAX_ORDER_DURATION) for start in order_start]

    f.write(f"OrderDue: [{' '.join(map(str, order_ends))}]\n")

    freeze = [0 if random.random() >= FREEZE_PERCETNAGE else 1 for _ in range(ORDERS)]

    f.write(f"Freeze: [{' '.join(map(str, freeze))}]\n")

    f.write(f"FrozenOU: [{' '.join(map(str, range(sum(freeze) + 1)[1:]))}]\n")

    minimum_duration_in_period = []
    for start, finish in zip(order_start, order_ends):
        difference = finish - start
        reduction = difference*random.random()
        minimum_duration_in_period.append(floor(reduction))

    f.write(f"MinimumDuration: [{' '.join(map(str, minimum_duration_in_period))}]\n")

    #resource_unit_time = [random.randint(MINIMUM_RESOURCE_UNIT, MAXIMUM_RESOURCE_UNIT) for _ in range(TIMESTEPS) 
    #    for _ in range(OU) for _ in range(RESOURCE_TYPES)]

    resource_unit_time = []
    for _ in range(OU):
        platforms = random.randint( 3, 6)
        for _ in range(TIMESTEPS):
            resource_unit_time.append(platforms)

    for _ in range(OU):
        people = random.randint( 2, 5)
        for _ in range(TIMESTEPS):
            resource_unit_time.append(people * 8)


    f.write(f"ResourceOUTime: [{' '.join(map(str, resource_unit_time))}]\n")


    Order_Cost  = []
    for _ in range(ORDERS):
        platforms = random.randint( 3, 6)
        duration = random.randint(3, 5)
        Order_Cost.append(platforms)

    for _ in range(ORDERS):
        people = random.randint( 2, 4)
        duration = random.randint(5, 10)
        Order_Cost.append(people * 8 * duration)
    #Order_Cost.extend(volumes)


    f.write(f"OrderCost: [{' '.join(map(str, Order_Cost))}]\n")

    f.close

if __name__ == "__main__":
    main()