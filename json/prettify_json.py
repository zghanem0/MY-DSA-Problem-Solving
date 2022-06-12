file_content = json.loads(file) # convert json to dic to be able to edit on it
def replace_status(file_content):
    file_content['status'] = desired_state. # change sth in dic
    replaced_file = json.dumps(file_content, sort_keys=True, indent=4, separators=(',', ': ')) # then convert the json back to be json but a pretty json not in one line 
    return replaced_file
