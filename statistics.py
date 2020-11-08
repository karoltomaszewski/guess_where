round_of_game = 1
points = 0

def read_record():
    record_file = open("record.txt", "r")
    record = record_file.readline()
    record_file.close()
    return int(record)

def new_record(record):
    record_file = open("record.txt", "r+")
    record_file.truncate(0)
    record_file.write(str(record))
    record_file.close()
