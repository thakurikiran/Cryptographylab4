import os

def copy_self(target_directory, file_count):
    
    current_script = os.path.abspath(__file__)

   
    with open(current_script, 'r') as f:
        script_content = f.read()

   
    for i in range(file_count):
        file_path = os.path.join(target_directory, f'copy_{i+1}.py')

       
        with open(file_path, 'w') as target_file:
            target_file.write(script_content)

if __name__ == "__main__":
   
    target_directory = "./lab4cryptography"
    
   
    file_count = 1

    
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

   
    copy_self(target_directory, file_count)