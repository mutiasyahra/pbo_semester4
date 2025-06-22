def read_json_file(file_path):
    import json
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def write_json_file(file_path, data):
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def append_to_json_file(file_path, new_data):
    data = read_json_file(file_path)
    data.update(new_data)
    write_json_file(file_path, data)