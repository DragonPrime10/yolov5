import os

def replace_first_character(folder_path):
    # Get the list of files in the specified folder
    files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        # Read the content of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Replace the first character of each line with '1'
        lines = ['4' + line[1:] for line in lines]

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)

if __name__ == "__main__":
    # Replace 'your_folder_path' with the actual path of your folder
    folder_path = '/Users/reidwilson/Desktop/Software Project AI Stuff/yolov5/pikachu/train/labels'

    replace_first_character(folder_path)
