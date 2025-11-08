# add_all_category_revised.py

# Input and output file names
input_file = "channels.m3u"
output_file = "channels_with_all_revised.m3u"

# Read original M3U
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Prepare containers
original_channels_block = []  # To hold the original category channels
all_category_block = []       # To hold the 'ALL' category channels

# Ensure the M3U header is handled only once
# The original file's #EXTM3U line will be used if it's the first line.

# Collect all #EXTINF and their next line (URL)
import re

for i in range(len(lines)):
    line = lines[i]
    
    # Skip the #EXTM3U header line when processing lines for channel blocks
    if line.startswith("#EXTM3U"):
        continue

    if line.startswith("#EXTINF"):
        if i + 1 < len(lines):
            extinf = line
            url = lines[i + 1]

            # 1. Create the 'ALL' Category Duplicate
            new_extinf = extinf

            if "group-title=" in new_extinf:
                # Replace the group-title content with "ALL"
                new_extinf = re.sub(r'group-title="[^"]+"', 'group-title="ALL"', new_extinf)
            else:
                # If no group-title exists, add group-title="ALL"
                new_extinf = new_extinf.replace("#EXTINF:-1", '#EXTINF:-1 group-title="ALL"')

            # Add to the ALL block
            all_category_block.append(new_extinf)
            all_category_block.append(url)

            # 2. Add the Original Channel to its block
            original_channels_block.append(extinf)
            original_channels_block.append(url)


# --- Write Final M3U File ---
with open(output_file, "w", encoding="utf-8") as f:
    
    # Start with the M3U Header
    f.write("#EXTM3U\n")
    
    # 1. Write the Original Categories first
    f.write("\n# -----------------------\n# Original Categories\n# -----------------------\n")
    f.writelines(original_channels_block)

    # 2. Write the ALL category block second (This is the crucial change)
    f.write("\n# -----------------------\n# ALL Category\n# -----------------------\n")
    f.writelines(all_category_block)

print(f"✅ Done! Saved as {output_file}")
