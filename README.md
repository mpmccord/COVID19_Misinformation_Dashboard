# COVID19_Misinformation_Dashboard
This is a dashboard to track COVID-19 Misinformation and output a result given a url
Project Structure
app.py: Runs the webpage
static: default given by Flask
Directories

- getting_data
files:
get_data_from_url.py

- GetDataFromURL:
Given a url, preprocesses the data and returns it as a url.
  - Methods:
    - getHTMLText(self, url):
      Gets the data from a url and returns it as a string.
    - cleanURLData:
      returns the title and text from the url.
    - getDataFromURL:
      main function that preprocesses the url given these functions and returns the title and url.

- model
  - directories:
      - pickle_files:
        where the classifiers are stored
  - files:
     -- preprocessing_data.py
        -- classes: PreProcessingData
          -- methods: 
            -- createDataFromURL
            : uses functions stored in preprocess_data in order to count spelling mistakes, create a bag of words model from website on both title and content
            -- removeUnneededData
            :removes all columns that were not found in the original data
            throws an error if all are not found: empty DataFrame
            -- addEmptyColumns:
              :if there is data that is not found, creates columns with that data that are 0s
          -- preProcessData:
            : runs these commands and returns the resulting dataframe of one sample.
    -- run_model.py
      -- classes: RunModel
        --methods:
          -- getMostInfluentialFeatures:
            finds the features with the largest weights in the original model
          -- getMostInfluentialFromDataframe:
            finds the features with the most influential features and strongest variance
          -- getClassesCorrespondingToWeights:
            gets the features corresponding to the weights and then creates a new website from that.
            returns a dictionary, i.e. {0: Fake, 1: Real}
          -- showExplanation:
              given most influential features from dataframe, gets the classes and returns a string representing the classification.
              returns a string.
          -- runModelAndPrintExplanation:
            opens the classifier pickle_file, runs it on the resulting dataframe.
            then uses show explanation in order to print the explanation.
       
    -- saving_loading_data.py
      -- class SavingAndLoadingData:
        : saves data to a pickle file and loads data from a pickle file.
          
  -- preprocessData:
    -- create_bag_words.py
      -- creates a bag of words model from text and returns it as a dataframe.
    -- spell_check.py
      -- checks the spelling of words using language_tool.
      
      -- SpellCheck:
          creates a language tool object using language tool in order to check spelling.
          -- countMistakes:
            -- runs language tool to find the mistakes and returns the number of mistakes found.
-- static:
  default template for storing things like styles.
-- templates:
  -- index.html
    -- Creates a form for the data preprocessing
    -- If given a text explanation, prints it below the form.
-- app.py
  -- runs the application.
      
      
