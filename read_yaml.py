import yaml

def read_yaml(file):
    file_data = open(file, "r") #to open the yaml file with read function
    data = yaml.safe_load(file_data) #safe_load is used to convert thre yaml file datas to dict
    file_data.close() #to close file
    return data 
print(read_yaml('darshan.yaml'))