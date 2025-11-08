# add_all_category.py (Revised for clarity, logic remains largely the same)

# Input and output file names
input_file = "channels.m3u"
output_file = "channels_with_all.m3u"

# Read original M3U
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Prepare containers
all_category_block = ["#EXTM3U\n"]  # This will hold the ALL category channels
original_channels_block = []        # This will hold the original channels

# Collect all #EXTINF and their next line (URL)
import re # Move import to the top if you use it globally, but keeping it here for context

for i in range(len(lines)):
    if lines[i].startswith("#EXTINF"):
        if i + 1 < len(lines):
            extinf = lines[i]
            url = lines[i + 1]

            # 1. Create the 'ALL' Category Duplicate
            new_extinf = extinf

            if "group-title=" in new_extinf:
                # Replace the group-title content with "ALL"
                new_extinf = re.sub(r'group-title="[^"]+"', 'group-title="ALL"', new_extinf)
            else:
                # If no group-title exists, add group-title="ALL"
                # Using a more robust regex replacement might be safer
                new_extinf = new_extinf.replace("#EXTINF:-1", '#EXTINF:-1 group-title="ALL"')

            # Add to the ALL block
            all_category_block.append(new_extinf)
            all_category_block.append(url)

            # 2. Add the Original Channel to its block
            original_channels_block.append(extinf)
            original_channels_block.append(url)

# Write final M3U: ALL category first + original list
with open(output_file, "w", encoding="utf-8") as f:
    # 1. Write the ALL block
    f.writelines(all_category_block)

    # 2. Write the Original Categories block header
    f.write("\n# -----------------------\n# Original Categories\n# -----------------------\n")
    
    # 3. Write the original channels
    # Note: We skip the first line (#EXTM3U) of the original block if present
    # since all_category_block already started with it.
    f.writelines(original_channels_block)

print(f"✅ Done! Saved as {output_file}")
