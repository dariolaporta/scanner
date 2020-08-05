import glob


# Returns a list of names in list files.
print("Using glob.glob()")
files = glob.glob('/Users/temera/Desktop/Lavoranti_Bulgari_2020/**/*.txt',
                  recursive=True)
for file in files:
    print(file)
