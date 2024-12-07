import json

with open('C:/Users/Public/Documents/Input/Milestone0.json', 'r') as file:
    data = json.load(file)


steps = data['steps']
machines = data['machines']
wafers = data['wafers']
quantity = wafers[0]['quantity']  
processing_times = wafers[0]['processing_times']

# Create machine-step mapping
machine_steps = {m['machine_id']: m['step_id'] for m in machines}


wafer_status = [{'name': f'W1-{i + 1}', **{step['id']: 'True' for step in steps}} for i in range(quantity)]
schedule = []

machine_available_time = {m['machine_id']: 0 for m in machines}
times = {}  
for wafer in wafer_status:
    for step_id in [step['id'] for step in steps]:
        for m_id,s_id in machine_steps.items():
            if s_id==step_id:
                machine_id=m_id
                start_time = max(machine_available_time[machine_id], times.get(wafer['name'], 0)) 
                end_time = start_time + processing_times[step_id]

        schedule.append({
            'wafer_id': wafer['name'],
            'step': step_id,
            'machine': machine_id,
            'start_time': start_time,
            'end_time': end_time
        })

        machine_available_time[machine_id] = end_time  
        times[wafer['name']] = end_time 

new_dict = {'schedule': schedule}
print(new_dict)

with open('C:/Users/Public/Documents/m1.json',"w") as file:
    json.dump(new_dict,file)
print(new_dict)
