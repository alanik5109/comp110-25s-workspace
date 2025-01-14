import pandas as pd

file_path = 'C:/Users/Abigail Lanik/Desktop/Compared_D4_Events_16-2_16-3.csv'
data = pd.read_csv(file_path)

def align_times_and_compare(df, tolerance=0.5):
    # Create a new DataFrame to store the comparison results
    comparison_df = pd.DataFrame(columns=['Subject', 'Behavior', 'Time', 'Image index',
                                          'Comparison', 'Observation id.1', 'Behavior.1',
                                          'Time.1', 'Image index.1'])
    
    # Convert times to numeric (just in case they are not)
    df['Time'] = pd.to_numeric(df['Time'], errors='coerce')
    df['Time.1'] = pd.to_numeric(df['Time.1'], errors='coerce')
    
    # Excluding empty or all-NA columns
    df = df.dropna(axis=1, how='all')
    
    # Start with the first dataframe's times
    for index, row in df.iterrows():
        # Find the closest time in the second dataframe within the tolerance
        closest_times = df[(df['Time.1'] >= row['Time'] - tolerance) & (df['Time.1'] <= row['Time'] + tolerance)]
        
        # If there is a closest time, then set "yes" in the Comparison column
        if not closest_times.empty:
            closest_time = closest_times.iloc[0]  # Take the first closest time
            comparison_df = comparison_df._append({
                'Subject': row['Subject'],
                'Behavior': row['Behavior'],
                'Time': row['Time'],
                'Image index': row['Image index'],
                'Comparison': 'yes',
                'Observation id.1': closest_time['Observation id.1'],
                'Behavior.1': closest_time['Behavior.1'],
                'Time.1': closest_time['Time.1'],
                'Image index.1': closest_time['Image index.1']
            }, ignore_index=True)
        else:
            # If no match is found, just copy the row without "yes" in Comparison
            comparison_df = comparison_df._append(row, ignore_index=True)

    return comparison_df

# Apply the function to the dataset
comparison_result = align_times_and_compare(data)

# Write the result to a new CSV file
output_file_path = '/Users/Abigail Lanik/Desktop/Analyzed_D4_Events_16-2_16-3.csv'
comparison_result.to_csv(output_file_path, index=False)

output_file_path