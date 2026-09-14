# Original list of data.
academic_majors = [
    "Information Science", "Information Science", 
    "Computer Science", "Information Science", 
    "Data Analytics"
]
compression_key = {
    "Information Science": 1,
    "Computer Science": 2,
    "Data Analytics": 3
}
# Actual List comprehension 
compressed_data = [compression_key[major] for major in academic_majors]

print("Original Data:")
print(academic_majors)

print("\nCompressed Data (Integers):")
print(compressed_data)
