import random

def calculate_impatience(current_speed, target_speed, current_impatience):
    """
    Simulates human frustration. If you are stuck going less than 20% 
    of your desired speed, impatience spikes.
    """
    speed_ratio = current_speed / target_speed
    
    if speed_ratio < 0.5:
        # Crawling in traffic -> Get angry fast
        return  current_impatience + 0.05
    elif speed_ratio > 0.6:
        # Moving nicely -> Cool down
        return current_impatience - 0.02
    
    
    return current_impatience

def decide_footpath_violation(impatience, compliance, current_lane, position, merge_point):
    """
    The Rule Breaker Logic: Decides if a car jumps onto the footpath (Lane 0).
    """
    # If already on the footpath or past the bottleneck, don't trigger
    if current_lane == 0 or position >= merge_point or position <= 200:
        return False
        
    # The breaking point: High impatience, low compliance
    if impatience > 0.85 or compliance < 0.2:
        # 30% chance to actually do it so they don't all turn at the exact same millisecond
        if random.random() < 0.1:
            return True
            
    return False

def decide_footpath_violation_challan(impatience, compliance, current_lane, position, merge_point, Car_ID, challan_list):
    """
    The Rule Breaker Logic: Decides if a car jumps onto the footpath (Lane 0).
    """
    # If already on the footpath or past the bottleneck, don't trigger
    if current_lane == 0 or position >= merge_point or position <= 200:
        return False
        
    # The breaking point: High impatience, low compliance
    if (impatience > 0.85 or compliance < 0.2) and Car_ID in challan_list['Car_ID'].values:
        # 30% chance to actually do it so they don't all turn at the exact same millisecond
        challan_count = challan_list.loc[challan_list['Car_ID'] == Car_ID, 'Challan'].values[0]
        if challan_count> 2 and random.random() < 0.05:
            return True
    elif (impatience > 0.85 or compliance < 0.2) :
        # 30% chance to actually do it so they don't all turn at the exact same millisecond
        if random.random() < 0.1:
            return True
            
    return False

def decide_target_lane(current_lane, lane_densities, aggression):
    """
    Density-based lane change model across all 3 highway lanes.
    Returns the lane number the car should move to, or the current lane if it stays put.
    """
    # 1. PHYSICAL CONSTRAINTS: Which lanes can we actually steer into?
    # Lane 1 (Left) can only go to Lane 2 (Center)
    # Lane 3 (Right) can only go to Lane 2 (Center)
    # Lane 2 (Center) has the choice of going Left (1) or Right (3)
    if current_lane == 1:
        adjacent_lanes = [2]
    elif current_lane == 3:
        adjacent_lanes = [2]
    else: 
        adjacent_lanes = [1, 3]

    # 2. ENVIRONMENTAL AWARENESS: Find the best adjacent lane
    # We look at the dictionary and pick the lane with the absolute lowest number of cars
    best_target_lane = min(adjacent_lanes, key=lambda l: lane_densities.get(l, 0))
    
    my_lane_density = lane_densities.get(current_lane, 0)
    target_lane_density = lane_densities.get(best_target_lane, 0)

    # 3. THE PRESSURE GAUGE: How much emptier is that other lane?
    density_advantage = my_lane_density - target_lane_density
    
    # If the best lane is equally crowded or worse, don't bother moving.
    if density_advantage <= 0:
        return current_lane
        
    # 4. THE HUMAN FACTOR (Psychology Threshold)
    # This formula scales based on the car's random aggression level (0.0 to 1.0)
    # - A highly aggressive driver (1.0) needs only 2 fewer cars to violently switch lanes.
    # - A passive, polite driver (0.0) needs a massive gap of 8 fewer cars to feel safe switching.
    required_advantage = 8.0 - (aggression * 6.0) 
    
    # 5. THE FINAL DECISION
    # If the relief of moving outweighs the driver's personal hesitation...
    if density_advantage >= required_advantage:
        return best_target_lane # SWERVE!
        
    # Otherwise, accept your fate and stay in the current lane.
    return current_lane




def calculate_variable_speed_limits(lane_densities, base_speed=25.0):
    """
    Calculates optimal speed limits for each lane based on current congestion.
    Harmonizes speeds to prevent shockwaves and discourage aggressive weaving.
    """
    target_speeds = {1: base_speed, 2: base_speed, 3: base_speed}
    
    # If the road is relatively empty, don't intervene
    total_cars = sum(lane_densities.values())
    if total_cars < 5:
        return target_speeds
        
    # 1. Apply Density Penalties
    for lane in [1, 2, 3]:
        density = lane_densities.get(lane, 0)
        
        # Every car above a safe baseline (e.g., 5 cars) drops the speed limit.
        # This smoothly compresses the pack before they hit the bottleneck.
        if density > 5:
            speed_reduction = (density - 5) * 0.8  # Lose 0.8 m/s per extra car
            target_speeds[lane] = max(8.0, base_speed - speed_reduction) # Never drop below 8 m/s
            
    # 2. SPEED HARMONIZATION (Crucial for safety)
    # We do not allow adjacent lanes to have a speed limit difference of more than 5 m/s.
    # If Lane 2 is jammed and going 10 m/s, Lanes 1 and 3 are forced down to 15 m/s max 
    # to stop aggressive drivers from darting out of Lane 2.
    for _ in range(2): # Run twice to smooth the edges across all 3 lanes
        if target_speeds[1] - target_speeds[2] > 5: target_speeds[1] = target_speeds[2] + 5.0
        if target_speeds[3] - target_speeds[2] > 5: target_speeds[3] = target_speeds[2] + 5.0
        if target_speeds[2] - target_speeds[1] > 5: target_speeds[2] = target_speeds[1] + 5.0
        if target_speeds[2] - target_speeds[3] > 5: target_speeds[2] = target_speeds[3] + 5.0
        
    return target_speeds