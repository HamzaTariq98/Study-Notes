from imageai.Classification import ImageClassification
import os, sys, pdb
import pandas as pd


def prediction_function(file_name,result_count = 1):
    working_path = os.path.join(execution_path, 'Images')
    predictions, probabilities = prediction.classifyImage(os.path.join(working_path, file_name), result_count = result_count )
    prediction_list.append({'file_name':file_name,'predictions':predictions, 'probabilities':probabilities})


def list_files_in_directory(directory_path):
    files_list = []
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            files_list.append(filename)
    return files_list


# Predefined function by help of ChatGPT to normalise output data
def unstack_columns(df):

    # Create empty lists to store the new data
    new_file_names = []
    new_predictions = []
    new_probabilities = []

    # Iterate through the original DataFrame rows
    for index, row in df.iterrows():
        file_name = row['file_name']
        predictions = row['predictions']
        probabilities = row['probabilities']

        # Iterate through the lists and add elements to the new lists
        for pred, prob in zip(predictions, probabilities):
            new_file_names.append(file_name)
            new_predictions.append(pred)
            new_probabilities.append(prob)

    # Create a new DataFrame from the lists
    new_data = {
        'file_name': new_file_names,
        'predictions': new_predictions,
        'probabilities': new_probabilities
    }
    new_df = pd.DataFrame(new_data)

    return new_df


current_path =  os.path.dirname(sys.argv[0])# Finding current path of script
os.chdir(current_path) # change cwd for desired path as in VScode cwd in desktop
execution_path = os.getcwd()

prediction = ImageClassification()
prediction.setModelTypeAsResNet50()
prediction.setModelPath(os.path.join(execution_path, "resnet50-19c8e357.pth"))
prediction.loadModel()


prediction_list = []

files = list_files_in_directory(os.path.join(execution_path, "Images"))

for file_name in files:
    prediction_function(file_name,1)

prediction_list = unstack_columns(pd.DataFrame(prediction_list))

print(prediction_list)

