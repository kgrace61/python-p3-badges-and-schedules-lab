def badge_maker(name):
    return (f'Hello, my name is {name}.')

def batch_badge_creator(names):
    badge_messages = []
    
    for name in names:
        badge_message = (f'Hello, my name is {name}.')
        badge_messages.append(badge_message)
    return badge_messages

def assign_rooms(names):
    room_assignments = []
    
    for i, name in enumerate(names, start=1):
        room_assignment = f"Hello, {name}! You'll be assigned to room {i}!"
    
        room_assignments.append(room_assignment)
    
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    
    for badge in badges: 
        print(badge)
        
    assignments = assign_rooms(names)
    for assignment in assignments:
        print(assignment)
    
