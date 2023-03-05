import pandas as pd
from sklearn.metrics import mean_squared_error

print("Train RMSE Results")
df = pd.read_csv('../model_output_train_comparison.csv')

df['force_ground_truth'] = df['force_ground_truth'].astype(float)
df['force_prediction'] = df['force_prediction'].astype(float)
print(df.dtypes)

#print(f"Energy RMSE -- {mean_squared_error(df['energy_ground_truth'], df['energy_prediction'], squared=False)}")
#print(f"Force RMSE -- {mean_squared_error(df['force_ground_truth'], df['force_prediction'], squared=False)}")

print("Test RMSE Results")
df = pd.read_csv('../model_output_test_comparison.csv')
#print(f"Energy RMSE -- {mean_squared_error(df['energy_ground_truth'], df['energy_prediction'], squared=False)}")
#print(f"Force RMSE -- {mean_squared_error(df['force_ground_truth'], df['force_prediction'], squared=False)}")

