import random

def calculate_impatience(current_speed, target_speed, current_impatience):
    """
    Simulates human frustration. If you are stuck going less than 20% 
    of your desired speed, impatience spikes.
    """
    speed_ratio = current_speed / target_speed
    
    if speed_ratio < 0.2:
        # Crawling in traffic -> Get angry fast
        return min(1.0, current_impatience + 0.05)
    elif speed_ratio > 0.6:
        # Moving nicely -> Cool down
        return max(0.0, current_impatience - 0.02)
    
    return current_impatience

def decide_footpath_violation(impatience, compliance, current_lane, position, merge_point):
    """
    The Rule Breaker Logic: Decides if a car jumps onto the footpath (Lane 0).
    """
    # If already on the footpath or past the bottleneck, don't trigger
    if current_lane == 0 or position >= merge_point:
        return False
        
    # The breaking point: High impatience, low compliance
    if impatience > 0.85 and compliance < 0.3:
        # 30% chance to actually do it so they don't all turn at the exact same millisecond
        if random.random() < 0.3:
            return True
            
    return False

def decide_lane_change(car_speed, my_lane_speed, target_lane_speed, aggression):
    """
    Simplified MOBIL Model for Hackathon. 
    Decides if a car wants to change lanes based on potential speed gain.
    """
    # Politeness factor: Aggressive = 0.0 (selfish), Passive = 0.5 (polite)
    politeness = 0.5 - (aggression * 0.5) 
    
    # How much faster will I go if I switch lanes?
    my_potential_gain = target_lane_speed - car_speed
    
    # If the target lane is moving faster
    if target_lane_speed > (my_lane_speed + 2.0):
        # Aggressive drivers switch for a tiny gain (1.0 m/s). 
        # Polite drivers need a bigger gap to justify the switch.
        required_gain = 1.0 + (politeness * 5.0)
        
        if my_potential_gain > required_gain:
            return True
            
    return False