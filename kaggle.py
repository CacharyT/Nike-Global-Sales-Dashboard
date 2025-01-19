import kagglehub

# Download latest version
path = kagglehub.dataset_download("ayushcx/nike-global-sales-data-2024")

print("Path to dataset files:", path)