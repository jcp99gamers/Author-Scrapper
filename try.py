import datetime
timestamp_str = "2023-03-07T14:13:32+05:30"
timestamp = datetime.datetime.fromisoformat(timestamp_str)
formatted_timestamp = timestamp.strftime('%d-%m-%Y %H:%M:%S %Z')
print(formatted_timestamp)