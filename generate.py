import pandas as pd
import random

# Generate a fake dataset with latitudes and longitudes within Brazil
def generate_fake_data(df):
    num_rows = len(df)
    data = {
        'LATITUDE': [],
        'LONGITUDE': []
    }
    
    # Define the latitude and longitude boundaries for Brazil
    min_lat, max_lat = -33.75, 5.25
    min_lon, max_lon = -73.75, -34.5
    
    for _ in range(num_rows):
        lat = round(random.uniform(min_lat, max_lat), 6)
        lon = round(random.uniform(min_lon, max_lon), 6)
        data['LATITUDE'].append(lat)
        data['LONGITUDE'].append(lon)
    
    new_df = pd.DataFrame(data)
    return pd.concat([df, new_df], axis=1)

# Read the original CSV file
df_original = pd.read_csv('key_account.csv')

# Generate a fake dataset with store locations and append the latitude and longitude columns
df_fake = generate_fake_data(df_original)

# Save the modified dataset as a new CSV file
df_fake.to_csv('key_account_fake_store_locations.csv', index=False)