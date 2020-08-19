# csv is used for reading and writing csv files and their rows
import csv


# This method splits positive dataset rows from negative dataset rows
# and puts each in a separate datafile respectively
def pos_neg_splitter():

    # Open cleaned up datafile in read-only mode
    clean_input = open('Clean_Datafile.csv', 'r')

    # Read cleaned up datafile as csv and load it to loaded_clean_dataset object
    loaded_clean_dataset = csv.reader(clean_input)

    # Create and open a datafile for output writers of each positive and negative dataset
    positive_output = open('Positive_DataSet.csv', 'w', newline="")
    negative_output = open('Negative_DataSet.csv', 'w', newline="")

    # Initialize a csv writer for each datafile which gives the ability of
    # writing desired rows into datafiles
    positive_output_writer = csv.writer(positive_output)
    negative_output_writer = csv.writer(negative_output)

    print("Splitting dataset to negative and positive datasets...")

    # Iterating through loaded_clean_dataset and separating rows by their first column value
    # then adding them to their relative csv.writer to be written on relative datafile
    for selected_row in loaded_clean_dataset:
        if str(selected_row[0]) != "0":
            positive_output_writer.writerow(selected_row)
        else:
            negative_output_writer.writerow(selected_row)


# This method splits positive and negative datasets into given ranges
# so train and test data sets will be generated by combining these split ranges
def train_test_splitter():

    # Open each positive and negative dataset in read-only mode
    positive_input = open('Positive_DataSet.csv', 'r')
    negative_input = open('Negative_DataSet.csv', 'r')

    # Create and Open train and test dataframes for train and test dataset writers
    train_output = open('Train_DataFrame.csv', 'w', newline="")
    test_output = open('Test_DataFrame.csv', 'w', newline="")

    # Read positive and negative datafiles as csv and load them to their relative datasets
    positive_dataset = csv.reader(positive_input)
    negative_dataset = csv.reader(negative_input)

    # Initialize a csv writer for each train and test datafile which gives the ability of
    # writing desired rows into datafiles
    dataset_train_writer = csv.writer(train_output)
    dataset_test_writer = csv.writer(test_output)

    # Add label rows for each file which is required by pandas
    dataset_train_writer.writerow(["State", "Comment"])
    dataset_test_writer.writerow(["State", "Comment"])

    print("Splitting positive and negative datasets to train and test datasets...")

    # Iterating through positive_dataset and separating rows by the given range (hard coded range)
    # then adding them to their relative csv.writer to be written on relative train or test datafile
    index = 0
    for row in positive_dataset:
        if 0 <= index < 640000:
            dataset_train_writer.writerow(["positive", row[1]])
            index += 1
        elif 640000 <= index < 800000:
            dataset_test_writer.writerow(["positive", row[1]])
            index += 1
        else:
            index += 1

    # Iterating through negative_dataset and separating rows by the given range (hard coded range)
    # then adding them to their relative csv.writer to be written on relative train or test datafile
    index = 0
    for row in negative_dataset:
        if 0 <= index < 640000:
            dataset_train_writer.writerow(["negative", row[1]])
            index += 1
        elif 640000 <= index < 800000:
            dataset_test_writer.writerow(["negative", row[1]])
            index += 1
        else:
            index += 1


# Entry point of python file execution
print("Step 2 of 3")
print("Beginning split process...")
pos_neg_splitter()
train_test_splitter()
print("Split process completed successfully!")
