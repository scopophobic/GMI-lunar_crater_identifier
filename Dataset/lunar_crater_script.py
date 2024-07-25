import csv
import sys

def parse_line(line):
    # Split the line into parts
    parts = line.split()
    
    # The name is everything before the first number
    name = ' '.join(parts[:-3])
    
    # Extract latitude, longitude, and diameter
    lat = parts[-3]
    lon = parts[-2]
    diameter = parts[-1]
    
    # Convert latitude to decimal degrees
    lat_value = float(lat[:-1])
    lat_value = -lat_value if lat.endswith('S') else lat_value
    
    # Convert longitude to decimal degrees
    lon_value = float(lon[:-1])
    lon_value = -lon_value if lon.endswith('W') else lon_value
    
    return [name, f"{lat_value:.2f}", f"{lon_value:.2f}", diameter]

def process_file(input_file, output_file):
    try:
        # Read input file
        with open(input_file, 'r') as file:
            data = file.readlines()

        # Process each line
        formatted_data = [parse_line(line.strip()) for line in data if line.strip()]

        # Write to a CSV file
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Name", "Latitude", "Longitude", "Diameter"])  # Write header
            writer.writerows(formatted_data)  # Write data

        print(f"CSV file '{output_file}' has been created successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.txt output.csv")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        process_file(input_file, output_file)