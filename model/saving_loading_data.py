import pickle
import os


class SavingAndLoadingData:
    def __init__(self, pickle_folder='pickle_files', **args):
        # The filenames for all the files I will need
        self.PICKLE_FOLDER = pickle_folder
        # print(os.path.join(self.PICKLE_FOLDER, self.FAKE_TWEETS_FILENAME))

    # Saves the data to a file stored in saved data
    # Params: my_data, the object you want to save, filename, where you want to store the file
    def save_data(self, my_data, filename):
        with open(os.path.join(self.PICKLE_FOLDER, filename), 'wb') as fe_data_file:
            pickle.dump(my_data, fe_data_file)
        return my_data

    # loads a data from a file
    # params: filename, the name of a file stored in the default pickle folder
    def load_saved_data(self, filename):
        with open(os.path.join(self.PICKLE_FOLDER, filename), 'rb') as fe_data_file:
            feature_engineered_data = pickle.load(fe_data_file)
        return feature_engineered_data
