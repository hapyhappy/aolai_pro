import yaml


def analyse_data(file_name, case_key):
    with open("./data/" + file_name + ".yaml", 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        data = data[case_key]
        temp_list = list()
        for i in data.values():
            temp_list.append(i)

        return temp_list
