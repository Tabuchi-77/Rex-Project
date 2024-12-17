import torch
import xarray as xr  # or from netCDF4 import Dataset

# Load the .nc file
file_path = 'potential_vorticity_2018_5.625deg.nc'
data = xr.open_dataset(file_path)

# Inspect the data
print(data)

# Select a variable (e.g., 'temperature') and convert it to a PyTorch tensor
numpy_array = data['lat'].values  # Replace 'temperature' with your variable name
tensor = torch.from_numpy(numpy_array)


# Check the tensor
print(tensor.shape)
print(tensor.dtype)
