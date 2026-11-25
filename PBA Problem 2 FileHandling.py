input_file = "input.txt"
output_file = "cleaned.txt"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

with open(output_file, "w", encoding="utf-8") as f:
    for line in lines:
        if line.strip():
            f.write(line)

print("Blank lines removed successfully!")
print(f"Output saved to {output_file}")
