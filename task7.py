import datetime
def textfile_timestamp():
    time = datetime.datetime.now()
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = (f"text_file {timestamp}.txt") # Creating a file with timestamp

    # Writing content to the file:
    with open( file_name,"w+") as file:
        file.write(timestamp)

    print (f"Text file '{file_name} created with the Content:{timestamp}.")
    file.close()
textfile_timestamp()


