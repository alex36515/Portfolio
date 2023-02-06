import pandas as pd
import re

current_prep_data = []

with open('Data/prep_data.txt', 'r', encoding="utf8") as f:
    output_value = []
    # Iterate through the lines
    for line in f:
        # Use the regular expression to check if the line starts with a number
        if re.match(r'^\d', line.lstrip().rstrip()):
            # Appends the succesive line values that start with a number to the same current_prep_data index
            output_value.append(line.lstrip().rstrip())
            continue

        if output_value:
            output_value[0] = ">" + output_value[0]
            output_string = ' >'.join(output_value)
            current_prep_data.append([output_string.lstrip().rstrip()])
            output_value = []
            

        #if line is not empty append to current_prep_data
        if line != '\n':
            current_prep_data.append([line.lstrip().rstrip()])

    output_value[0] = ">" + output_value[0]
    output_string = ' >'.join(output_value)
    current_prep_data.append([output_string.lstrip().rstrip()])

# convert current_prep_data into a 1d list
current_prep_data_1d = [item for sublist in current_prep_data for item in sublist]

# convert current_prep_data into a 2d list with two columns
current_prep_data = [current_prep_data_1d[i:i+2] for i in range(0, len(current_prep_data_1d), 2)]


print(current_prep_data)

df = pd.DataFrame(current_prep_data, columns=['Review', 'Output'])


# Write the DataFrame to a CSV file
df.to_csv('prep_data.csv', index=False)
df = pd.read_csv('prep_data.csv')
print(df)