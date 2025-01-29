import kagglehub

# Download latest version
path = kagglehub.dataset_download("ankushpanday1/tuberculosis-tb-predictiontop-75-countries")

print("Path to dataset files:", path)