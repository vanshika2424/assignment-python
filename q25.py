def copy_file_contents(source_file, destination_file):
    
        
    with open(source_file, 'r') as src:
            
        contents = src.read()

    with open(destination_file, 'w') as dest:
            
        dest.write(contents)
        
    print(f"Contents copied from {source_file} to {destination_file} successfully.")
    
   

source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

copy_file_contents(source_file, destination_file)